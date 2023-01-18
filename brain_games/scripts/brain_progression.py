#!/usr/bin/env python3
from brain_games.games import brain_progression
from brain_games import game_engine


def main():
    game_engine.start(brain_progression)


if __name__ == "__main__":
    main()