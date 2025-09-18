## Python 


# Data Types
python provides built in data types are : integers(int), floats, strings(str), booleans(bool)

    x = "Hello World" # string
    x = 50            # integer
    x = 60.5          # float
    x = ["hello", "for", "hello"]   # list : change, x.append("again")  # Adds an item to the list
    x = ("hello", "for", "hello")   # tuple :cannot change, print(x[1])  # Accessing item by index
    x = {"hello", "for", "hello"}   # set:Unordered, x.add("again")  # Adds item, removes duplicates
    x = {"name": "Suraj", "age": 24}  # dict
    x = True     # bool


# Variables
# Rules for Naming Variables:
    Must start with a letter (a-z, A-Z) or an underscore (_).​
    Case-sensitive (name, Name, and NAME are different variables).


# Python/String Operators
    1. Arithmetic Operators: +, -, *, /, //, %, **​
    2. len : to calculate length of a string
    3. Indexing : to print the letter of a string
    4. Slicing: syntax is [start:end:step] : to print the given order output
    5. concatenation with '+' : to add the two strings
    6. Repetition with '*': to print the string N number of times
    7. Using string methonds: to print the string all letters to Uppercase. syntax is print(variable.upper())
    8. Lowercase : print(variable.lower())
    9. Replace : print(variable.replace(_old:'l', _new:'x'))
    10. Calculation string manipulation

<!-- (16/09/2025) -->
## Operators 
    1. Modulo operator(%) : It gives the remainder value as output syntax is (divident % devisor) ; print(4 % 2)
    2. Floor Division (//) : It divides two numbers and gives you the quotient and the remainder is ignored. print(52 // 7) 
    3. Exponentation operation(**) : syntax is: print(2 ** 3) : two to the power of 3
    4. chr function : Convert the numeric value into a character syntax is chr(value + 65) 
        Note: 65 is ASCII for 'A'

## Python follows : PEMDAS
    How python calculate the calculation or the order on based of priority:
        - Parenthesis()
        - Exponentiation **
        - Multiplication *, Division /, Integer Division //, Modulo %
        - Addition +, Subtraction -

## Difference between // and %
    - // → Floor Division
            It divides two numbers and gives you the quotient and the remainder is ignored.
            Example:
                52 // 7   # = 7

    - % → Modulus Operator
            It divides two numbers and gives you the remainder (what is left over after division).
            Example:
                52 % 7   # = 3

## PEP 8
    - Is a style guide for python code.
    - It provides guidelines for writing consistent & readable code.

## Import Module 
    Perform example relevent to import modules

## Input function : input()
    - Converting Input to Integers


<!-- (17/09/2025) -->
## Operators
    1. Comparison operators
        - Equal to (==)
        - Not equal to (!=)
        - Greater than (>)
        - Less than (<)
        - Greater than or equal to (>=)
        - Less than or equal to (<=)
    2. Logical operators
        - and : Return True if both operands are True
        - or : Return True if atleast one operand is True
        - not : Return the opposite boolean value

## Python Function
    1. Built-in-function:
        - Type conversion : str(), int(), float()
        - Numeric operations: round(), sum(), min(), max()
        - Object information: type(), len()
    2. Created-function: the function that user needs to create is start with def keyword,
        - Syntax is : def function_name():


# Note :
    - Install matplotlib : Its used to visualize data/output in a graphical representation, pip install matplotlib
    - Import math module : Import the math module for advanced mathematical calculation

<!-- (18/09/2025) -->

# List
    - Examples:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(numbers[2:6])  # Output: [3, 4, 5, 6]

        vegetables = ['carrot', 'potato']
        fruits = ['apple', 'orange']
        combined = vegetables + fruits
        print(combined)   # Output: ['carrot', 'potato', 'apple', 'orange']

        fruits.append('banana')  # Adding new list
        print(fruits)  # Output: ['apple', 'orange', 'banana']

    - Nesting List:
        # List of Students
        students = [
            ['John', [85, 75, 98]],
            ['Joy' , [43, 65, 87]],
            ['Jay', [65. 89, 41]]
        ]

# Dictionaries 
    - Written in key-value pair.
    - Examples:
        person = {"name": "Suraj", "age": 24}
        print(person["name"])  # Output: Suraj

        person["email"] = "john@gmail.com"   # Adding new key-value pair
        person["age"] = 33  # Modify the existing value

# Tuples : 
    - Tuple is immutable, means once created it cannot be change or modify.
    - Examples:
        person = ("John", 25, "NY")
        print(person[0])  
    
    - Tuple is used for packing & unpacking
        cordinates = (10, 20, 30)
        x, y, z = cordinates
        print(x)  # Output: 10

# set:
    - Unordered, unique elements only.
    - Examples:
        my_set = {1, 2, 2, 3}
        print(my_set)  # Output: {1, 2, 3}

# type() function
    To check or display the type of values i.e., string,float,etc that we are passing.

# if-else, for loop, while loop

