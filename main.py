import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import numpy as np
import io

# ======== Core Encryption Functions ========
def generate_lorenz_sequence(length):
    x, y, z = 0.1, 0.0, 0.0
    seq = []
    for _ in range(length):
        x += 0.01 * (10 * (y - x))
        y += 0.01 * (x * (28 - z) - y)
        z += 0.01 * (x * y - (8/3) * z)
        seq.append(abs(x + y + z) % 1)
    return np.array(seq)

def encrypt_image(img_array):
    flat_img = img_array.flatten()
    seq = generate_lorenz_sequence(len(flat_img))
    indices = np.argsort(seq)
    shuffled_img = flat_img[indices]
    chaotic_vals = (seq * 255).astype(np.uint8)
    diffused_img = (shuffled_img.astype(np.uint16) + chaotic_vals) % 256
    return diffused_img.astype(np.uint8).reshape(img_array.shape), shuffled_img.reshape(img_array.shape), diffused_img.reshape(img_array.shape)

# ======== Histogram Function (Light Mode) ========
def plot_histogram(image_array, title, color='steelblue'):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(image_array.flatten(), bins=256, color=color, edgecolor='black', alpha=0.7)
    ax.set_title(title, fontsize=12, pad=10, color='black')
    ax.set_xlabel('Pixel Value', fontsize=10, color='black')
    ax.set_ylabel('Frequency', fontsize=10, color='black')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_facecolor("#FAFAFA")
    fig.patch.set_facecolor("#FFFFFF")
    for spine in ax.spines.values():
        spine.set_edgecolor('#CCCCCC')
    return fig

# ======== Streamlit UI (White Mode) ========
def main():
    st.set_page_config(page_title="Image Cryptography", layout="centered")
    st.markdown("""
    <style>
    :root {
        --primary: #0078D7;
        --secondary: #00BFA6;
        --background: #FFFFFF;
        --surface: #FAFAFA;
        --text: #000000;
        --border: #DDDDDD;
    }
    html, body, .stApp {
        background-color: var(--background) !important;
        color: var(--text) !important;
    }
    .stTextInput>div>div>input, 
    .stTextArea>div>div>textarea {
        background-color: var(--surface) !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
    }
    .stButton>button {
        background-color: var(--primary) !important;
        color: white !important;
        border: none;
        font-weight: bold;
        margin-top: 5px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stDownloadButton>button {
        background-color: var(--secondary) !important;
        color: white !important;
        font-weight: bold;
    }
    .stImage>img {
        border: 1px solid var(--border);
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0,0,0,0.05);
    }
    h1, h2, h3, h4, h5, h6 {
        color: var(--primary) !important;
    }
    .stPlotlyChart, .stPyplot {
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 10px;
        background-color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🔐 Chaotic Image Cryptography with Histogram Analysis")

    img_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if img_file:
        try:
            img = Image.open(img_file)
            img = img.convert('RGB')
            img_array = np.array(img)
            
            with st.spinner('Processing...'):
                final_img, confusion_img, diffusion_img = encrypt_image(img_array)
                
                # Original vs Encrypted
                st.subheader("Encryption Process")
                col1, col2 = st.columns(2)
                with col1:
                    st.image(img, caption="Original Image", width=300)
                    st.pyplot(plot_histogram(img_array, "Original Image Histogram", '#0078D7'))
                with col2:
                    st.image(final_img, caption="Final Encrypted Image", width=300)
                    st.pyplot(plot_histogram(final_img, "Encrypted Image Histogram", '#00BFA6'))
                
                # Confusion vs Diffusion
                st.subheader("Processing Stages")
                col3, col4 = st.columns(2)
                with col3:
                    st.image(confusion_img, caption="After Confusion (Scrambled)", width=300)
                    st.pyplot(plot_histogram(confusion_img, "Confusion Stage Histogram", '#FFA000'))
                with col4:
                    st.image(diffusion_img, caption="After Diffusion (Encrypted)", width=300)
                    st.pyplot(plot_histogram(diffusion_img, "Diffusion Stage Histogram", '#E53935'))

                # Histogram Analysis
                st.subheader("🔍 Histogram Analysis")
                st.markdown("""
                - **Original Histogram:** Natural pixel distribution.
                - **Confusion Stage:** Shows pixel scrambling — uniformity = better confusion.
                - **Diffusion Stage:** Shows pixel value changes — uniformity = better diffusion.
                - **Final Encrypted:** Near-uniform distribution = high encryption strength.
                """)

                # Download
                buf = io.BytesIO()
                Image.fromarray(final_img).save(buf, format='PNG')
                st.download_button("💾 Download Encrypted Image", buf.getvalue(), "encrypted.png", mime="image/png")

        except Exception as e:
            st.error(f"❌ Encryption failed: {str(e)}")

if __name__ == "__main__":
    main()
