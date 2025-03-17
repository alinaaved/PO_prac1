import argparse  # Стандартная библиотека

from engine import run_game  # Локальный модуль
from games import gcd, progression  # Локальные модули

GAMES = {
    "gcd": gcd,
    "progression": progression,
}


def main():
    parser = argparse.ArgumentParser(description="Brain Games")
    parser.add_argument("game", choices=GAMES.keys(), help="Game to play")
    args = parser.parse_args()
    run_game(GAMES[args.game])


if __name__ == "__main__":
    main()