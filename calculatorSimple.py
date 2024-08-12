import streamlit as st

# Title of the app
st.title('Simple Calculator using Python By Waqas Farooq')
st.title('It includes addition, multiplication, subtraction, comparison')

# Input fields for numbers
num1 = st.number_input('Enter the first number value here', value=0.0)
num2 = st.number_input('Enter the second number value here', value=0.0)

# Drop-down menu for operation selection
operation = st.selectbox('Choose an operation to calculate', ['Addition', 'Subtraction', 'Multiplication', 'Division','Compare'])

# Calculate result based on selected operation
def calculate_result():
 result = None
 if operation == 'Addition':
    result = num1 + num2
 elif operation == 'Subtraction':
    result = num1 - num2
 elif operation == 'Multiplication':
    result = num1 * num2
 elif operation == 'Division':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Error: Division by zero'
 elif operation == 'Compare':
   if num1 > num2:
    result = 'Number 1 is greater then Number 2'
   elif num2 > num1:
    result = 'Number 2 is greater then Number 1'
   elif num2 == num1:
    result = 'Both numbers values are equal'
 return result

# Add a button
if st.button("Calculate"):
    # Call the calculate_result function when the button is clicked
    result = calculate_result()
    st.write(f"The result is: {result}")


#st.write("Result: ",result)
# Display the result
#if result is not None:
    
    #st.write(f'The result of {operation}ing {num1} and {num2} is: {result}')
