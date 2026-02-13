# project1_kirilldublin

Консольная текстовая игра на Python: **"Лабиринт сокровищ"**.

Игрок перемещается по комнатам, подбирает предметы, решает загадки, сталкивается
со случайными событиями и пытается открыть сундук в сокровищнице.

## Установка

```bash
make install
```

Альтернатива:

```bash
poetry install
```

## Запуск

```bash
make project
```

Альтернатива:

```bash
poetry run project
```

## Полезные команды

- `go <direction>` или `north/south/east/west`
- `look`
- `take <item>`
- `use <item>`
- `inventory`
- `solve`
- `help`
- `quit`

## Проверка качества

```bash
make lint
```

## Демонстрация (asciinema)

```markdown
[![asciicast](https://asciinema.org/a/LP3deYaWukb14guv.svg)](https://asciinema.org/a/LP3deYaWukb14guv)
```

## Структура проекта

- `labyrinth_game/main.py` — точка входа, цикл игры, обработка команд.
- `labyrinth_game/constants.py` — константы, карта комнат, список команд.
- `labyrinth_game/player_actions.py` — действия игрока и изменение `game_state`.
- `labyrinth_game/utils.py` — описание комнат, загадки, случайные события, ловушки.
