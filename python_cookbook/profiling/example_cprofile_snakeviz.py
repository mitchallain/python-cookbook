import cProfile
import os
from snakeviz import cli

from .algos import factorial, quicksort


def main():
    with cProfile.Profile() as pr:
        factorial(100)
        quicksort([3, 6, 8, 10, 1, 2, 1])
        pr.print_stats()
        os.makedirs("_outputs", exist_ok=True)
        pr.dump_stats("_outputs/profile.out")
        cli.main(["_outputs/profile.out"])


if __name__ == "__main__":
    main()
