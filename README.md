# Secure-Image-Encryption-System-Using-Chaotic-Algorithm
A Streamlit-based secure image encryption system using Lorenz chaotic algorithm with confusion–diffusion stages and histogram analysis for validating encryption strength.

#  Secure Image Encryption System Using Chaotic Algorithm

This project implements a **secure image encryption system** based on the **Lorenz chaotic system**, using **confusion and diffusion principles** to protect digital images.  
It also includes **histogram analysis** to evaluate the strength and randomness of the encryption.

The application is built as an interactive **web app using Streamlit**.

---

##  Project Objective

To secure digital images against unauthorized access by leveraging the **randomness and sensitivity of chaotic systems**, ensuring strong encryption and resistance to statistical attacks.

---

##  Core Concept

The encryption is based on the **Lorenz chaotic map**, which generates a pseudo-random sequence used for:

- **Confusion** – Rearranging pixel positions
- **Diffusion** – Modifying pixel intensity values

These stages together provide strong cryptographic security.

---

##  Features

- Upload RGB images (`.png`, `.jpg`, `.jpeg`)
- Chaotic sequence generation using Lorenz system
- Image encryption using:
  - Pixel scrambling (confusion)
  - Pixel value modification (diffusion)
- Histogram analysis for:
  - Original image
  - Confusion stage
  - Diffusion stage
  - Final encrypted image
- Download encrypted image
- Clean and interactive Streamlit UI

---

##  Tech Stack

- **Programming Language:** Python  
- **Framework:** Streamlit  
- **Libraries Used:**
  - NumPy
  - Pillow (PIL)
  - Matplotlib
  - Streamlit

---

##  Encryption Workflow

1. **Image Upload**
2. **Lorenz Chaotic Sequence Generation**
3. **Confusion Stage**
   - Pixel positions are rearranged using chaotic sequence
4. **Diffusion Stage**
   - Pixel values are modified using chaotic values
5. **Final Encrypted Image Generation**
6. **Histogram Analysis**
   - Used to verify uniformity and randomness

---

##  Histogram Analysis Explanation

- **Original Image Histogram:** Shows natural pixel distribution
- **Confusion Histogram:** Indicates effective scrambling
- **Diffusion Histogram:** Shows pixel value spreading
- **Encrypted Image Histogram:** Near-uniform distribution confirms strong encryption

Uniform histograms indicate high resistance to statistical attacks.

---

##  How to Run the Project

### 1 Clone the Repository
```bash
git clone https://github.com/your-username/Secure-Image-Encryption-System-Using-Chaotic-Algorithm.git
cd Secure-Image-Encryption-System-Using-Chaotic-Algorithm
