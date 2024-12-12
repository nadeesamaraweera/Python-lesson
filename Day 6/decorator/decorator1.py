def make_pretty (func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def oridinary():
    print("Iam Oridinary")

# decorate_func = make_pretty(oridinary)

# def inner():
#     print("I got decorator")
#     oridinary()

# decorate_func()

oridinary()
