import art
import functions

should_continue = False
stored_result = 0.0
while True:
    if should_continue:
        n1 = stored_result
        stored_result, should_continue = functions.calculate(n1)
    else:
        print(art.logo)
        n1 = float(input("Enter the first number: "))
        stored_result, should_continue = functions.calculate(n1)
