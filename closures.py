# https://www.youtube.com/watch?v=swU3c34d2NQ
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Closures


def outer_func(msg):
    message = msg 

    def inner_func():
        """Note that this inner function oes not take in any arguments"""
        print(message)

    return inner_func


def main():
    hi_func = outer_func('hi')
    hello_func = outer_func('hello')
    print(hi_func.__name__)
    print(hello_func.__name__)

    # A closure is an inner function that remembers and has access to variables
    # in the local scope in which the variable was created, even after the outer
    # function has finished executing.

    # Each of these functions remembers the values of its own msg variable.
    # A closure closes over the free variables from its environment
    # (in this case, message).
    hi_func()
    hello_func()


if __name__ == "__main__":
    main()
