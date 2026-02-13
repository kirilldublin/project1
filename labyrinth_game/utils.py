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

    if user_answer != correct_answer.strip().lower():
        print("Неверно. Попробуйте снова.")
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

    print("Сундук заперт. У вас нет ключа.")
    choice = get_input("Попробовать ввести код? (да/нет): ").strip().lower()

    if choice != "да":
        print("Вы отступаете от сундука.")
        return

    puzzle = room["puzzle"]
    if puzzle is None:
        print("Кодовый механизм не отвечает.")
        return

    _, correct_code = puzzle
    entered_code = get_input("Введите код: ").strip().lower()

    if entered_code == correct_code.strip().lower():
        print("Код подошел. Замок открыт!")
        room["items"].remove("treasure_chest")
        room["puzzle"] = None
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
        return

    print("Неверный код. Сундук остается закрытым.")


def show_help() -> None:
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")
