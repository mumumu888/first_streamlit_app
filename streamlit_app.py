import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Parents New Healthy Diner')
streamlit.header('朝食メニュー')
streamlit.text('🥣 オメガ 3 とブルーベリー オートミール')
streamlit.text('🥗 ケール、ほうれん草、ロケットスムージー')
streamlit.text('🐔 平飼い卵の固ゆで')
streamlit.text('🥑🍞 アボカドトースト')
streamlit.header('🍌🥭 自分でフルーツスムージーを作ろう 🥝🍇')

# ここに選択リストを置き、含めたい果物を選択できるようにしましょう。
fruits_selected = streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) 
Fruits_to_show = my_fruit_list.loc[fruits_selected]

# ページにテーブルを表示します。
streamlit.dataframe(Fruits_to_show)

#create the repeatable code block(called a function)
def get_fruitvice_data(this_fruit_choice):
  #import requests
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice) 
  # write your own comment -what does the next line do? 
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
 
streamlit.header("フルーティバイス フルーツアドバイス!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
        back_from_function = get_fruitvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)

except URLError as e:
streamlit.error()
  
#don't run anything past here while we troubleshoot
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows= my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ',add_my_fruit )

my_cur.execute("insert into fruit_load_list values('from streamlit')")
