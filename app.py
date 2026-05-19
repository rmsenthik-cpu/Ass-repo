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
    border-radius: 12px;
    margin-top: 20px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("🌍 International Business Marketing Prompt Application")

st.markdown("""
### Generate International Marketing Content using Generative AI

This application automatically generates:

✅ A Global-Ready Product Title  
✅ A Powerful Marketing Slogan  
✅ Product Advertising Descriptions from:
- Digital Marketing Expert
- Brand Strategist
- International Sales Consultant

""")

# =========================================================
# LOAD MODEL
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
# SIDEBAR SETTINGS
# =========================================================

st.sidebar.title("⚙ AI Settings")

temperature = st.sidebar.slider(
    "Temperature",
    0.1,
    1.0,
    0.8
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
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

# =========================================================
# GENERATE BUTTON
# =========================================================

if st.button("🚀 Generate Marketing Content"):

    if product_name.strip() == "":

        st.warning("Please enter a product name.")

    else:

        prompt = f"""
You are a world-class International Business Marketing Expert.

Generate the following for the product: {product_name}

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

Format the response exactly like this:

Global-Ready Product Title:
<answer>

Powerful Marketing Slogan:
<answer>

Digital Marketing Expert:
<answer>

Brand Strategist:
<answer>

International Sales Consultant:
<answer>
"""

        with st.spinner("Generating AI Marketing Content..."):

            result = generator(
                prompt,
                max_length=max_tokens,
                do_sample=True,
                temperature=temperature,
                truncation=True
            )

            output = result[0]["generated_text"]

        # =========================================================
        # DISPLAY OUTPUT
        # =========================================================

        st.success("Marketing Content Generated Successfully!")

        st.markdown("## 📢 Generated Output")

        st.markdown(f"""
        <div class="output-box">
        <pre>{output}</pre>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SAMPLE OUTPUT
# =========================================================

st.markdown("---")

st.markdown("## 💡 Example Input")

st.info("Smart Fitness Watch")

st.markdown("""
### Expected Output Format

Global-Ready Product Title:
FitPulse Global X

Powerful Marketing Slogan:
"Empowering Every Moment Worldwide"

Digital Marketing Expert:
A next-generation smart wearable designed for modern global consumers.

Brand Strategist:
FitPulse creates a premium emotional connection between technology and wellness.

International Sales Consultant:
Designed for international scalability with universal market appeal.
""")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Developed using Streamlit + Hugging Face Transformers + Prompt Engineering
""")
