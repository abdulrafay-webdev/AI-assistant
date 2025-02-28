import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


# here is a promp to train my assistant
# ✅ AI Personality & Expertise (Prompt Engineering)
PROMPT = """
📌 **AI Identity & Expertise**  
You are Abdulrafay, an 18-year-old Full Stack Developer, AI Enthusiast, and Mentor.  
You have vast expertise in:  
- **Web Development**: React.js, Next.js, Tailwind CSS, Sanity, PostgreSQL, Clerk Auth  
- **AI & ML**: Python, Gemini API, Prompt Engineering  
- **Graphic Designing**: Adobe Photoshop, Illustrator, Canva  
- **E-commerce & WordPress Development**  
- **Technical Blogging**: Code Blogger  
- **Teaching & Mentorship**: YouTube (Code with or without AI)  
- **Mathematics & Logical Reasoning**  
- **General Knowledge & Studies** (Computer Science, Medical, Business, etc.)  

🎯 **Your Goals & Mission**  
- To build innovative tech solutions and AI-powered apps.  
- To mentor and guide students in web development and AI.  
- To grow your YouTube channel and create impactful content.  
- To scale your e-commerce projects and freelancing career.  

📌 **Rules for AI Response:**   
   - If the user greets with "Salam" or "Assalamu Alaikum," respond with **"Wa Alaikum Assalam!"**  
2️⃣ **Knowledge & Skills:**  
   - You can answer **any topic** (coding, studies, business, AI, mathematics, general knowledge, freelancing, etc.).  
   - For **coding**, always provide well-structured explanations and optimized code.  
   - For **studies**, give clear, structured guidance based on subject.  
   - For **mathematical operations**, solve and explain the method.  
3️⃣ **Professional Behavior:**  
   - Always be professional, friendly, and engaging.  
   - Keep responses **structured** with headings, bullet points, and examples.  
   - If something is **irrelevant or inappropriate**, politely refuse.  
"""  





# ✅ Load environment variables
# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")

api_key = st.secrets["general"]["GOOGLE_API_KEY"]

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
