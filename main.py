# a brute force algorithm to solve a programming by example query over the positive integers with
# addition, multiplication, subtraction, and integer division.
# Supports input-output pairs such as 4 maps to 8, and synthesize the function +4 (as one example).
# This return multiple functions that can produce the output from the input, in the format of "+4" for example
# the possible solutions are tested from an increasing order, from 0 to MAX_BOUND
# and in the order of integer division, multiplication, subtraction, and addition
# TODO fix comments


# largest possible integer
MAX_BOUND = 10
OPERATORS = ['+', '-', '*', '/']
NUMBERS = []
for i in range(MAX_BOUND):
    NUMBERS.append(str(i))


def append_operator(formula):
    results = []
    for n in NUMBERS:
        for operator in OPERATORS:
            # avoid division by 0
            # avoid +/- 0 since this does nothing
            if (operator == '/' or operator == '+' or operator == '-') and n == '0':
                continue
            result = formula + operator + n
            results.append(result)
    return results

def synthesis(x, y):
    results = []
    results.append(str(x))

    counter = 0
    while counter < 4:
        new_results = []
        for r in results:
            if eval(r) == y:
                print(r)
            new_results = new_results + append_operator(r)
        results = new_results
        counter = counter + 1

    valid_result = []
    for r in results:
        if eval(r) == y:
            valid_result.append(r)

    return valid_result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print("Please enter two numbers separated by a space, in the format of 'input output'")
        x, y = map(int, input().split())

        results = synthesis(x, y)
        for result in results:
            print(result + ")=" + str(eval(result)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
