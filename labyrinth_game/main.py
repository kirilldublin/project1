#!/usr/bin/env python3

from labyrinth_game.constants import COMMANDS
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    solve_puzzle,
)


def process_command(game_state: dict, command_line: str, commands: dict) -> None:
    raw_parts = command_line.strip().lower().split(maxsplit=1)

    if not raw_parts:
        return

    command = raw_parts[0]
    argument = raw_parts[1] if len(raw_parts) > 1 else ""

    match command:
        case "look":
            describe_current_room(game_state)
        case "go":
            move_player(game_state, argument)
        case "north" | "south" | "east" | "west":
            move_player(game_state, command)
        case "take":
            take_item(game_state, argument)
        case "use":
            use_item(game_state, argument)
        case "inventory":
            show_inventory(game_state)
        case "solve":
            if game_state["current_room"] == "treasure_room":
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case "help":
            show_help(commands)
        case "quit" | "exit":
            game_state["game_over"] = True
            print("Игра завершена.")
        case _:
            print("Неизвестная команда. Введите help, чтобы увидеть список команд.")


def main() -> None:
    game_state = {
        "player_inventory": [],
        "current_room": "entrance",
        "game_over": False,
        "steps_taken": 0,
    }

    print("Добро пожаловать в Лабиринт сокровищ!")
    print("Введите help, чтобы посмотреть команды.")
    describe_current_room(game_state)

    while not game_state["game_over"]:
        command_line = get_input("> ")
        process_command(game_state, command_line, COMMANDS)


if __name__ == "__main__":
    main()
