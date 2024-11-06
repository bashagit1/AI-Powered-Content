import streamlit as st
import os
from openai import OpenAI

# Initialize OpenAI API with API Key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set Streamlit page title and emoji favicon
st.set_page_config(page_title="🌟 Content Creator AI", page_icon="✨")

# Sidebar Styling
with st.sidebar:
    st.markdown("<h2 style='color: #FFA07A;'>🌈 Choose Your Options</h2>", unsafe_allow_html=True)
    st.markdown("Customize your content generation with the options below!")

    # Select Content Type
    content_type = st.selectbox("📝 Content Type", ["Blog Post", "Article", "Product Description", "Social Media Post"])

    # Select Tone
    tone = st.selectbox("🎨 Tone", ["Professional", "Casual", "Playful", "Inspirational", "Witty"])

    # Target Audience Input
    target_audience = st.text_input("👥 Target Audience", placeholder="e.g., Digital Marketers")

# Main Content Area
st.markdown("<h1 style='text-align: center; color: #FF6347;'>✨ AI-Powered Content Generator ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B0082;'>Generate engaging content effortlessly!</p>", unsafe_allow_html=True)

# User Input for Topic
st.markdown("#### 💬 Enter Topic for Content:")
topic = st.text_input("Type your topic here:", placeholder="e.g., Benefits of Remote Work")

# Function to Generate Content
def generate_content(content_type, topic, tone, target_audience):
    prompt = f"Generate a {tone.lower()} {content_type.lower()} about {topic} for {target_audience}."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for generating content."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Generate Button and Display Response
if st.button("✨ Generate Content"):
    if topic and target_audience:
        response = generate_content(content_type, topic, tone, target_audience)
        st.markdown("### 📝 Generated Content:")
        st.write(response)

        # Download button for content
        st.download_button("💾 Download Content", data=response, file_name="generated_content.txt")
    else:
        st.warning("Please provide both a topic and target audience.")

# User Guide for Easy Navigation
st.info("""
### 🛠️ How to Use:
1. Enter a topic for the content.
2. Choose the content type, tone, and audience from the sidebar.
3. Click 'Generate Content' to receive your custom content!
""")
