* Input plain message and save it as `plaintext`
* create `ciphertext` variable
* iterate through every `letter` in `plaintext`
* check if the current `letter` is in alphabet
* if it is:
    * create `num` variable and save ASCII value of current letter
    * add 4 to `num` (4 to right is our key)
    * check if `letter` is A-Z and it's ASCII value is greater than ASCII value of letter *Z*
    * if it is, subtract 26 from `num` (to go back to letter *A*)
    * check if `letter` is a-z and it's ASCII value is greater than ASCII value of letter *z*
    * if it is, subtract 26 from `num` (to go back to letter *a*)
    * set `ciphertext` to ASCII value of `num`
* if it is not:
    * set `ciphertext` to `letter`
* print `ciphertext`
