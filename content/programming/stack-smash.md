Title: Stack SMASH
Date: 2016-5-28 23:59
Tags: programming, C, embedded systems, gdb
Slug: stack-smash

I'm writing an application for my UW Embedded Systems class. The project is to read IMU sensor data, fuse it together, and report the data on an LCD or over bluetooth (or both).

I spent a lot of today trying to read data and pass it between tasks in FreeRTOS and learned a couple of things.

## Stack Smashing

I ended up smashing my stack a lot today, but didn't know it until many hours too late. My program would just crash inexplicably and end up in the HardFault handler. In order to retry I'd have to reset the device, reload gdb, etc. I couldn't figure out the root cause and spent the better part of a day limping along.

Then I finally figured it out, after allocating a 100 char buffer -- I checked my stack size and it hit me. 128 bytes. Definitely not gonna cut it.

Small lesson, but one definitely learned.

## sprintf

This is more of a RTFM sort of lesson. Spent some time painfully trying to print stuff out over UART today. Realized late this evening that I can use sprintf to print a formatted string to a buffer and then send that whole thing out over UART rather than trying to clobber things together in multiple calls. Much cleaner! Still need to figure out how adjust the internals of printf to just print out over UART instead of stdout, but that's low priority right now.

## functions in gdb

This is one of my favorite. You can define functions in gdb! Here's a simple example.

Say you set a breakpoint, and you want to continue the program execution back to that breakpoint and then print out a local variable. You want to repeat that a few times to watch it change. It's two commands (after you've set the breakpoint):

```
print myData
c
```

You can toggle the history (up arrow) to achieve this, which isn't too hard, or you can define both functions in one line:

```
(gdb) def loopnprint
Type commands for definition of "loopnprint".
End with a line saying just "end".
>print i
>c
>end
(gdb) loopnprint
$1 = 0

Breakpoint 2, StartFuseSensorTask (argument=0x0) at Src/main.c:341
$2 = 1

Breakpoint 2, StartFuseSensorTask (argument=0x0) at Src/main.c:341
$3 = 2

Breakpoint 2, StartFuseSensorTask (argument=0x0) at Src/main.c:341
(gdb)
```

Now all you have to do is hit enter!
