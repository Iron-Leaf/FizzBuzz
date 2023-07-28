# what Ints to increment over
startingInt = -10
intToCountTo = 100


# Container of FizzBuzz info IE: Triggering Modulo & Text to Print
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


# Simple Quick sort so the Fizzbuzzers print in numerical order
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# The fizzbuzzers
elements = [
    fizzBuzzer(3, "Fizz"),
    fizzBuzzer(5, "Buzz"),
    fizzBuzzer(2, "Foo"),
    fizzBuzzer(10, "Bar"),
]

# Sort
elements = quick_sort(elements)

# START
print("Friendly Game of FizzBuzz")

# increment from "startingInt" int to end @ "intToCountTo"
for num in range(startingInt, intToCountTo + 1):
    # Starting line so that you can see what number is being used
    print(str(num), end=":\t")

    # boolean store to determine if the num needs to be printed or not if a FizzBuzzer ran
    dontPrintInt = False
    for buzzer in elements:
        # if anything Fizzbuzzes the dontPrintInt is set to true
        if buzzer.fizzChecker(num):
            dontPrintInt = True
    # if nothing fizzbuzzed then prints the int
    if not dontPrintInt:
        print(str(num), end="")
        # New Line
    print()
