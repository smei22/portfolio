#function example template
# adds num1 and num2 and prints the results
def add(num1, num2):
        result = num1 + num2
        print("The result is: " + str(result))

# Simple Calculator
print("Welcome Preschoolers to Simple Calculator")
print("Enter an Operation: ")

              
def simpleCalculator():
        while True:
                print("""1. Addition
        2. Subtraction
        3. Division
        4. Multiplication
        5. Quit""")
                operation = int(input("(1-5) Operation: "))  #TRUE

                #operation = input("(1-5) Operation: ") # FALSE BECAUSE WE ARE INPUTTING INTEGER NOT STRING!! WE MUST PUT int() BEFORE INPUT TO TURN IT INTO AN INTEGER
                if operation == 1:  #TRUE BECAUSE 1 IS AN INTEGER
                        int1 = int(input("Enter your first number: "))
                        int2 = int(input("Enter your second number: "))
                        add(int1, int2)


                elif operation == 2:
                        int1 = int(input("Enter your first number: "))
                        int2 = int(input("Enter your second number: "))
                        add(int1, -int2)
                elif operation == 3:
                        int1 = int(input("Enter your first number: "))
                        int2 = int(input("Enter your second number: "))
                        quotient = int1 // int2
                        print("The result is: " + quotient)


                elif operation == 4:
                        int1 = int(input("Enter your first number: "))
                        int2 = int(input("Enter your second number: "))
                        product = int1 * int2
                        print("The result is: " + product)

                elif operation == 5:
                        break

simpleCalculator()
