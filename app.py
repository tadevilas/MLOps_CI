import streamlit  as st

# Streamlit UI

st.title('Powre Calculator')
st.write('Enter a number to calculate its Square, Cube, and Fifth Power')

# Get user input
n = st.number_input('Enter an Interger', value= 1, step= 1)

# Cal Results
square = n**2
cube = n**3
fifth_Power  = n**5

# Display Results
st.write(f'The Squre of the {n} is: {square}')
st.write(f'The Cube of the {n} is: {cube}')
st.write(f'The Fifth Power of the {n} is: {fifth_Power}')