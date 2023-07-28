intToCountTo = 100
startingInt = -10

class fizzBuzzer:
    def __init__(self, modulo, text):
        self.Modulo = modulo
        self.Text = text

    def __lt__(self, other):
        return self.Modulo < other.Modulo

    def fizzChecker(self, input):
        if input % self.Modulo == 0:
            print(self.Text, end="")
            return True


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

elements = [
    fizzBuzzer(3, "Fizz"),
    fizzBuzzer(5, "Buzz"),
    fizzBuzzer(2, "Foo"),
    fizzBuzzer(10, "Bar"),
]

elements = quick_sort(elements)

print("Friendly Game of FizzBuzz")

for num in range(startingInt, intToCountTo + 1):
    print(str(num), end=":\t")
    dontPrintInt = False
    for buzzer in elements:
        if buzzer.fizzChecker(num):
            dontPrintInt = True
    if not dontPrintInt:
        print(str(num), end="")
    print()
