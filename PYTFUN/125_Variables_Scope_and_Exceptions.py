a, b, c = 1, 2, 3 # Three global variables

def f(x):
    d = 4 # Brand new local!
    a = 5 # Local to f, shadows global f

    def g():
        x = 1 # Local to g, shadows f's x
        nonlocal a # allows access to f's a
        a = 6 # updates the nonlocal
        global c
        c = 7


    g()
    assert x == 1 # g's x did not overwrite f's x
    assert a == 6 # assert that it changed
    assert b == 2 # globals are visible

f(10)
assert a == 1 and b == 2 and c == 7

# try:
#     print(x)
# except NameError as e:
#     print('NameError raised as expected')

# MAXIMUM_MARK = 80
# tom_mark = 58
# print(("Tom's mark is %.2f%%" % (tom_mark / MAXIMUM_MARK * 100)))


# error handling for non-existing path
# error handling for 'ABCDE' value instead of temp
# -?([0-9]+(\.[0-9][0-9]?)?)C

