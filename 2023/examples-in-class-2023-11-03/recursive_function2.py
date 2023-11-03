def recursive_function_name(x):
    x = x - 1
    print(x)
    if x > 0:
        recursive_function_name(x)

recursive_function_name(10)