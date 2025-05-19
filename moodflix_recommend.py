import random

# 映画データ（タイトル, 感情, 簡単な紹介）
movies = [
    {"title": "聲の形／声之形", "emotion": "Sad", "desc": "关于校园霸凌与心理创伤的动人故事。"},
    {"title": "カメラを止めるな！／摄影机不要停！", "emotion": "Surprised", "desc": "拍摄过程中意外不断，笑中带泪。"},
    {"title": "呪怨／咒怨", "emotion": "Fearful", "desc": "日式恐怖代表作，令人背脊发凉。"},
    {"title": "リトル・フォレスト／小森林", "emotion": "Happy", "desc": "女主回到乡下，用料理面对四季人生。"},
    {"title": "怒り／愤怒", "emotion": "Angry", "desc": "三起谋杀案串起人与人之间的信任危机。"},
    {"title": "火垂るの墓／萤火虫之墓", "emotion": "Sad", "desc": "战争中的兄妹在绝望中努力求生。"},
    {"title": "猫の恩返し／猫的报恩", "emotion": "Happy", "desc": "女高中生进入猫的王国，展开奇幻冒险。"},
]

# 感情选项
emotions = ["Happy", "Sad", "Angry", "Surprised", "Fearful"]

# 用户输入
user_emotion = input("请选择你的情绪（Happy, Sad, Angry, Surprised, Fearful）：").strip().capitalize()

if user_emotion not in emotions:
    print("⚠️ 输入的情绪不在推荐列表中，请重新运行并输入正确的情绪。")
    exit()

# 推荐逻辑
def recommend_movies(emotion, num=3):
    filtered = [m for m in movies if m["emotion"].lower() == emotion.lower()]
    if not filtered:
        return ["没有找到对应情绪的电影。"]
    return random.sample(filtered, min(len(filtered), num))

# 调用推荐函数并显示结果
recommendations = recommend_movies(user_emotion)
print(f"\n基于您的 {user_emotion} 情绪，为您推荐以下电影：\n")
for movie in recommendations:
    print(f"🎬 {movie['title']}")
    print(f"   {movie['desc']}")
    print()