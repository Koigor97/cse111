
def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

# my_list = make_list(101)
# print(my_list)

# generators are iterables.
def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(100)
next(g)
next(g)
print(next(g))

for i in generator_function(50):
    print(i)


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0, 100)
for i in gen:
    print(i)