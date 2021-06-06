# Entrance Exam CS MSc
### The Task
Create a program named Dice to solve the following exercises. 
The input of the program is a so-called trial, i.e. a sequence of the rolled results. This input must be read from the standard input.<br>
The first line of the input contains a single integer N, indicating the number of throws 1 ≤ N ≤ 1000000. <br>
The second line of the input contains exactly N characters, each character is a digit from 1 to 6. <br>
<br>
The output of the program should be written to the standard output. There are 3 exercises you are expected to solve. <br>
The output should contain exactly 3 lines: the ith line in the output is the solution to exercise i. <br>
#### Exercise 1
How many times did it occur in the trial, that exactly two 6s were rolled after each other? <br>
#### Exercise 2
Find the length of the longest subsequence of successive rolls, in which the value 6 does not occur. <br>
#### Exercise 3
We shall call a sequence of successive rolls in the trial a lucky series, if the sequence contains only 5s and 6s. <br>
Find out, which is the most frequent length for lucky series. If there are more than one "most frequent" lucky series lengths, print the longest. If there are no lucky series in the trial, print zero.

### This version is slightly modified
This version is modified to read the input from a file for easier testing. <br>
Run the script with (from within the folder)
```
python3 Dice.py
