import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image from the path (assuming grayscale)
img_path = 'anhlocbang_fourier.png'
image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Step 1: Apply Fourier Transform
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)

# Step 2: Create a mask to filter out unwanted frequencies (e.g., horizontal/vertical lines)
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2

# Create a mask first, center square is 1, remaining all zeros
mask = np.ones((rows, cols), np.uint8)
mask[crow-10:crow+10, :] = 0  # Horizontal line removal

# Apply mask to the shifted Fourier transform
fshift_filtered = fshift * mask

# Step 3: Inverse Fourier Transform
f_ishift = np.fft.ifftshift(fshift_filtered)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Normalize the output image to the range 0-255
img_back_normalized = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Step 4: Plot original and filtered images for comparison
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].imshow(image, cmap='gray')
axs[0].set_title('Original Image')
axs[0].axis('off')

axs[1].imshow(img_back_normalized, cmap='gray')
axs[1].set_title('Filtered Image')
axs[1].axis('off')

plt.show()