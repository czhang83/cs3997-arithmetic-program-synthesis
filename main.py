# a brute force algorithm to solve a programming by example query over the positive integers with
# addition, multiplication, subtraction, and integer division.
# Supports input-output pairs such as 4 maps to 8, and synthesize the function +4 (as one example).
# This return multiple functions that can produce the output from the input, in the format of "+4" for example
# the possible solutions are tested from an increasing order, from 0 to MAX_BOUND
# and in the order of integer division, multiplication, subtraction, and addition


# largest possible integer
MAX_BOUND = 10

def synthesis(x, y):
    results = []
    for i in range(10):
        if i != 0 and x / i == y:
            results.append('/' + str(i))
        if x * i == y:
            results.append('*' + str(i))
        if x - i == y:
            results.append('-' + str(i))
        if x + i == y:
            results.append('+' + str(i))
    return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print("Please enter two numbers separated by a space, in the format of 'input output'")
        x, y = map(int, input().split())

        results = synthesis(x, y)
        for result in results:
            print(result)
            str_to_eval = str(x) + str(result)
            print("eval(" + str_to_eval + ")=" + str(eval(str_to_eval)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
