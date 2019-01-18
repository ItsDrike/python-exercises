* First, let's create a function that will determine for us, if the number we entered is an Armstrong number, it will take `number` parameter
    * Create string form of `number` and save it to `num`
    * Create list with `num` separated by digits and save it as `nums`
    * Iterate through `nums` as `x`
        * Set variable fint to be equal itself + int form of `x` raised to 3rd power
    * If fint value is same as initial number value, **return True**
    * Else **return False**
* Iterate through every number between 1 to 100,000 as `i`
    * Increase `i` by 1
    * Check if number `i` is armstrong number
        * If it is, print `i` is an Armstrong Number
    * **Optional Part (print current number - NOT NECESSARY)**
        * (Optional) Print variable i, end='\r' so we know, what number are we currently on *(don't use if you want it to be fast, this will slow it significantly)*
