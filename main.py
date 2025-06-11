import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Function to compute and display histogram
def show_histogram(image, title):
    plt.figure(figsize=(6, 4))
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist, color='blue')
    plt.title(f'Histogram: {title}')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.show()

def show_image(image, title):
    plt.figure(figsize=(6, 6))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def show_combined_histograms(before_image, after_image, title_before, title_after, is_rgb_before=False):
    plt.figure(figsize=(10, 4))
    
    plt.subplot(121)
    if is_rgb_before:
        colors = ('r', 'g', 'b')
        for i, color in enumerate(colors):
            hist = cv2.calcHist([before_image], [i], None, [256], [0, 256])
            plt.plot(hist, color=color, label=f'{color.upper()} Channel')
        plt.legend()
    else:
        hist_before = cv2.calcHist([before_image], [0], None, [256], [0, 256])
        plt.plot(hist_before, color='blue')
    plt.title(f'Histogram: {title_before}')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

    plt.subplot(122)
    hist_after = cv2.calcHist([after_image], [0], None, [256], [0, 256])
    plt.plot(hist_after, color='blue')
    plt.title(f'Histogram: {title_after}')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

# Input Image path
image_path = 'InputImage.jpg' # Change this to your image path

if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' not found")
    exit()

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image at '{image_path}'")
    exit()

# i) Convert RGB Image to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
show_image(gray_image, 'Grayscale Image')
show_histogram(gray_image, 'Grayscale Image')
show_combined_histograms(image, gray_image, 'Original RGB', 'Grayscale', is_rgb_before=True)

# ii) Change resolution to 512x512
resized_image = cv2.resize(gray_image, (512, 512), interpolation=cv2.INTER_AREA)
show_image(resized_image, 'Resized Image (512x512)')
show_histogram(resized_image, 'Resized Image')

# iii) Increase contrast using histogram equalization
equalized_image = cv2.equalizeHist(resized_image)
show_image(equalized_image, 'Equalized Image')
show_histogram(equalized_image, 'Equalized Image')

# iv) Display histograms before and after equalization together
show_combined_histograms(resized_image, equalized_image, 'Before Equalization', 'After Equalization', is_rgb_before=False)

# v) Apply Median filter
median_filtered = cv2.medianBlur(equalized_image, 5)
show_image(median_filtered, 'Median Filtered Image')
show_histogram(median_filtered, 'Median Filtered Image')

# Save all processed images
output_dir = 'd:/Desktop/Temp/Assignments/CV/'

cv2.imwrite(os.path.join(output_dir, 'grayscale_image.jpg'), gray_image)
cv2.imwrite(os.path.join(output_dir, 'resized_image.jpg'), resized_image)
cv2.imwrite(os.path.join(output_dir, 'equalized_image.jpg'), equalized_image)
cv2.imwrite(os.path.join(output_dir, 'median_filtered_image.jpg'), median_filtered)

print("All images processed and saved successfully.")