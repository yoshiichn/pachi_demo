import random
import time
from playsound import playsound
from pathlib import Path

hit_numbers = range(100, 3190, 100)
win_numbers = [111, 222, 333, 444, 555, 666, 777, 888]
sounds_dir = Path(__file__).parents[1] / "sounds"
fever_sound = sounds_dir / "fever.mp3"
hit_sound = sounds_dir / "hit.mp3"


def play_fever():
    print("fever")
    playsound(fever_sound)


def play_winning():
    print("GARO")
    playsound(hit_sound)


def is_chance(ball: int) -> bool:
    return ball in hit_numbers


def is_fever(ball: int) -> bool:
    return ball in win_numbers


def main():
    while True:
        ball = random.randint(1, 3190)
        if is_chance(ball):
            play_winning
        if is_fever(ball):
            play_fever()
        time.sleep(1)


if __name__ == "__main__":
    main()
