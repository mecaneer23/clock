# Clock

A command line program to display the time in multiple formats.

## Name

clock

## Synopsis

**clock** \[ **-adnpx** \]

## Description

**clock** is a command line program to display the time in multiple formats. Some options include digital and analog, as well as an ncurses or purely printed display. Clock is written in Python.

## Options

| Flag   | Description                                                    |
| ------ | -------------------------------------------------------------- |
| **-a** | Analog clock, this is the default.                             |
| **-d** | Digital watch clock face. This is easier to read but less cool |
| **-n** | Use Ncurses to display the time instead of printing.           |
| **-p** | Print the time to stdout. This is the default                  |
| **-x** | Add a custom time. `./clock.py -x 12 00` |

