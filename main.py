def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment


c1 = counter()
c2 = counter()

print(c1())  # Output: 1
print(c1())  # Output: 2
print(c2())  # Output: 1
print(c2())  # Output: 2
print(c1())  # Output: 3

def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times2 = multiplier(2)
times3 = multiplier(3)

print(times2(5))  # Output: 10
print(times3(5))  # Output: 15
print(times2(10))  # Output: 20
print(times3(10))  # Output: 30
