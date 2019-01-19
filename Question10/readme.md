### Bank System
Create a bank system, where clients can register/login, make a deposit/withdrawal
and save the information into file
#### Basically:
* Check if user want to login or register
* If register:
    * Ask user for a name and password
    * Save user's name to file
    * Save encrypted password to file
    * Save money amount to file (first amount will be 0 USD)
* If login:
    * Ask user for a name and password
    * Encrypt password and check, if it matches with encrypted password in file
    * If it does:
        * The user will have 3 options:
            * Deposit - Ask user, how much money to add to account
            * Withdrawal - Ask user, how much money to remove from account
            * Logout - Go back to login/register
    * If it does not:
        * Go back to login/register

### Example:
On start-up:
<pre>Welcome, this is PythonBank, please login/register
> Press 1. to Login
> Press 2. to Register
</pre>
User input:
* A:
    <pre>1</pre>
    Output:
    <pre>Please enter your username: </pre>
    Input:
    <pre>username</pre>
    Output:
    <pre>Enter password: </pre>
    Input:
    <pre>password</pre>
    Output:
    * 1:
        <pre>Password has been accepted, welcome username
        Balance: 0 USD.
        1. - Deposit.
        2. - Withdrawal.
        3. - Logout.
        </pre>
        // I won't cover everything ...
    * 2:
        <pre>Password is incorrect</pre>
        -Go back to start-up
* B:
    <pre>2</pre>
    Output:
    <pre>Please enter your new username: </pre>
    Input:
    <pre>username</pre>
    Output:
    <pre>Enter password: </pre>
    Input:
    <pre>password</pre>
    Output:
    * 1:
        <pre>You have been registered, login to continue</pre>
        -Go back to start-up
    * 2:
        <pre>This user aleardy exists, please use diffirent username.</pre>
        -Go back to start-up
//I have not covered everything, but that would just take too long, but this should be enough for you to create functional bank interface

### If it seems to hard, just don't do everything at once, first, just create login system, without file-saving, you can just save to dictionary, this task is harder than most others, so if you don't feel like you can do it, skip it, but you should at least try.
