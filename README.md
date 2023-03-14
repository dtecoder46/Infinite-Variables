# Story

I was coding my own programming language when I suddenly noticed that the inputs were being appended together on the same string. To prevent this, I stumbled upon this method of creating any number of empty string variables that could be saved under another variable, which is what this program summarizes.

# Function

First, the initial empty string and a variable value are declared. A for loop is then utilized, and because for loops can iterate through various numbers, the number from the for loop statement replaces the ending letter of the initial empty string variable, and this is saved into a different variable. 
Therefore, for each number iterated by the for loop, a different variable named is created under the same variable. Then, any string can be appended to the other variable (which stores the new variable name), so the following strings will not pile up onto the same variable, making the output look nicer.