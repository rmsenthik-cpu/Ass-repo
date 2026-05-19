# =========================================================
# INTERNATIONAL BUSINESS MARKETING PROMPT APPLICATION
# =========================================================

import streamlit as st
from transformers import pipeline

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="International Business Marketing AI",
    page_icon="🌍",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

h1 {
    color: #00D4AA;
    text-align: center;
}

.stButton>button {
    background-color: #00D4AA;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

.stTextInput>div>div>input {
    background-color: #262730;
    color: white;
}

.output-box {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("🌍 International Business Marketing Prompt Application")

st.markdown("""
### Generate Professional Global Marketing Content using Generative AI

This AI application automatically creates:

✅ Global Product Titles  
✅ Powerful Marketing Slogans  
✅ International Advertising Descriptions  
✅ Expert-Level Branding Content  

""")

# =========================================================
# LOAD HUGGING FACE MODEL
# =========================================================

@st.cache_resource
def load_model():

    generator = pipeline(
        "text-generation",
        model="gpt2"
    )

    return generator

generator = load_model()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚙ Settings")

temperature = st.sidebar.slider(
    "Temperature",
    0.1,
    1.0,
    0.8
)

max_tokens = st.sidebar.slider(
    "Max New Tokens",
    100,
    500,
    300
)

# =========================================================
# USER INPUT
# =========================================================

product_name = st.text_input(
    "Enter Product Name",
    placeholder="Example: Smart Fitness Watch"
)

target_market = st.selectbox(
    "Select Target Market",
    [
        "Global Market",
        "Healthcare",
        "Education",
        "Finance",
        "Technology",
        "Fashion",
        "Automobile"
    ]
)

# =========================================================
# GENERATE BUTTON
# =========================================================

if st.button("🚀 Generate Marketing Content"):

    if product_name.strip() == "":

        st.warning("Please enter a product name.")

    else:

        prompt = f"""
        You are an International Business Marketing Expert.

        Product Name:
        {product_name}

        Target Market:
        {target_market}

        Generate the following:

        1. A Global-Ready Product Title

        2. A Powerful Marketing Slogan

        3. Product Advertising Descriptions from:
           - Digital Marketing Expert
           - Brand Strategist
           - International Sales Consultant

        Requirements:
        - Professional branding
        - Emotional engagement
        - International marketing standards
        - Persuasive advertising
        - Global audience compatibility
        - Premium business tone
        """

        with st.spinner("Generating AI Marketing Content..."):

            result = generator(
                prompt,
                max_length=max_tokens,
                do_sample=True,
                temperature=temperature
            )

            output = result[0]["generated_text"]

        # =========================================================
        # DISPLAY OUTPUT
        # =========================================================

        st.success("Marketing Content Generated Successfully!")

        st.markdown("## 📢 Generated Marketing Content")

        st.markdown(f"""
        <div class="output-box">
        {output}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SAMPLE OUTPUT SECTION
# =========================================================

st.markdown("---")

st.markdown("## 💡 Example Products")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("Smart Fitness Watch")

with col2:
    st.info("AI Health Tracker")

with col3:
    st.info("Electric Scooter")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Developed using:
Streamlit + Hugging Face Transformers + Generative AI
""")
