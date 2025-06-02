import pytest
from assignment import generate_random_addition_problem, check_addition_problem, generate_random_subtraction_problem, check_subtraction_problem
from assignment import generate_random_multiplication_problem, check_multiplication_problem, generate_random_division_problem, check_division_problem
import random
def test_generate_random_addition_problem_reproducibility():
    random.seed(42)
    problem1 = generate_random_addition_problem()
    
    random.seed(42)
    problem2 = generate_random_addition_problem()
    problem3 = generate_random_addition_problem()
    
    assert problem1 == problem2, "Same seed should produce same addition problem"
    assert problem1 != problem3, "Different calls with same seed should not produce different problems"
    assert isinstance(problem1, str), "Problem should be a string"
    assert '+' in problem1, "Problem should contain a '+' sign"
    

def test_check_addition_problem():
    assert check_addition_problem(5, 7, 12) == True
    assert check_addition_problem(5, 7, 13) == False
    assert check_addition_problem(0, 0, 0) == True
    assert check_addition_problem(100, 200, 300) == True
    

def test_generate_random_subtraction_problem_reproducibility():
    random.seed(42)
    problem1 = generate_random_subtraction_problem()
    
    random.seed(42)
    problem2 = generate_random_subtraction_problem()
    problem3 = generate_random_addition_problem()
    
    assert problem1 == problem2, "Same seed should produce same subtraction problem"
    assert isinstance(problem1, str), "Problem should be a string"
    assert '-' in problem1, "Problem should contain a '-' sign"
    assert problem1 != problem3, "Different calls with same seed should not produce different problems"
    assert eval(problem1) >= 0
    


def test_check_subtraction_problem():
    assert check_subtraction_problem(10, 5, 5) == True
    assert check_subtraction_problem(10, 5, 6) == False
    assert check_subtraction_problem(20, 20, 0) == True
    assert check_subtraction_problem(100, 50, 50) == True

def test_generate_random_multiplication_problem_reproducibility():
    random.seed(42)
    problem1 = generate_random_multiplication_problem()
    
    random.seed(42)
    problem2 = generate_random_multiplication_problem()
    problem3 = generate_random_addition_problem()
    
    assert problem1 == problem2, "Same seed should produce same multiplication problem"
    assert isinstance(problem1, str), "Problem should be a string"
    assert '*' in problem1, "Problem should contain a '*' sign"
    assert problem1 != problem3, "Different calls with same seed should not produce different problems"

def test_check_multiplication_problem():
    assert check_multiplication_problem(5, 7, 35) == True
    assert check_multiplication_problem(5, 7, 34) == False
    assert check_multiplication_problem(0, 5, 0) == True
    assert check_multiplication_problem(10, 10, 100) == True

def test_generate_random_division_problem_reproducibility():
    random.seed(42)
    problem1 = generate_random_division_problem()
    
    random.seed(42)
    problem2 = generate_random_division_problem()
    problem3 = generate_random_addition_problem()
    
    assert problem1 == problem2, "Same seed should produce same division problem"
    assert isinstance(problem1, str), "Problem should be a string"
    assert '/' in problem1, "Problem should contain a '/' sign"
    assert problem1 != problem3, "Different calls with same seed should not produce different problems"

def test_correct_format_of_problem():
    for i in range(10):
        problem = generate_random_division_problem()
        assert isinstance(eval(problem), int)
        assert eval(problem) >= 0
        assert eval(problem) <= 100        

def test_check_division_problem():
    assert check_division_problem(10, 2, 5) == True
    assert check_division_problem(10, 2, 6) == False
    assert check_division_problem(0, 5, 0) == True
    assert check_division_problem(100, 4, 25) == True

def test_check_division_problem_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        check_division_problem(10, 0, 0)

