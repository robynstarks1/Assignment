# Program Start

# Define a function to greet the user
DEFINE function greet_user()
    PROMPT user for their name
    STORE user input in variable 'name'
    PRINT "Welcome, " + name

# Define a function to check if a number is even or odd
DEFINE function check_even_odd(number)
    IF number MODULO 2 is equal to 0
        PRINT "Even"
    ELSE
        PRINT "Odd"

# Main program execution
CALL greet_user()  # Call the function to greet the user
PROMPT user for a number and convert it to an integer
STORE input in variable 'number'
CALL check_even_odd(number)  # Call the function to check even/odd status

# Program End
