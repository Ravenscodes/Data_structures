from Stack import MyStack


def evaluate_post_fix(exp):
    stack = MyStack()
    try:
        for char in exp:
            if char.isdigit():
                # Push numbers in stack
                stack.push(char)
            else:
                # use top two numbers and evaluate
                right = stack.pop()
                left = stack.pop()
                ''' Using Python's eval () method that takes a str expression, 
                evaluates it and returns an integer '''
                stack.push(str(eval(left + char + right)))
        # final answer should be a number
        return int(float(stack.pop()))
    except TypeError:
        return "Invalid Sequence"


if __name__ == "__main__" :
    print("Result of expression (921*-8-4+) : " + str(evaluate_post_fix("921*-8-4+")))
    print("Result of expression (921*-8--4+) : " + str(evaluate_post_fix("921*-8--4+")))