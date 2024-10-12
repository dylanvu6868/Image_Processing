import cv2
import numpy as np

# Load images
img = cv2.imread(r"D:\CPV301_VHD\blackpink.jpg")
img1 = cv2.imread(r"D:\CPV301_VHD\liverpool2324.jpg")
img2 = cv2.imread(r"D:\CPV301_VHD\blackpink.jpg")

scale_percent = 50  # Giảm kích thước ảnh xuống 50%
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)

# Resize img2 to match img1
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# # 1. Multiplication and Addition with a Constant
# def multiply_add(img, alpha=1.5, beta=30):
#     result = alpha * img + beta
#     return np.clip(result, 0, 255).astype(np.uint8)

# result_img = multiply_add(img)
# cv2.imshow("Original Image", img)
# cv2.imshow("Multiplication and Addition", result_img)

# # 2. Multiplicative Gain (Scaling)
# def apply_gain(img, gain=1.6):
#     result = gain * img
#     return np.clip(result, 0, 255).astype(np.uint8)

# gained_img = apply_gain(img)
# cv2.imshow("Original Image", img)
# cv2.imshow("Gained Image", gained_img)

# # 3. Linear Blend (Dyadic Operator)
# def blend_images(img1, img2, alpha=0.5):
#     return cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)

# blended_img = blend_images(img1, img2, alpha=0.5)
# cv2.imshow("Original Image", img)
# cv2.imshow("Original Image 1", img1)
# cv2.imshow("Blended Image", blended_img)

# 4. Invert Gamma Mapping
def invert_gamma(img, gamma=2.2):
    inv_gamma = 1.0 / gamma
    img_normalized = img / 255.0
    corrected_img = np.power(img_normalized, inv_gamma)
    return (corrected_img * 255).astype(np.uint8)

gamma_inverted_img = invert_gamma(img, gamma=2.2)
cv2.imshow("Original Image", img)
cv2.imshow("Gamma Inverted Image", gamma_inverted_img)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows(2000)
