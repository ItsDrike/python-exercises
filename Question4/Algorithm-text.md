* Import json module
* Input string and separate it to list by characters, save list to `characters`
* Set variables `counted_chars` (dictionary) and `char_count` integer
* Iterate through every `char` of `characters`
    * If `char` is not space
        * Set `counted_chars` with key: `char` to how many times `char` is in `characters`
        * Add 1 to char_count
* Iterate through every key in `counted_chars`
    * Determine `percentual_appearance` of current character
    * Set this `percentual_appearance` as value of current key in `counted_chars`
* Print `counted_chars` in json format (indent=4)
