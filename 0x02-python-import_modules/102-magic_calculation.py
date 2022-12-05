#!/usr/bin/python3
<<<<<<< HEAD

def magic_calculation(a, b):
    """Match bytecode provided"""
    from magic_calculation_102 import add, sub

=======
def magic_calculation(a, b):
    """Match bytecode provided"""
    from magic_calculation_102 import add, sub
>>>>>>> df2a7187cb92e3a6671b863a637301a5b50ffc5a
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
<<<<<<< HEAD
        return (c)

    else:
        return (sub(a, b))
=======
            return (c)
        else:
            return (sub(a, b))
>>>>>>> df2a7187cb92e3a6671b863a637301a5b50ffc5a
