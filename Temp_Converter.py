
'''Overview
In this assignment, you will create a Python program that converts temperatures between Fahrenheit and Celsius. The program will prompt the user to enter a temperature in Fahrenheit and convert it to Celsius, or vice versa, depending on the user's choice. This assignment will help you practice using loops, if statements, and user input/output in Python.

Objectives
Use if statements to handle conditional logic.
Implement loops to allow multiple conversions without restarting the program.
Apply input and output operations to interact with the user.
Requirements
User Choice: The program should first ask the user whether they want to convert a temperature from Fahrenheit to Celsius or from Celsius to Fahrenheit. Use input to get the user's choice and use an if statement to determine which formula to use.  Allow for upper and lowercase characters.

Temperature Input: Prompt the user to input the temperature.

Conversion:

If converting from Fahrenheit to Celsius, use the formula: C = (F - 32) * 5/9.
If converting from Celsius to Fahrenheit, use the formula: F = C * 9/5 + 32.
Perform the conversion and display the result to the user.
Loop for Multiple Conversions: After displaying the conversion result, ask the user if they want to perform another conversion. The program should continue running until the user chooses to exit.  This will require a while loop.
'''


# Here I open with the loop to encase the entire program. I set the while loop to always be true so that it will continue the program until the user exits.
while  True:

# The user input that starts the conversion. By selecting F or C the if statement below will decide what forumala and output to use or if the input is invalid and respond with a message.
    unit = input("Enter the starting unit of measurement F for Fahrenheit or C for Celsius: ")

# The if statement for celsius.
    if unit == "C":
        C = int(input("Enter the temperature in Celsius: "))
        print("The temperature is: " + str(C * 9/5 + 32) + " degrees fahrenheit.")
# The elif statement continues the if statement but adds fahrenheit as an option.
    elif unit == "F":
        F = int(input("Enter the temperature in Fahrenheit: "))
        print("The temperature is: " + str((F - 32) * 5/9) + " degrees celsius.")
# The else response is here if an input does not match C or F. It will loop the use back to the start to get a correct input.
    else:
        print("SI Unit does not exist please enter C or F to begin conversion: ")




    
    
