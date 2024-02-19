#!/usr/bin/env python3
"""A command line program to display the time in multiple formats."""
# pylint: disable=missing-function-docstring

import os
import sys
from datetime import datetime

from md_to_py import md_table_to_lines


def analog_clock(hours: int, minutes: int) -> list[str]:
    time = _get_analog_time(hours, minutes)
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


def circular_analog(hours: int, minutes: int) -> list[str]:
    time = _get_analog_time(hours, minutes)
    return [
        r"         , - ~ - ,         ",
        r"     , '     12    ' ,     ",
        r"   ,     11      1     ,   ",
        f"  ,   10 {time[0]} 2    ,  ",
        f" ,       {time[1]}       , ",
        f" ,  9    {time[2]}    3  , ",
        f" ,       {time[3]}       , ",
        f"  ,    8 {time[4]} 4    ,  ",
        r"   ,     7       5     ,   ",
        r"     ,       6     , '     ",
        r"       ' - ,___ , '        ",
    ]


def _get_analog_time(hours: int, minutes: int) -> list[str]:
    guard_inputs(hours, minutes)
    hours = to_twelve_hours(hours)
    minutes = int(round_to_nearest_minutes(minutes)) // 5
    return [
        combine_strings(h, m)
        for h, m in zip(time_to_analog(hours, 1), time_to_analog(minutes, 0))
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
    if not (0 < hours <= 24 and 0 <= minutes <= 59):
        raise ValueError("Invalid time")


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
    from curses import use_default_colors, wrapper

    def inner(stdscr):
        use_default_colors()
        stdscr.clear()
        for row in ascii_array:
            stdscr.addstr(row + "\n")
        stdscr.refresh()
        stdscr.getkey()

    wrapper(inner)


def main(args: str = "", xtime: tuple[int, int] = (0, 0)) -> None:
    if "h" in args:
        print(
            "\n".join(
                md_table_to_lines(
                    19, 29, f"{os.path.dirname(__file__)}/README.md", ("**",)
                )
            )
        )
        return

    if "x" in args:
        time = xtime
        args = args.replace("x", "")
    else:
        time = [int(i) for i in datetime.now().strftime("%H %M").split()]
    if "t" in args:
        print(to_twelve_hours(time[0]), str(time[1]).ljust(2, "0"), sep=":")
        return
    clock = {"d": digital_watch, "c": circular_analog}.get(args, analog_clock)
    display = ncurses_ascii if "n" in args else print_ascii
    display(clock(*time))


if __name__ == "__main__":
    if len(sys.argv) > 3 and sys.argv[1].startswith("-"):
        main(sys.argv[1][1:], (int(sys.argv[2]), int(sys.argv[3])))
    elif len(sys.argv) > 1 and sys.argv[1].startswith("-"):
        main(sys.argv[1][1:])
    else:
        main()
