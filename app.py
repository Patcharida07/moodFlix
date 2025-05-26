import streamlit as st
import datetime
from textblob import TextBlob

# ページ設定
st.set_page_config(page_title="Mood Movie", layout="wide")

# タイトルと説明
st.title("🎬 Mood Movie")
st.subheader("気分にぴったりな映画を、AIが選んでくれるよ")
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0)),
                        url("https://images.unsplash.com/photo-1626814026160-2237a95fc5a0?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

# 感情分析関数（TextBlob使用）
def detect_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "嬉しい🙂"
    elif polarity < -0.2:
        return "悲しい😢"
    else:
        return "驚き😲"

# 推薦ロジック（簡易）
def recommend_movie(mood, user_text):
    if "涙" in user_text or "泣きたい" in user_text:
        mood = "悲しい😢"
    elif "怒り" in user_text or "イライラ" in user_text:
        mood = "怒り😠"
    elif "嬉しい" in user_text or "幸せ" in user_text:
        mood = "嬉しい🙂"

    if mood == "悲しい😢":
        return [
            {"title": "火垂るの墓", "comment": "美しくて感動的な物語。泣きたい時にぴったり。"},
            {"title": "余命1ヶ月の花嫁", "comment": "切ないラブストーリーが心に沁みる。"},
            {"title": "世界の中心で、愛をさけぶ", "comment": "涙が止まらない青春ドラマ。"},
            {"title": "聲の形", "comment": "心に響く青春ドラマ。"},
            {"title": "そして父になる", "comment": "親子の絆に心打たれる感動作。"}
        ]

    elif mood == "怒り😠":
        return [
            {"title": "怒り", "comment": "重く鋭い人間ドラマ。"},
            {"title": "告白", "comment": "衝撃の展開が続くサスペンス。"},
            {"title": "ミュージアム", "comment": "連続殺人犯を追う衝撃スリラー。"},
            {"title": "孤狼の血", "comment": "暴力と正義が交錯する刑事ドラマ。"},
            {"title": "新聞記者", "comment": "社会派サスペンスの秀作。"}
        ]

    elif mood == "嬉しい🙂":
        return [
            {"title": "しあわせのパン", "comment": "北海道の自然と心温まる物語。"},
            {"title": "歩いても 歩いても", "comment": "家族のぬくもりを感じる日常劇。"},
            {"title": "夏目友人帳", "comment": "心優しい妖と人の交流。"},
            {"title": "猫の恩返し", "comment": "楽しい冒険と癒しが詰まった作品。"},
            {"title": "リトル・フォレスト", "comment": "自然と共に暮らす喜び。"}
        ]

    elif mood == "驚き😲":
        return [
            {"title": "パプリカ", "comment": "夢と現実が交錯する脳内トリップ。"},
            {"title": "イニシエーション・ラブ", "comment": "どんでん返しがすごい恋愛ミステリー。"},
            {"title": "カメラを止めるな！", "comment": "驚きと笑いが止まらない低予算神作。"},
            {"title": "MONSTER", "comment": "心理サスペンスの金字塔。"},
            {"title": "嫌われ松子の一生", "comment": "波乱万丈の人生を鮮やかに描く。"}
        ]

    elif mood == "怖い😨":
        return [
            {"title": "リング", "comment": "日本ホラーの金字塔。"},
            {"title": "呪怨", "comment": "背筋が凍る恐怖体験。"},
            {"title": "残穢【ざんえ】", "comment": "静かな恐怖がじわじわと。"},
            {"title": "仄暗い水の底から", "comment": "不気味さと哀しさの入り混じる一作。"},
            {"title": "屍人荘の殺人", "comment": "ホラー×推理の新感覚ミステリー。"}
        ]

    else:
        return [{"title": "インサイド・ヘッド", "comment": "感情の旅に出かけよう。"}]

# サイドバーで入力
with st.sidebar:
    st.header("🎭 気分を入力しよう")

    # テキスト入力
    user_text = st.text_area("📝 今の気持ちを自由に書いてね", placeholder="例：今日は落ち込んでる…")

    # プリセット気分選択
    mood_radio = st.radio("😊 今の気分を選んでください", ["悲しい😢", "怒り😠", "嬉しい🙂", "驚き😲", "怖い😨"])

    # ボタン押下
    submit = st.button("🎥 映画を提案して！")

# 結果表示
if submit:
    if user_text.strip():
        detected_mood = detect_sentiment(user_text)
        st.write(f"🧠 AIが感情を分析した結果: **{detected_mood}**")
        final_mood = detected_mood
    else:
        final_mood = mood_radio

    st.header(f"🎬 あなたの気分: 「{final_mood}」")
    recommendations = recommend_movie(final_mood, user_text)

    for rec in recommendations:
        st.subheader(f"✅ {rec['title']}")
        st.caption(rec['comment'])

    # 履歴の保存
    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append({
        "date": datetime.datetime.now(),
        "mood": final_mood,
        "movies": [rec["title"] for rec in recommendations]
    })

# 履歴表示
with st.expander("📚 過去のおすすめを見る"):
    if "history" in st.session_state and st.session_state.history:
        for item in reversed(st.session_state.history):
            st.markdown(f"- **{item['date'].strftime('%Y-%m-%d %H:%M')}** | 気分: *{item['mood']}* → {', '.join(item['movies'])}")
    else:
        st.write("まだ履歴がありません。")
