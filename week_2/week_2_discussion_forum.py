# Example 1: Define a function that takes an argument. 
# Call the function. Identify what code is the argument 
# and what code is the parameter.

def add_excitement(phrase):
    print(phrase + '!')

add_excitement('Hello')
# Hello!

# phrase is the parameter of the add_excitement function 
# and 'Hello' is the argument.

# Example 2: Call your function from Example 1 three times 
# with different kinds of arguments: a value, a variable, 
# and an expression. Identify which kind of argument is 
# which. 

# Calling my function with a value
add_excitement('Hello World')
# Hello World!

# Calling my function with a variable
introduction = 'Hello, my name is Ryan'
add_excitement(introduction)
# Hello, my name is Ryan!

# Calling my function with an expression
add_excitement(introduction + " and I'm happy to be here")
# Hello, my name is Ryan and I'm happy to be here!

# Example 3: Construct a function with a local variable. 
# Show what happens when you try to use that variable 
# outside the function. Explain the results.

def get_yearly_housing_cost(monthly_rent):
    utilities = 100
    yearly_total = (monthly_rent + utilities) * 12
    print('Total rent is: $' + str(yearly_total))

print(utilities)
# Traceback (most recent call last):
#   File "/Users/ryanmccall/codeup/data_science/personal/uopeople/intro_to_python/week_2/week_2_discussion_forum.py", line 41, in <module>
#     print(utilities)
# NameError: name 'utilities' is not defined

# Trying to print the variable utilities outside of the 
# function causes a name error because variables created 
# inside functions are local to the function and cannot 
# be referenced outside the function.

# Example 4: Construct a function that takes an argument. 
# Give the function parameter a unique name. Show what 
# happens when you try to use that parameter name outside 
# the function. Explain the results.

def get_ice_cream(flavor):
    print('Here is a scoop of', flavor)

print(flavor)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'flavor' is not defined

# Trying to call the parameter name outside of the 
# function causes a name error because the parameter 
# name is only able to be referenced inside the function.

# Example 5: Show what happens when a variable defined 
# outside a function has the same name as a local 
# variable inside a function. Explain what happens to the 
# value of each variable as the program runs.

def get_dog_years(your_age):
    age = your_age * 7
    print('You are', age, 'in dog years.')

age = 29
get_dog_years(age)
print(age)
# You are 203 in dog years
# 29

# There is both a local and global variable with the same 
# name, age. Outside the funciton, the global variable 
# age holds the integer 29. Inside the function, the 
# local variable age holds the result of the expression 
# your_age * 7 which, in this case, is the integer 203.