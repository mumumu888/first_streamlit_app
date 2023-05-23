import streamlit
import pandas
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

streamlit.header("フルーティバイス フルーツアドバイス!")
import requests
fruityvice_response =requests.get("https://fruityvice.com/api/fruit/watermelon") 
streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
