import argparse

from .encode import encode_source
from .display import print_program


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="punchcard-python",
        description="Encode Python to a punched card and visualize.",
    )
    parser.add_argument(
        "--file",
        "-f",
        default=None,
        type=argparse.FileType("r"),
        help="The Python file to encode.",
    )
    parser.add_argument(
        "--source",
        "-s",
        default=None,
        type=str,
        help="Python source pass as string to encode.",
    )
    parser.add_argument(
        "--columns",
        "-c",
        default=80,
        type=int,
        help="The number of columns on the punched card.",
    )
    parser.add_argument(
        "--punched-char",
        "-p",
        default="◼️",
        type=str,
        help="Character to represent punched holes.",
    )
    parser.add_argument(
        "--unpunched-char",
        "-u",
        default="◻️",
        type=str,
        help="Character to represent unpunched holes.",
    )

    args = parser.parse_args()

    if args.file:
        with open(args.file) as src:
            source = src.read()
    elif args.source:
        source = args.source
    else:
        parser.error("Pass in either --file or --source.")

    try:
        encoded = encode_source(source, columns=args.columns)
        print_program(
            encoded, punched_char=args.punched_char, unpunched_char=args.unpunched_char
        )
    except Exception as e:
        parser.error(e)
