import streamlit as st
from transformers import pipeline

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="International Business Marketing AI",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🌍 International Business Marketing Prompt Application")

st.markdown("""
Generate:
- Global Product Titles
- Marketing Slogans
- International Advertising Content

using Generative AI Prompt Engineering.
""")

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

@st.cache_resource
def load_model():
    generator = pipeline(
        "text-generation",
        model="gpt2"
    )
    return generator

generator = load_model()

# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------

product_name = st.text_input(
    "Enter Product Name",
    placeholder="Example: Smart Fitness Watch"
)

# ---------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------

if st.button("Generate Marketing Content"):

    if product_name.strip() == "":
        st.warning("Please enter a product name.")
    else:

        prompt = f"""
        You are an international business marketing expert.

        Generate the following for the product:
        {product_name}

        1. Global-Ready Product Title
        2. Powerful Marketing Slogan
        3. Product Advertising Description from:
           - Digital Marketing Expert
           - Brand Strategist
           - International Sales Consultant

        Requirements:
        - Professional tone
        - Emotional engagement
        - International branding style
        - Persuasive marketing
        - Global audience compatibility
        """

        with st.spinner("Generating AI Marketing Content..."):

            result = generator(
                prompt,
                max_length=300,
                do_sample=True,
                temperature=0.8
            )

            output = result[0]["generated_text"]

        # ---------------------------------------------------
        # DISPLAY OUTPUT
        # ---------------------------------------------------

        st.subheader("Generated Marketing Content")

        st.write(output)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")
st.caption("Developed using Streamlit + Hugging Face Transformers")
