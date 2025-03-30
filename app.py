from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import os

load_dotenv()

st.title("【提出課題】LLM機能を搭載したWebアプリを開発しよう")

st.subheader("あなたの専門家に相談してみましょう！")
st.write("以下から専門家を選択し、質問を入力てください。")
selected_item = st.radio("専門家を選択してください。", ["AIエンジニア", "健康アドバイザー", "旅行アドバイザー"])

input_message = st.text_input(label="専門家に何でも聞いてください")

if st.button("実行"):
  client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

  first_completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "system", "content": f"あなたは{selected_item}です。安全なアドバイスを提供してください。専門以外の質問には答えないでください。"},
          {"role": "user", "content": input_message}
      ],
      temperature=0.5
  )
  st.subheader(f"専門家「{selected_item}」からの回答")
  st.write(first_completion.choices[0].message.content)