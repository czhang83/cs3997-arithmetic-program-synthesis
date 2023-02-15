# finds an arithmetic expression by a bottom up approach that query over the positive integers with
# addition, multiplication, subtraction, and integer division.
# Supports input-output pairs such as 4 maps to 8, and synthesize the function +4 (as one example).
# this would generate new functions, use conditional inference to eliminate functional equivalent functions
# pick better functions among equivalence, repeat this up to MAX_FUNCTION_DEPTH to give a good function
# This will first print all valid functions this program found (for demonstration purpose)
# then print one function it picked through the equivalence comparison.

# length of longest possible function
MAX_FUNCTION_DEPTH = 4
# largest possible integer
MAX_BOUND = 10
OPERATORS = ['+', '-', '*', '/']
NUMBERS = []
for i in range(MAX_BOUND):
    NUMBERS.append(str(i))

valid_result = []


def evaluate_function(f):
    return eval(f)


# shorter function length is preferred
def get_better_function(func_1, func_2):
    if len(func_1) > len(func_2):
        return func_2
    return func_1


# given a list of functions, remove functional equivalent functions
# in the context of arithmetic, this means that the resulting values are the same
# when comparing equivalent functions, always remove the one with a lower score (shorter function length is preferred)
# if any function generate the targeted y, record it in the global list
def cond_inference(functions, y):
    value_to_function_map = {}
    for f in functions:
        value = evaluate_function(f)
        if value == y:
            valid_result.append(f)
        if value in value_to_function_map:
            value_to_function_map[value] = get_better_function(value_to_function_map[value], f)
        else:
            value_to_function_map[value] = f
    return list(value_to_function_map.values())


# add operations to the given function
# (4 + 5) -> ((4 + 5) + 1), ((4 + 5) + 2), etc.
def append_operator(function):
    results = []
    for n in NUMBERS:
        for operator in OPERATORS:
            # avoid division by 0
            # avoid +/- 0 since this does nothing
            if (operator == '/' or operator == '+' or operator == '-') and n == '0':
                continue
            # avoid non integer division round offs
            if operator == '/' and evaluate_function(function) % int(n) != 0:
                continue
            # WLOG, ignore order of operations
            result = '(' + function + operator + n + ')'
            results.append(result)
    return results


def synthesis(x, y):
    results = []
    results.append(str(x))

    counter = 0
    while counter < MAX_FUNCTION_DEPTH:
        # for every function currently have
        # appends all possible operations
        # then use conditional inference to reduce the number of functions
        new_results = results
        for r in results:
            new_results = new_results + append_operator(r)
        results = cond_inference(new_results, y)
        counter = counter + 1
        # print('result after cond inf')
        # print(results)

    good_result = ''
    for r in results:
        if eval(r) == y:
            good_result = r

    return good_result


if __name__ == '__main__':
    while True:
        valid_result = []
        print("Please enter two numbers separated by a space, in the format of 'input output'")
        x, y = map(int, input().split())

        result = synthesis(x, y)
        print('Printing possible expressions')
        for r in valid_result:
            print(r + "　=　" + str(eval(r)))

        print('Printing a good expression')
        print(result + "　=　" + str(eval(r)))

