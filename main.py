import argparse
import sys
from src.quick_word.words import words

__version__ = "0.1.0"
__author__ = "Kevin Yokley"
__license__ = "MIT"


parser = argparse.ArgumentParser(
    prog="quick-word",
    description="Dump list of random dictionary words",
)
parser.add_argument("--version", action="store_true")
parser.add_argument(
    "word_count", nargs="?", help="Number of words to generate", type=int, default=0
)

args = parser.parse_args()


def main():
    """Main entry point for the quick_word CLI."""
    version = args.version
    if version:
        print(f" quick-word {__version__}")
        return

    try:
        word_count = int(args.word_count)
    except ValueError:
        print(f"Expected an int. Got '{args.word_count}'")
        sys.exit(1)

    print("\n".join(words(word_count)))


if __name__ == "__main__":
    main()
