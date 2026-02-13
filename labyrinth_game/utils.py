import math

from labyrinth_game.constants import ROOMS
from labyrinth_game.player_actions import get_input


def describe_current_room(game_state: dict) -> None:
    room_name = game_state["current_room"]
    room = ROOMS[room_name]

    print(f"\n== {room_name.upper()} ==")
    print(room["description"])

    if room["items"]:
        print("Заметные предметы:", ", ".join(room["items"]))

    exits = ", ".join(sorted(room["exits"].keys()))
    print(f"Выходы: {exits}")

    if room["puzzle"]:
        print("Кажется, здесь есть загадка (используйте команду solve).")


def pseudo_random(seed: int, modulo: int) -> int:
    if modulo <= 0:
        return 0

    value = math.sin(seed * 12.9898) * 43758.5453
    fraction = value - math.floor(value)
    return int(fraction * modulo)


def trigger_trap(game_state: dict) -> None:
    print("Ловушка активирована! Пол стал дрожать...")
    inventory = game_state["player_inventory"]
    seed = game_state["steps_taken"] + len(inventory)

    if inventory:
        lost_index = pseudo_random(seed, len(inventory))
        lost_item = inventory.pop(lost_index)
        print(f"Вы потеряли предмет: {lost_item}")
        return

    damage_roll = pseudo_random(seed + 7, 10)
    if damage_roll < 3:
        print("Ловушка нанесла критический урон. Вы проиграли.")
        game_state["game_over"] = True
        return

    print("Вы чудом уцелели и смогли выбраться из ловушки.")


def random_event(game_state: dict) -> None:
    seed = game_state["steps_taken"]
    event_happened = pseudo_random(seed + 3, 10)

    if event_happened != 0:
        return

    event_type = pseudo_random(seed + 11, 3)
    current_room = game_state["current_room"]

    if event_type == 0:
        print("Вы заметили блеск на полу и нашли coin.")
        room_items = ROOMS[current_room]["items"]
        if "coin" not in room_items:
            room_items.append("coin")
        return

    if event_type == 1:
        print("Где-то рядом слышен тревожный шорох.")
        if "sword" in game_state["player_inventory"]:
            print("Вы демонстрируете меч, и неизвестное существо отступает.")
        return

    if current_room == "trap_room" and "torch" not in game_state["player_inventory"]:
        print("В темноте trap_room вы наступаете не туда.")
        trigger_trap(game_state)


def solve_puzzle(game_state: dict) -> None:
    room_name = game_state["current_room"]
    room = ROOMS[room_name]
    puzzle = room["puzzle"]

    if puzzle is None:
        print("Загадок здесь нет.")
        return

    question, correct_answer = puzzle
    print(question)
    user_answer = get_input("Ваш ответ: ").strip().lower()

    alternatives = {
        "10": {"10", "десять"},
        "шаг шаг шаг": {"шаг шаг шаг"},
        "резонанс": {"резонанс"},
    }
    accepted_answers = alternatives.get(correct_answer, {correct_answer})

    if user_answer not in accepted_answers:
        print("Неверно. Попробуйте снова.")
        if room_name == "trap_room":
            trigger_trap(game_state)
        return

    print("Верно! Загадка решена.")
    room["puzzle"] = None

    rewards = {
        "hall": "silver_coin",
        "trap_room": "gear_token",
        "library": "treasure_key",
    }
    reward = rewards.get(room_name)

    if reward and reward not in game_state["player_inventory"]:
        game_state["player_inventory"].append(reward)
        print(f"Награда за решение: {reward}")


def attempt_open_treasure(game_state: dict) -> None:
    room_name = game_state["current_room"]
    room = ROOMS[room_name]

    if room_name != "treasure_room" or "treasure_chest" not in room["items"]:
        print("Сокровищный сундук здесь недоступен.")
        return

    inventory = game_state["player_inventory"]

    if "treasure_key" in inventory:
        print("Вы применяете ключ, и замок щелкает. Сундук открыт!")
        room["items"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
        return

    print("Сундук заперт. У вас нет treasure_key.")
    choice = get_input("Сундук заперт. Ввести код? (да/нет): ").strip().lower()

    if choice != "да":
        print("Вы отступаете от сундука.")
        return

    puzzle = room["puzzle"]
    if puzzle is None:
        print("Кодовый механизм не отвечает.")
        return

    _, correct_code = puzzle
    entered_code = get_input("Введите код: ").strip().lower()

    accepted_codes = {"10", "десять"} if correct_code == "10" else {correct_code}
    if entered_code in accepted_codes:
        print("Код подошел. Замок открыт!")
        room["items"].remove("treasure_chest")
        room["puzzle"] = None
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
        return

    print("Неверный код. Сундук остается закрытым.")


def show_help(commands: dict) -> None:
    print("\nДоступные команды:")
    for command, description in commands.items():
        print(f"  {command:<16} {description}")
