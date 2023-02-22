#!/usr/bin/env python3

def analog_clock(hours, minutes):
    if guard_inputs(hours, minutes):
        return
    print(hours, minutes)

def digital_watch(hours, minutes):
    if guard_inputs(hours, minutes):
        return

def guard_inputs(hours, minutes):
    return 0 < hours <= 12 and 0 < minutes <= 60

def main():
    from datetime import datetime
    print(datetime.now())
    analog_clock(*[int(i) for i in datetime.now().strftime("%H %M").split()])

if __name__ == "__main__":
    main()
