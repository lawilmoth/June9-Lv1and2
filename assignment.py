# Answer all the questions. Write "pytest" in the terminal and press enter to see what you answered correctly

#Remember to write 'return' at the end of each function with the answer to the question.



def generate_random_addition_problem():
    """Randomly generate 2 integers between 0 and 10 and return a string representing the addition problem.
    Ex: '3 + 5'
    Ex 2: '1 + 9'
    return the string representation of the addition problem.
    """
    pass # Replace this with your code



def check_addition_problem(x, y, answer):
    """Check if the answer to the addition problem is correct.
    The problem will be x + y where x and y are integers provided as arguments.
    The answer is an integer.
    Return True if the answer is correct, False otherwise.
    Ex: check_addition_problem(3 , 5, 8) -> True, because 3 + 5 = 8
    Ex 2: check_addition_problem(1 , 9, 10) -> False, because 1 + 9 = 10, but the answer is not correct.
    """
    pass # Replace this with your code
    

def generate_random_subtraction_problem():
    """Randomly generate 2 integers between 0 and 10 and return a string representing the subtraction problem.
    Ex: '5 - 3'
    Ex 2: '9 - 1'
    return the string representation of the subtraction problem.
    The problem should be little kid friendly. Answers of should always be positive.
    """
    pass # Replace this with your code

def check_subtraction_problem(x, y, answer):
    """Check if the answer to the subtraction problem is correct.
    The problem will be x - y where x and y are integers provided as arguments.
    The answer is an integer.
    Return True if the answer is correct, False otherwise.
    Ex: check_subtraction_problem(5 , 3, 2) -> True, because 5 - 3 = 2
    Ex 2: check_subtraction_problem(9 , 1, 8) -> False, because 9 - 1 = 8, but the answer is not correct.
    """
    pass # Replace this with your code

def generate_random_multiplication_problem():
    """Randomly generate 2 integers between 0 and 10 and return a string representing the multiplication problem.
    Ex: '3 * 5'
    Ex 2: '1 * 9'
    return the string representation of the multiplication problem.
    """
    pass # Replace this with your code

def check_multiplication_problem(x, y, answer):
    """Check if the answer to the multiplication problem is correct.
    The problem will be x * y where x and y are integers provided as arguments.
    The answer is an integer.
    Return True if the answer is correct, False otherwise.
    Ex: check_multiplication_problem(3 , 5, 15) -> True, because 3 * 5 = 15
    Ex 2: check_multiplication_problem(1 , 9, 10) -> False, because 1 * 9 = 9, but the answer is not correct.
    """
    pass # Replace this with your code

def generate_random_division_problem():
    """Randomly generate 2 integers between 0 and 10 and return a string representing the division problem.
    This problem will be different because we will use the first two numbers to calculate the product before we give the problem.
    num1 = 5, num2 = 3
    product = num1 * num2
    The problem will be 'product / num2' where product is the product of the two numbers.
    This will ensure that the division problem is always little kid friendly.

    Ex: '21/ 3'
    Ex 2: '100 / 10'
    Non-example: '5 / 3' (this is not little kid friendly because the answer is not an integer)

    return the string representation of the division problem.
    The problem should be little kid friendly. Answers of should always be positive integers.
    """
    pass # Replace this with your code

def check_division_problem(x, y, answer):
    """Check if the answer to the division problem is correct.
    The problem will be x / y where x is the product of two integers provided as arguments and y is the second integer.
    The answer is an integer.
    If there write the line below 
            raise DivisionByZeroError("Division by zero is not allowed")
    Return True if the answer is correct, False otherwise.
    Ex: check_division_problem(15 , 3, 5) -> True, because 15 / 3 = 5
    Ex 2: check_division_problem(10 , 2, 5) -> False, because 10 / 2 = 5, but the answer is not correct.

    """
    pass # Replace this with your code