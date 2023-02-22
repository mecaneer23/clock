#!/usr/bin/env python3


def analog_clock(hours, minutes):
    guard_inputs(hours, minutes)
    hours = to_twelve_hours(hours)
    minutes = int(round_to_nearest_minutes(minutes)) // 5
    time = [combine_strings(h, m) for h, m in zip(time_to_ascii(hours, 1), time_to_ascii(minutes, 0))]
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


def time_to_ascii(time, short=0):
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


def main():
    from datetime import datetime

    print_ascii(analog_clock(*[int(i) for i in datetime.now().strftime("%H %M").split()]))


if __name__ == "__main__":
    main()
