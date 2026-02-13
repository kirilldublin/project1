from labyrinth_game.constants import ROOMS


def normalize_name(raw_value: str) -> str:
    return raw_value.strip().lower().replace(" ", "_")


def get_input(prompt: str = "> ") -> str:
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def show_inventory(game_state: dict) -> None:
    inventory = game_state["player_inventory"]
    if not inventory:
        print("Инвентарь пуст.")
        return

    print("Инвентарь:", ", ".join(inventory))


def move_player(game_state: dict, direction: str) -> None:
    current_room = game_state["current_room"]
    room = ROOMS[current_room]
    normalized_direction = normalize_name(direction)

    if normalized_direction not in room["exits"]:
        print("Нельзя пойти в этом направлении.")
        return

    game_state["current_room"] = room["exits"][normalized_direction]
    game_state["steps_taken"] += 1

    from labyrinth_game.utils import describe_current_room

    describe_current_room(game_state)


def take_item(game_state: dict, item_name: str) -> None:
    if not item_name:
        print("Укажите предмет: take <item>.")
        return

    normalized_item = normalize_name(item_name)
    current_room = game_state["current_room"]
    room_items = ROOMS[current_room]["items"]

    if normalized_item == "treasure_chest":
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return

    if normalized_item not in room_items:
        print("Такого предмета здесь нет.")
        return

    room_items.remove(normalized_item)
    game_state["player_inventory"].append(normalized_item)
    print(f"Вы подняли: {normalized_item}")


def use_item(game_state: dict, item_name: str) -> None:
    if not item_name:
        print("Укажите предмет: use <item>.")
        return

    normalized_item = normalize_name(item_name)
    inventory = game_state["player_inventory"]

    if normalized_item not in inventory:
        print("У вас нет такого предмета.")
        return

    if normalized_item == "torch":
        print("Вы зажигаете факел. В лабиринте становится заметно светлее.")
        return

    if normalized_item == "sword":
        print("Вы берете меч в руку. Вы чувствуете уверенность.")
        return

    if normalized_item == "bronze_box":
        if "rusty_key" not in inventory:
            inventory.append("rusty_key")
            print("Вы открываете бронзовую шкатулку и находите rusty_key.")
            return

        print("Шкатулка уже открыта. Внутри больше ничего нет.")
        return

    print("Вы пока не знаете, как использовать этот предмет.")
