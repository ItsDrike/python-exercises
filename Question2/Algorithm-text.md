* First let's create a user-defined function for fibonacci numbers and call it `fibonacci()`, that will take `n` parameter (the `n` parameter will say what number in sequence the function will return)
    * If n is 0, output 0
    * If n is 1, output 1
    * Else, output `fibonacci(n - 1) + fibonacci(n - 2)`
* Now let's create list called `even_fibonacci`, for now empty, but this will contain our even fibonacci numbers
* Iterate through range 1-10000 as `n`
    * Set `fib` to fibonacci number `n` (using our user-function)
    * If `fib` is divisible by 2
        * Add `fib` to `even_fibonacci` as string (string form is used, so it can be formated easier when we will be printing it out)
    * If `fib` is higher than 10000, break the loop (we reached our maximum)
* print `even_fibonacci` formated in a way, so every number is followed by ', '
