#Katherine O'Roark
#Problem 1
while True:
    print("this is the loop that never ends!")
#you can break out of this loop by using the ctrl+c command

#problem 2
i = 1
sum = 0
while i < 12:
    if i%2 == 0:
        sum += i
    i += 1
print("The sum of all even, positive numbers less than 12 is:", sum)

#problem 4
def fib(n):
    if  n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f = fib(n-1)+fib(n-2)
        return f

print(fib(4))
