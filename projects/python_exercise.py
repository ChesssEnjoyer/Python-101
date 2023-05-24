x = [1,2]
y=x
x[0] = 100

print(x,y)


def get_largest_numbers(numbers, n):
    numbers.sort()
    
    return numbers[-n:]

nums = [2,3,4,1,34,123,321,1]

print(nums)
largest = get_largest_numbers(nums, 2)
print(nums, "\n")


z = [i for i in range(10) if i % 2 == 0]
print(z, "\n")


def complicated_function(*args, **kwargs):
    print(args, kwargs['x'], "\n")
    pass

complicated_function(1, 2, 3, x = 1, s = "hello", b = True)


def complicated2_function(a, b, c = True, d = False):
    print(a, b, c, d)
    pass

complicated2_function(*[1,2],  **{"c": "hello", "d": "cool"})


def add(a,b):
    return a + b


if __name__  == "__main__":
    print("run")