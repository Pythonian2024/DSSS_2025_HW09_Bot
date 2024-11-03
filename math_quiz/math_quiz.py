import random


def rand_int(min, max): 
    """
    This function return a Random integer between two limits.
    Args:
        min: minimum limit
        max: maximum limit
    return:
        a random integer between min and max
    
    """
    assert(3)
    return random.randint(min, max)


def rand_operation():
    """
    choose random operation
    Return:
        a randomly choose operation
    """
    return random.choice(['+', '-', '*'])


def implement_operation(num_1st, num_2nd, oper):
    """
    implement an operation between two numbers
    args:
        num_1st: first number
        num_2nd: second numbe
        oper: an operation to apply
    return:
        oper_desc: operation discreption 
        result: the result of the implemeted operation
    """

    oper_desc = f"{num_1st} {oper} {num_2nd}"
    if oper == '+': result = num_1st + num_2nd
    elif oper == '-': result = num_1st - num_2nd
    else: result = num_1st * num_2nd
    return oper_desc, result

def math_quiz():
    """
    A function to implement a user_interactive Math Quiz Game

    """
    
    score = 0    
    No_of_attempts = 3  # number of questions to be asked 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(No_of_attempts):
        num_1st = rand_int(1, 10); num_2nd = rand_int(1, 6); oper = rand_operation()

        PROBLEM, ANSWER = implement_operation(num_1st , num_2nd , oper)
        print(f"\nQuestion: {PROBLEM}")
        
        while True:
            
            try:
                useranswer = int(input("Your answer: "))
                break
            
            except ValueError:
                print("Try again! please make sure you enter an integer number!")
                
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{No_of_attempts}")

if __name__ == "__main__":
    math_quiz()
