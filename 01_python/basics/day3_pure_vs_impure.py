# Pure function
def multiply(x, y):
    return x * y


# Impure function
count = 0

def increase_count():
    global count
    count += 1
    return count


print(multiply(2, 3))
print(increase_count())
print(increase_count())