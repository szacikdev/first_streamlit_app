import streamlit, pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('New Healthy Dinner')

streamlit.header('Breakfast menu')
streamlit.text('🥣 Blueberry oatmeal')
streamlit.text('🥗 Strawberry smoothie')
streamlit.text('🐔 Hard-boiled eggs')
streamlit.text('🥑🍞 Avocado toast')   


streamlit.title('Build your own smoothie')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit),['Avocado', 'Strawberries'])
--fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.


streamlit.dataframe(my_fruit_list)
