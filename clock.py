#!/usr/bin/env python3

from typing import List


def analog_clock(hours: int, minutes: int) -> list[str]:
    guard_inputs(hours, minutes)
    hours = to_twelve_hours(hours)
    minutes = int(round_to_nearest_minutes(minutes)) // 5
    if minutes > 9:
        hours += 1
    time = [
        combine_strings(h, m)
        for h, m in zip(time_to_analog(hours, 1), time_to_analog(minutes, 0))
    ]
    return [
        r"        _____        ",
        r"     _.'_____'._     ",
        r"   .'.-'  12 '-.'.   ",
        r"  /.' 11      1 '.\  ",
        rf" // 10{time[0]} 2 \\ ",
        rf"::    {time[1]}    ::",
        rf"|| 9  {time[2]}  3 ||",
        rf"::    {time[3]}    ::",
        rf" \\ 8 {time[4]} 4 // ",
        r"  '. 7        5 .'/  ",
        r"   '.'-.__6__.-'.'   ",
        r"    ((-._____.-))    ",
        r"    _))       ((_    ",
        r"   '--'       '--'   ",
    ]


def time_to_analog(time: int, short: int = 0):
    """short is a boolean value (0 or 1)"""
    return [
        [
            [
                r"    |    ",
                r"    |    ",
                r"    O    ",
                r"         ",
                r"         ",
            ],
            [
                r"         ",
                r"    |    ",
                r"    O    ",
                r"         ",
                r"         ",
            ],
        ],
        [
            [
                r"      /  ",
                r"     /   ",
                r"    O    ",
                r"         ",
                r"         ",
            ],
            [
                r"         ",
                r"     /   ",
                r"    O    ",
                r"         ",
                r"         ",
            ],
        ],
        [
            [
                r"         ",
                r"        /",
                r"    O--  ",
                r"         ",
                r"         ",
            ],
            [
                r"         ",
                r"        /",
                r"    O    ",
                r"         ",
                r"         ",
            ],
        ],
        [
            [
                r"         ",
                r"         ",
                r"    O----",
                r"         ",
                r"         ",
            ],
            [
                r"         ",
                r"         ",
                r"    O--  ",
                r"         ",
                r"         ",
            ],
        ],
        [
            [
                r"         ",
                r"         ",
                r"    O--  ",
                "        \\",
                r"         ",
            ],
            [
                r"         ",
                r"         ",
                r"    O    ",
                "        \\",
                r"         ",
            ],
        ],
        [
            [
                r"         ",
                r"         ",
                r"    O    ",
                r"     \   ",
                r"      \  ",
            ],
            [
                r"         ",
                r"         ",
                r"    O    ",
                r"     \   ",
                r"         ",
            ],
        ],
        [
            [
                r"         ",
                r"         ",
                r"    O    ",
                r"    |    ",
                r"    |    ",
            ],
            [
                r"         ",
                r"         ",
                r"    O    ",
                r"    |    ",
                r"         ",
            ],
        ],
        [
            [
                r"         ",
                r"         ",
                r"    O    ",
                r"   /     ",
                r"  /      ",
            ],
            [
                r"         ",
                r"         ",
                r"    O    ",
                r"   /     ",
                r"         ",
            ],
        ],
        [
            [
                r"         ",
                r"         ",
                r"  --O    ",
                r"/        ",
                r"         ",
            ],
            [
                r"         ",
                r"         ",
                r"    O    ",
                r"/        ",
                r"         ",
            ],
        ],
        [
            [
                r"         ",
                r"         ",
                r"----O    ",
                r"         ",
                r"         ",
            ],
            [
                r"         ",
                r"         ",
                r"  --O    ",
                r"         ",
                r"         ",
            ],
        ],
        [
            [
                r"         ",
                r"\        ",
                r"  --O    ",
                r"         ",
                r"         ",
            ],
            [
                r"         ",
                r"\        ",
                r"    O    ",
                r"         ",
                r"         ",
            ],
        ],
        [
            [
                r"  \      ",
                r"   \     ",
                r"    O    ",
                r"         ",
                r"         ",
            ],
            [
                r"         ",
                r"   \     ",
                r"    O    ",
                r"         ",
                r"         ",
            ],
        ],
    ][0 if time == 12 else time][short]


def combine_strings(a: str, b: str) -> str:
    output = ""
    for x, y in zip(a, b):
        if x == y:
            output += x
        else:
            output += chr(max(ord(x), ord(y)))
    return output


