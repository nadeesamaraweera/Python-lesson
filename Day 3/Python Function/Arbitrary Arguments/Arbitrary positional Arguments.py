def arbitrary_positional_arguments(*args):
    print(args,type(args))

arbitrary_positional_arguments(2,5,8,9)
# (2, 5, 8, 9) <class 'tuple'>