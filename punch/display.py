"""Display punched cards."""

from .encode import Card, Program
from .ibm1401 import ROWS, ROW_ORDER


def _print_card(card: Card, punched_char: str, unpunched_char: str) -> None:
    """Print a single line of a punched card."""
    columns = len(card)

    card_symbols = [[unpunched_char] * columns for _ in range(ROWS)]

    for col, punched_rows in enumerate(card):
        for row in punched_rows:
            row_num = row
            card_symbols[row_num - 1][col] = punched_char

    for row in ROW_ORDER:
        print(f"{row}\t{' '.join(card_symbols[row - 1])}")


def print_program(
    prog: Program, punched_char: str = "◼️", unpunched_char: str = "◻️"
) -> None:
    """Print a representation of a deck of punched cards."""
    for i, card in enumerate(prog):
        header = f"Row\tCard {i + 1} of {len(prog)}\n{'-' * 20}"
        print(f"\n{header}")
        _print_card(card, unpunched_char=unpunched_char, punched_char=punched_char)
