# def factorial_iterative(n):
#     """
#     :param n:
#     :return:
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac
# number =  int(input("Enter the number\n"))
# print("the factorial using iterative method is\n", factorial_iterative(number))

# def factorial_recursive(n):
#     """
#
#     :param n:
#     :return:
#     """
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 *3 * factorial_recursive(2)
# 5 * 4 * 3 *2 * factorial_recursive(1)
# 5 * 4 *3 * 2 * 1 == 120
# number = int(input("Enter the number\n"))
# print("factorial using recusive\n", factorial_recursive(number))

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number = int(input("Enter the number\n"))
print("factorial using fibonacci\n", fibonacci(number))