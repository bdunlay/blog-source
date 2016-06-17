Title: Interview Questions
Date: 2016-5-25 17:27
Modified: 2016-6-16 22:20
Tags: career,
Slug: interview-questions
Summary: Interview questions I've been asked for software positions.

## Every Interview Question

This is a list of all of the technical interview questions I've ever been asked when applying for software engineering roles. They are grouped together by company, and they are in the order in which they were asked. This begins with questions I was asked while still in college through present day.

### Company 0 (No Offer)

* Write a function to print out all permutations of a string.

### Company 1 (Offer)

* Calculate the degree between the angle of the hands on a clock given the time.
* I pulled this code from the standard library. What does it do? (strtok)
* Implement a doubly-linked list. Insert an element, and delete an element. Is it thread safe?
* Find an element in a sorted array.
* Print out a tree in level-order, one line per level.

### Company 2 (Offer)

* Implement a spell checker in C.

### Company 3 (No Offer)

* Implement memcpy
* Set a bit, clear a bit
* What does the volatile keyword do?
* Reverse a string using the following function signatures: `void reverse(char *str)` and `char* reverse(const char *str)`
* Design a protocol over UART. How would you send binary data over this (text based) protocol? Implement base64 encoding.
* Given an array of integers, find an index (if it exists) in which the sum of all integers on the left of the index and the sum of all integers on the right of the index are equal.

### Company 4 (Offer)

* Fix some (contrived) bugs in the current codebase.

### Company 5 (...)

* Implement strcpy
* Give a presentation on a specified topic to 15 people
* Set a bit, clear a bit, set a mask in a register
* Implement a function to return the nth number of the fibonacci sequence
* Design system to control a pwm-based component
* How to atomically write a register or non-volatile memory?
* What does this code do? Bugs? Improvements? (shuffled 1000 ints from 0-999)
* What features would you include in an RPC framework?
* Implement read, write, ioctl for a GPS device driver in linux
* What is /dev and /etc ?
* Bash questions about how to find file names, how to find contents of files
* How would you store 1.5 in a 16 bit system with no floating point unit?

### Company 6 (No Offer)

* A fellow engineer has asked you to review some code. Identify any possible errors, if they exist (10 question multiple choice).
* Can you apply const modifier to a function?
* Can you manipulate a member variable of a class from a const function?
* How do virtual functions work?
* Name data structures you know and their properties?
* Tell me about a software project you worked on that you are most proud of?
* What are the 4 types of casts in C++?
* What does the register keyword do?
* What does the volatile keyword do?
* What is a friend function and how do you implement it?
* What is a virtual function?
* What is the alignment of a class?
* What is the big O of a "decent" sorting algorithm
* What is the const modifier?
* What is the difference between a reference variable and a pointer?
* Why do we have virtual functions?

### Company 7 (No Offer)

* Given a graph, in which vecticies are frogs, and edges are parent/child relationships, determine if two frogs have a common ancestor.
* Implement a class "BigInt" for working with integers of arbitrary precision, as well as some functions supporting basic mathematical operations (add, subtract, etc).

### Company 8 (...)

* Given an array and a range, count the errors in the array. Errors are defined as follows: a value is missing, duplicated, or out of range. After finding a solution, there is a design change: Return a list of all the errors instead of the count.
* Implement a program to parse SVG path data and calculate a path's distance. Read from stdin, one path per line. Assume that inputs define exactly one closed polygon per line of input, and that no path elements will intersect. Print any errors that might occur to stderr. Ignore comments (prefixed with #) and whitespace.
* Come up with a method to calculate the estimated cut time along that path. Modify the SVG path data program to include this calculation.
* Implement two functions as a part of the provided program, which implements a mock mobile device. The first function is an interrupt handler, being called at a rate of 100Hz and passed x,y, and z coordinates (and a timestamp). The interrupt handler should place data into a queue to be processed by the second function. The second function should process data from the queue and determine when the orientation of a device has changed. When a change in orientation is detected, a single line should be printed to stdout, displaying at what time the change occurred and the new orientation.
