# Day 10 - Calculator 🧮

This project is a basic calculator that allows users to perform continuous mathematical operations. Users can choose to continue calculating with the previous result or start fresh. 

## Features

- Addition, subtraction, multiplication, and division
- Uses functions and dictionaries for operation logic
- Continuation of calculations using previous results
- ASCII art logo (from `art.py`)

## How It Works

- User is asked to enter the first number.
- User selects a mathematical operator (`+`, `-`, `*`, `/`).
- User enters the second number.
- The result is displayed.
- User chooses whether to continue with the result or start a new calculation.

## Example Output
```
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

Enter the first number: 13
+
-
*
/
Pick an operation: *
Enter the next number: 24
13.0 * 24.0 = 312.0
Type 'y' to continue calculating with 312.0, or type 'n' to start a new calculation:
```

## Skills Learned

- Writing functions that return values
- Returning multiple values
- Storing functions in dictionaries
- Using loops and control flow to manage program logic
- Using docstrings
- Implementing simple UI logic with ASCII art
- Different Syntax ways for Boolean logic: `again = yes_no == "y"`
