import streamlit as st
from textblob import TextBlob
import random

movies_by_mood = {
    "positive": ["The Pursuit of Happyness", "Forrest Gump", "La La Land"],
    "negative": ["Joker", "Requiem for a Dream", "Grave of the Fireflies"],
    "neutral": ["Cast Away", "The Secret Life of Walter Mitty", "The Terminal"]
}
st.title("🎬 MoodFlix - 気分で選ぶ映画アプリ")

st.write("今の気分にぴったりの映画をおすすめします！")

user_input = st.text_input("วันนี้คุณรู้สึกยังไงบ้าง? (พิมพ์ความรู้สึกเช่น ดีใจ เหงา เบื่อ ฯลฯ)")
if user_input:
    # วิเคราะห์อารมณ์ด้วย TextBlob
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        mood = "positive"
    elif polarity < -0.1:
        mood = "negative"
    else:
        mood = "neutral"

    # เลือกหนังจากหมวดอารมณ์
    recommended = random.choice(movies_by_mood[mood])
    st.success(f"เราแนะนำให้คุณดูเรื่อง: {recommended} 🎬")