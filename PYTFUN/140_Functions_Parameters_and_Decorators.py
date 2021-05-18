# Write a function which takes any number of parameters and returns their average.
def get_avg(*args):
    return (sum(args) * 1.0) / len(args)


result = get_avg(12, 5, 19, 2, 44)
# result = get_avg(7, 200, 3081, 43, 10, 65, 46, 4865, 35, -12, 5.6, -79.935, 60)
print(result)

# not finished:
# import datetime
#
#
# def profile(f):
#     is_evaluating = False
#     def g(x):
#         nonlocal is_evaluating
#         if is_evaluating:
#             return f(x)
#         else:
#             start = datetime.datetime.now()
#             is_evaluating = True
#             value = f(x)
#             is_evaluating = False
#             end = datetime.datetime.now()
#             print(f"Start: {start}\nEnd: {end}\n")
#             return value
#     return g
#
#
# def log(original_function):
#     def new_function(*args):
#         start = datetime.datetime.now()
#         res = original_function(*args)
#         end = datetime.datetime.now()
#
#         print(f"Start: {start}\nEnd: {end}\n")
#         return res
#
#     # with open('./data/LucasLog.txt', mode='a') as logfile:
#     #     logfile.write(f"Start: {start}\nEnd: {end}\n")
#     return new_function
#
#
# def calculate(n: int) -> int:
#     if (n == 0):
#         return 2
#     elif (n == 1):
#         return 1
#     else:
#         a = get_nth_lucas_number(n - 1)
#         b = get_nth_lucas_number(n - 2)
#         return a + b
#
#
# @log
# def get_nth_lucas_number(n):
#     return calculate(n)
#
#
# print(get_nth_lucas_number(35))
#
