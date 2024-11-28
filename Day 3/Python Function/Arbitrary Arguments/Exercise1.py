def arbitrary_positional_arguments(*args):
    for value in args:
        print(value)

arbitrary_positional_arguments(2, 5, 8, 9)