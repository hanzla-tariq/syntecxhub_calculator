# sum function
def add (sum_num1, sum_num2):
    res = sum_num1 + sum_num2
    return res
# substraction function
def sub (sub_num1, sub_num2):
    res = sub_num1 - sub_num2
    return res
# multiplication function
def mul (num1, num2):
    res = num1 * num2
    return res
# division function
def div (num1 , num2):
    res = num1 / num2
    return res
# power function
def power (num1, num2):
    res = num1 ** num2
    return res
# main function
def main() :
    oper1 = float(input("Enter first number: "))
    cont = True
    while cont:
        op = input("Enter operator(+, -, *, /, ^):")
        # validating operator
        if op not in ["+", "-", "*"," /", "^"]:
            print("Error: Enter valid operator(+, -, *, /, ^)")
            continue
        oper2 = float(input("Enter second number: "))
        # applying operations
        if op == "+" :
           Result = add(oper1, oper2)
           print("Result:", Result )
        elif op == "-" :
           Result = sub(oper1, oper2)
           print("Result: ", Result)
        elif op == "*" :
           Result = mul(oper1, oper2)
           print("Result:", Result)
        elif op == "/" :
            # handling divided by zero
            if oper2 == 0:
               print("Error: Cannot divide by zero:")
               continue
            Result = div(oper1, oper2)
            print("Result:", Result)
        elif op == "^":
            Result = power(oper1, oper2)
            print("Result:", Result)
        # checking if user wants to continue
        while True:
            res = input("Do you want to continue(y,n) or clear(c): ").lower()
            if res == "y":
                oper1 = Result
                break
            # handling clear operation
            elif res == "c":
                Result = 0
                print("Result cleared successfully")
                oper1 = float(input("Enter first number: "))
                break
            elif res == "n":
                print("Final results:", Result)
                cont = False
                break
            else:
                print("Enter valid character (y,n,c)")
if __name__ == "__main__":
   main()