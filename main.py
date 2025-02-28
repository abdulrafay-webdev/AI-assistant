import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


# here is a promp to train my assistant
# ✅ AI Personality & Expertise (Prompt Engineering)
PROMPT = """
You are Abdulrafay, an 18-year-old Full Stack Developer and AI Enthusiast.  
You have expertise in:
- **Web Development** (React.js, Next.js, Tailwind CSS, Sanity, PostgreSQL, Clerk Auth)
- **AI & ML** (Python, Gemini API, Prompt Engineering)
- **Graphic Designing** (Adobe Photoshop, Illustrator, Canva)
- **E-commerce & WordPress Development**
- **Technical Blogging** (Code Blogger)
- **Teaching & Mentorship** (YouTube: Code with or without AI)

📌 **Rules for AI Response:**
- Always reply as if you are Abdulrafay.
- If the user asks about **studies** (Computer Science, Medical, Business, etc.), provide structured guidance.
- If the question is about **coding**, give optimized solutions with explanations.
- If the topic is irrelevant, politely refuse.
"""




# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("🚨 API key not found! Please check your .env file.")
    st.stop()
else:
    genai.configure(api_key=api_key)

# ✅ Initialize AI Model
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ AI Avatar Image Path
AI_AVATAR = "images/ai_avatar.jpeg"  # Local Image
# AI_AVATAR = "https://your-image-url.com/avatar.jpg"  # Online Image

# ✅ Streamlit UI
st.set_page_config(page_title="AI Assistant", page_icon="🤖")


# ✅ UI: Title with Image
col1, col2 = st.columns([1, 5])  # 👈 1: Image, 5: Title (Adjust width)
with col1:
    st.image(AI_AVATAR, width=100)  # 👈 Image ka size set karein
with col2:
    st.title("I am Abdul Rafay, Your Tech Partner")

# ✅ Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Display Previous Messages with Avatar
for chat in st.session_state.messages:
    avatar_img = AI_AVATAR if chat["role"] == "ai" else None  # AI ka custom avatar set karein
    with st.chat_message(chat["role"], avatar=avatar_img):
        st.markdown(chat["content"])

# ✅ User Input
user_input = st.chat_input("Type your message...")

if user_input:
    # ✅ Show User Message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # ✅ AI Response with Custom Avatar
    with st.chat_message("ai", avatar=AI_AVATAR):  # AI Avatar Set
        response = model.generate_content(f"{PROMPT}\n\nUser: {user_input}")
        ai_response = response.text
        st.markdown(ai_response)

    # ✅ Save AI Response in Session State
    st.session_state.messages.append({"role": "ai", "content": ai_response})
