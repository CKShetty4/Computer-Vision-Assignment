# Computer Vision Assignment – B.Tech CSE (RUAS)

This repository contains the implementation and report for the Computer Vision assignment as part of the B.Tech in CSE curriculum at Ramaiah University of Applied Sciences.

## Assignment Overview

* **Course Title:** Computer Vision
* **Course Code:** 20AIC313A
* **Instructor:** Ms. Anitha K R

---

## Contents

* `main.py` – Python script using OpenCV for image processing tasks.
* `BTech_CSE_A_Assignment_Computer_Vision.pdf` – Complete report with detailed explanations, theoretical questions, and analysis.

---

## Tasks Implemented in `main.py`

1. **Convert RGB Image to Grayscale**
2. **Resize Image to 512 × 512**
3. **Enhance Contrast using Histogram Equalization**
4. **Display Histograms (Before & After Equalization)**
5. **Apply Median Filter for Noise Reduction**

All intermediate and final outputs are saved to the specified output directory. 

*Matplotlib is used for visualization instead of `cv2.imshow`.

---

## Theoretical Topics Covered

* Detailed explanation of **Deep Learning in Computer Vision**
* Discussion on **Challenges in Real-world Implementation** of Deep Learning
* Reflection on **Skills and Benefits Gained** during assignment execution

---

## Requirements

* Python 3.7+
* OpenCV (`cv2`)
* NumPy
* Matplotlib

---

## Usage

Clone the repository and run the script, use the following commands in your terminal:

```bash
git clone https://github.com/CKShetty4/Computer-Vision-Assignment.git
cd Computer-Vision-Assignment
```

Ensure `InputImage.jpg`  is placed in the root directory or update the `image_path` in `main.py`.

Install dependencies if required:

```bash
pip install opencv-python numpy matplotlib
```

Run the script:

```bash
python main.py
```

---

## Output Directory

Processed images are saved in same directory

Modify the path in `main.py` if necessary.

---

## Key Takeaways

This project enhanced hands-on skills in image preprocessing, histogram manipulation, and Python scripting with OpenCV, while also deepening theoretical knowledge in CNNs and real-world DL challenges.

---

## References

* Goodfellow et al., *Deep Learning*
* Krizhevsky et al., *ImageNet Classification with Deep CNNs*
* He et al., *ResNet: Deep Residual Learning*
* Buolamwini & Gebru, *Gender Shades*
* And more (see PDF report for full list)

