import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('朝食メニュー')
streamlit.text('🥣 オメガ 3 とブルーベリー オートミール')
streamlit.text('🥗 ケール、ほうれん草、ロケットスムージー')
streamlit.text('🐔 平飼い卵の固ゆで')
streamlit.text('🥑🍞 アボカドトースト')
streamlit.header('🍌🥭 自分でフルーツスムージーを作ろう 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
