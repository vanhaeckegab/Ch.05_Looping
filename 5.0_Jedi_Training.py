  #Sign your name:Gabe Van Haecke

'''
 1. Make the following program work.
   '''  
# print("This program takes three numbers and returns the sum.")
# total = 0
#
# for i in range(3):
#     x = float(input("Enter a number: "))
#     total += x
# print("The total is:", total)
#
#

'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
#
# for i in range(2,101,2):
#     print(i)
#

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
# i = 10
# while i >= 0:
#     print(i)
#     i -= 1
# print("Blast off!")

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
# import random
# print(random.randint(1, 10))
#


'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
# total = 0
# e = 0
# n = 0
# z = 0
# for i in range(7):
#     num = float(input("Pick a number "))
#     total += num
#     if num > 0:
#         e += 1
#     elif num < 0:
#         n += 1
#     else:
#         z += 1
# print("The total sum is", total, ", there were", e, "positive numbers,", n, "negative numbers, and", z,
#       "of the numbers were zero.")
