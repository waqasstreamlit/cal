import streamlit as st

# Title of the app
st.title('Simple Calculator using Python By Waqas Farooq')

# Input fields for numbers
num1 = st.number_input('Enter the first number value here', value=0.0)
num2 = st.number_input('Enter the second number value here', value=0.0)

# Drop-down menu for operation selection
operation = st.selectbox('Choose an operation to calculate', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

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