def md_table_to_lines(
    first_line_idx: int,
    last_line_idx: int,
    filename: str = "README.md",
    remove: List[str] = [],
) -> List[str]:
    """
    Converts a markdown table to a list of formatted strings.

    Args:
        first_line_idx (int): The index of the first line of the markdown table to be converted.
        last_line_idx (int): The index of the last line of the markdown table to be converted.
        filename (str, optional): The name of the markdown file containing the table. Default is "README.md".
        remove (list[str], optional): The list of strings to be removed from each line. This is in the case of formatting that should exist in markdown but not python. Default is an empty list.

    Returns:
        list[str]: A list of formatted strings representing the converted markdown table.

    Raises:
        ValueError: If the last line index is less than or equal to the first line index.
        FileNotFoundError: If the specified markdown file cannot be found.
    """

    # Check for valid line indices
    if last_line_idx <= first_line_idx:
        raise ValueError("Last line index must be greater than first line index.")

    # Get raw lines from the markdown file
    try:
        with open(filename) as f:
            lines = f.readlines()[first_line_idx - 1 : last_line_idx - 1]
    except FileNotFoundError:
        raise FileNotFoundError("Markdown file not found.")

    # Remove unwanted characters and split each line into a list of values
    for i, _ in enumerate(lines):
        for item in remove:
            lines[i] = lines[i].replace(item, "")
        lines[i] = lines[i].split("|")[1:-1]
    column_count = len(lines[0])
    lines[1] = ["-" for _ in range(column_count)]

    # Create lists of columns
    columns = [[0, []] for _ in range(column_count)]
    for i in range(column_count):
        for line in lines:
            columns[i][1].append(line[i])

    # Find the maximum length of each column
    for i, (_, v) in enumerate(columns):
        columns[i][0] = len(max([w.strip() for w in v], key=len))
    lines[1] = ["-" * (l + 1) for l, _ in columns]

    # Join the lines together into a list of formatted strings
    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            line[j] = v.strip().ljust(columns[j][0] + 2)
        lines[i] = "".join(lines[i])
    lines[1] = "-" * (
        sum(columns[i][0] for i, _ in enumerate(columns)) + 2 * (len(columns) - 1)
    )
    return lines


def digital_watch(hours: int, minutes: int) -> list[str]:
    guard_inputs(hours, minutes)
    minutes_tens, minutes_ones = str(minutes).rjust(2, "0")
    hours = to_twelve_hours(hours)
    a = time_to_digital(1)[1:] if len(str(hours)) == 2 else ["   ", "   "]
    b = time_to_digital(int(str(hours)[-1]))
    c = time_to_digital(int(minutes_tens))
    d = time_to_digital(int(minutes_ones))
    return [
        r"       .--.-----.--.         ",
        r"       |--|-----|--|         ",
        r"       |--|     |--|         ",
        r"       |  |-----|  |         ",
        r"     __|--|     |--|__       ",
        r"    /  |  |-----|  |  \      ",
        r"   /   \__|-----|__/   \     ",
        r"  /   ______---______   \/\  ",
        r" /   /               \   \/  ",
        rf"{{   /   {b[0]}   {c[0]} {d[0]} \   }}  ",
        rf"|  {{{a[0]} {b[1]} . {c[1]} {d[1]}  }}  |-.",
        rf"|  |{a[1]} {b[2]} . {c[2]} {d[2]}  |  | |",
        r"|  {                   }  |-'",
        r"{   \                 /   }  ",
        r" \   `------___------'   /\  ",
        r"  \     __|-----|__     /\/  ",
        r"   \   /  |-----|  \   /     ",
        r"    \  |--|     |--|  /      ",
        r"     --|  |-----|  |--       ",
        r"       |--|     |--|         ",
        r"       |--|-----|--|         ",
        r"       '--'-----'--'         ",
    ]


def time_to_digital(time: int) -> list[str]:
    return [
        [
            " _ ",
            "| |",
            "|_|",
        ],
        [
            "   ",
            "  |",
            "  |",
        ],
        [
            " _ ",
            " _|",
            "|_ ",
        ],
        [
            " _ ",
            " _|",
            " _|",
        ],
        [
            "   ",
            "|_|",
            "  |",
        ],
        [
            " _ ",
            "|_ ",
            " _|",
        ],
        [
            " _ ",
            "|_ ",
            "|_|",
        ],
        [
            " _ ",
            "  |",
            "  |",
        ],
        [
            " _ ",
            "|_|",
            "|_|",
        ],
        [
            " _ ",
            "|_|",
            " _|",
        ],
    ][time]


def guard_inputs(hours: int, minutes: int) -> None:
    assert 0 < hours <= 24 and 0 <= minutes <= 59, "Invalid time"


def to_twelve_hours(hours: int) -> int:
    return (hours - 12) if hours > 12 else hours


def round_to_nearest_minutes(minutes: int) -> str:
    remainder = minutes % 5
    return str(minutes + 5 - remainder if remainder > 2 else minutes - remainder).rjust(
        2, "0"
    )


def print_ascii(ascii_array: list[str]) -> None:
    for row in ascii_array:
        print(row)


def ncurses_ascii(ascii_array: list[str]) -> None:
    from curses import wrapper, use_default_colors

    def inner(stdscr):
        use_default_colors()
        stdscr.clear()
        for row in ascii_array:
            stdscr.addstr(row + "\n")
        stdscr.refresh()
        return stdscr.getkey()

    wrapper(inner)


def main(args: str = "", xtime: tuple[int, int] = (0, 0)) -> None:
    if "h" in args:
        import os

        print(
            "\n".join(
                md_table_to_lines(
                    19, 28, f"{os.path.dirname(__file__)}/README.md", ["**"]
                )
            )
        )
        return

    from datetime import datetime

    time = (
        xtime
        if "x" in args
        else [int(i) for i in datetime.now().strftime("%H %M").split()]
    )
    if "t" in args:
        print(to_twelve_hours(time[0]), str(time[1]).ljust(2, "0"), sep=":")
        return
    clock = digital_watch if "d" in args else analog_clock
    display = ncurses_ascii if "n" in args else print_ascii
    display(clock(*time))


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 3 and sys.argv[1].startswith("-"):
        main(sys.argv[1][1:], (int(sys.argv[2]), int(sys.argv[3])))
    elif len(sys.argv) > 1 and sys.argv[1].startswith("-"):
        main(sys.argv[1][1:])
    else:
        main()
