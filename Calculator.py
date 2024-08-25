# Write the main 4 functions

def add(n1, n2):
  return n1 + n2 

def substract(n1, n2):
  return n1 - n2 

def multiply(n1, n2):
  return n1 * n2 

def devide(n1, n2): 
  return n1 / n2 

# Add these 4 fucntions in a dictionary as the values. Keys = "+", "-", "*", "/"  

operations = {
  "+": add,
  "-": substract, 
  "*": multiply,
  "/": devide 
}

# Function to operate the calculator
def calculator(): 

  should_accumulate = True
  num1 = float(input("What is the first number: ")) 

  while should_accumulate: 
    for symbol in operations:
      print(symbol)  # Print available operations (+, -, *, /)
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What is the second number: ")) 
    
    # Perform the operation based on user input using the operations dictionary
    answer = operations[operation_symbol](num1, num2) 

    print(f"{num1} {operation_symbol} {num2} = {answer}") 
    
    # Asking the user if they want to continue with the result or exit
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") 

    if choice == "y": 
      num1 = answer  # If 'y', update num1 with the current answer for further calculations
    else: 
      should_accumulate = False # If 'n', set should_accumulate to False to exit the loop
      print("\n" * 20) # Print 20 new lines to clear the screen for the next calculation
      
# Call the calculator function to start the program
calculator() 
  