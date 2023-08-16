import streamlit, pandas

streamlit.title('New Healthy Dinner')

streamlit.header('Breakfast menu')
streamlit.text('🥣 Blueberry oatmeal')
streamlit.text('🥗 Strawberry smoothie')
streamlit.text('🐔 Hard-boiled eggs')
streamlit.text('🥑🍞 Avocado toast')   

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
