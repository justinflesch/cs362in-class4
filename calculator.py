# Calculator program

class calc:
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def multi(self, num1, num2):
        return num1 * num2

    def divi(self, num, denom):
        if denom == 0:
            print("Cannot divide by 0")
        else:
            return num / denom

    def __init__(self):
        result = 0
        val = input("Choose an operation, type it's value and hit enter: \na) Addition\nb) Subtraction\nc) Multiplication\nd) Division\n")
        if val == "a":
            num1 = float(input("Enter first addititive: "))
            num2 = float(input("Enter second addititive: "))
            result = self.add(num1, num2)
        elif val == "b":
            num1 = float(input("Enter number to be subtracted from: "))
            num2 = float(input("Enter subtractor: "))
            result = sub(num1, num2)
        elif val == "c":
            num1 = float(input("Enter first multiplayer: "))
            num2 = float(input("Enter second multiplayer: "))
            result = multi(num1, num2)
        elif val == "d":
            numerator = float(input("Enter numerator: "))
            denominator = float(input("Enter denominator: "))
            result = divi(numerator, denominator)
        else:
            print("That is not a currently supported option!")
        print(result)

if __name__ == "__main__":
    calculator = calc()