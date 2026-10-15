'''
Evaluate and print the result of the following expression:
x = 10 + 3 * 2 ** 2

Based on what you learnt in the lecture explain why the output is what it is.
'''

x = 10 + 3 * 2 ** 2

print(f"The value of x = {x}")

"""
The answer for the expression
-> x = 10 + 3 * 2 ** 2
is 22 because first we'll evaluate the exponent giving us
-> x = 10 + 3 * 4
next multiplication will be perfomed, so the expression will become
-> x = 10 + 12
and finally addition will give us
-> x = 22
"""