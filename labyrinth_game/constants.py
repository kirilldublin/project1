COMMANDS = {
    "go <direction>": "перейти в направлении (north/south/east/west)",
    "north/south/east/west": "быстрое перемещение без команды go",
    "look": "осмотреть текущую комнату",
    "take <item>": "поднять предмет",
    "use <item>": "использовать предмет из инвентаря",
    "inventory": "показать инвентарь",
    "solve": "попытаться решить загадку в комнате",
    "quit": "выйти из игры",
    "help": "показать это сообщение",
}

HELP_COLUMN_WIDTH = 16

# Константы псевдослучайного генератора.
PR_SIN_MULTIPLIER = 12.9898
PR_SCRAMBLE_MULTIPLIER = 43758.5453

# Константы механики ловушек и случайных событий.
TRAP_DAMAGE_MODULO = 10
TRAP_DEFEAT_THRESHOLD = 3
TRAP_DAMAGE_SEED_OFFSET = 7
EVENT_TRIGGER_MODULO = 10
EVENT_TRIGGER_VALUE = 0
EVENT_TRIGGER_SEED_OFFSET = 3
EVENT_TYPE_MODULO = 3
EVENT_TYPE_SEED_OFFSET = 11

# Награды и альтернативные ответы для загадок.
PUZZLE_REWARDS = {
    "hall": "silver_coin",
    "trap_room": "gear_token",
    "library": "treasure_key",
}

ALTERNATIVE_ANSWERS = {
    "10": {"10", "десять"},
    "шаг шаг шаг": {"шаг шаг шаг"},
    "резонанс": {"резонанс"},
}

ROOMS = {
    "entrance": {
        "description": (
            "Вы в темном входе лабиринта. Стены покрыты мхом. "
            "На полу лежит старый факел."
        ),
        "exits": {"north": "hall", "east": "trap_room"},
        "items": ["torch"],
        "puzzle": None,
    },
    "hall": {
        "description": (
            "Большой зал с эхом. По центру стоит пьедестал с запечатанным "
            "сундуком."
        ),
        "exits": {"south": "entrance", "west": "library", "north": "treasure_room"},
        "items": [],
        "puzzle": (
            "На пьедестале надпись: 'Назовите число, которое идет после девяти'. "
            "Введите ответ цифрой или словом.",
            "10",
        ),
    },
    "trap_room": {
        "description": (
            "Комната с хитрой плиточной ловушкой. На стене надпись: "
            "'Осторожно - ловушка'."
        ),
        "exits": {"west": "entrance"},
        "items": ["rusty_key"],
        "puzzle": (
            "Система плит активна. Чтобы пройти, назовите слово 'шаг' три раза "
            "подряд (введите 'шаг шаг шаг').",
            "шаг шаг шаг",
        ),
    },
    "library": {
        "description": (
            "Пыльная библиотека. На полках старые свитки. Где-то здесь может "
            "быть ключ от сокровищницы."
        ),
        "exits": {"east": "hall", "north": "armory"},
        "items": ["ancient_book"],
        "puzzle": (
            "В одном свитке загадка: 'Что растет, когда его съедают?' "
            "(ответ одно слово)",
            "резонанс",
        ),
    },
    "armory": {
        "description": (
            "Старая оружейная комната. На стене висит меч, рядом - небольшая "
            "бронзовая шкатулка."
        ),
        "exits": {"south": "library"},
        "items": ["sword", "bronze_box"],
        "puzzle": None,
    },
    "treasure_room": {
        "description": (
            "Комната, на столе большой сундук. Дверь заперта - нужен "
            "особый ключ."
        ),
        "exits": {"south": "hall"},
        "items": ["treasure_chest"],
        "puzzle": (
            "Дверь защищена кодом. Введите код (подсказка: это число "
            "пятикратного шага, 2*5=?).",
            "10",
        ),
    },
}
