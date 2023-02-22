#!/usr/bin/env python3


def analog_clock(hours, minutes):
    guard_inputs(hours, minutes)
    hours = to_twelve_hours(hours)
    minutes = int(round_to_nearest_minutes(minutes)) // 5
    time = [combine_strings(h, m) for h, m in zip(time_to_analog(hours, 1), time_to_analog(minutes, 0))]
    return [
         r"        _____        ",
         r"     _.'_____'._     ",
         r"   .'.-'  12 '-.'.   ",
         r"  /.' 11      1 '.\  ",
        fr" // 10{time[0]} 2 \\ ",
        fr"::    {time[1]}    ::",
        fr"|| 9  {time[2]}  3 ||",
        fr"::    {time[3]}    ::",
        fr" \\ 8 {time[4]} 4 // ",
         r"  '. 7        5 .'/  ",
         r"   '.'-.__6__.-'.'   ",
         r"    ((-._____.-))    ",
         r"    _))       ((_    ",
         r"   '--'       '--'   ",
    ]


def time_to_analog(time, short=0):
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


def combine_strings(a, b):
    output = ""
    for x, y in zip(a, b):
        if x == y:
            output += x
        else:
            output += chr(max(ord(x), ord(y)))
    return output


def digital_watch(hours, minutes):
    guard_inputs(hours, minutes)
    minutes = str(minutes).rjust(2, "0")
    hours = to_twelve_hours(hours)
    a = time_to_digital(1)[1:] if len(str(hours)) == 2 else ["   ", "   "]
    b = time_to_digital(int(str(hours)[-1]))
    c = time_to_digital(int(minutes[0]))
    d = time_to_digital(int(minutes[1]))
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
         fr"{{   /   {b[0]}   {c[0]} {d[0]} \   }}  ",
         fr"|  {{{a[0]} {b[1]} . {c[1]} {d[1]}  }}  |-.",
         fr"|  |{a[1]} {b[2]} . {c[2]} {d[2]}  |  | |",
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


def time_to_digital(time):
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


def guard_inputs(hours, minutes):
    if 0 < hours <= 24 and 0 <= minutes < 59:
        return
    raise ValueError("Invalid time")


def to_twelve_hours(hours):
    return (hours - 12) if hours > 12 else hours


def round_to_nearest_minutes(minutes):
    remainder = minutes % 5
    return str(
        minutes + 5 - remainder
        if remainder > 2
        else minutes - remainder
    ).rjust(2, "0")


def print_ascii(ascii_array):
    for row in ascii_array:
        print(row)


def ncurses_ascii():
    import curses


def main(args=""):
    from datetime import datetime

    time = [int(i) for i in datetime.now().strftime("%H %M").split()]
    clock = digital_watch if "d" in args else analog_clock
    display = ncurses_ascii if "n" in args else print_ascii
    display(clock(*time))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1].startswith("-"):
        main(sys.argv[1][1:])
    else:
        main()