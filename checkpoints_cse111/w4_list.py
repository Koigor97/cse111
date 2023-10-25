"""
Demonstrate that numbers are passed to a function by value
and lists are passed to a function by reference.
"""


def main():
    print("main()")
    x = 10
    lx = [2, 4, 6, 10, 12]
    print(f"    Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"    After calling modify_args():  x {x}  lx {lx}")


def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("    modify_args(n, alist)")
    print(f"        Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n *= 3
    the_index = len(alist)
    alist.remove(the_index - 3)

    print(f"        After changing n and alist:  n {n}  alist {alist}")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
