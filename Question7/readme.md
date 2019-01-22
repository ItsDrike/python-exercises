### Character counter (percentual character Appearance)
Your task is to write a program that accepts any string, you should return percentual values of each letter in the javascript-like format (use json module for print formating)
#### Basically:
* Input any string
* Count how many time each letter occured (including symbols like '.', but not including spaces (' '))
* Determine percentual value of each occurence of every letter that is in the string (without spaces)
* Fromat them like it is shown in example
* Print out percentual occurences (rounded to 2 decimals) of these letters in **json format** with **indent of 4** (**use json module for print formating**)

#### Example:
<pre>
IN: This is an example sentence. It is used in cases like this, when we do not know, what to type in here as some random string.
OUT:
{
    "T": 1.01,
    "h": 5.05,
    "i": 8.08,
    "s": 11.11,
    "a": 6.06,
    "n": 10.1,
    "e": 14.14,
    "x": 1.01,
    "m": 3.03,
    "p": 2.02,
    "l": 2.02,
    "t": 8.08,
    "c": 2.02,
    ".": 2.02,
    "I": 1.01,
    "u": 1.01,
    "d": 3.03,
    "k": 2.02,
    ",": 2.02,
    "w": 4.04,
    "o": 6.06,
    "y": 1.01,
    "r": 3.03,
    "g": 1.01
}
</pre>
