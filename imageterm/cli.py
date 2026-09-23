import argparse
from .api import api
import sys

def main():
    parser = argparse.ArgumentParser(description="Displays images in the terminal based on arguments")
    parser.add_argument("query", help="Enter tags to search safebooru with (use commas 'r' to seperate multiple tages) :3")

    args = parser.parse_args()

    if not args.query:
        print("No image args given, please give one and try again :3")
        sys.exit()

    tag = args.query
    api(tag)

if __name__ == "__main__":
    main()
