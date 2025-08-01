import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_and_convert_grayscale(image_path):
    """
    Load an image, convert to grayscale, display both versions, and save the grayscale image.
    
    Args:
        image_path (str): Path to the input image file
    """
    
    # Load the original image
    original_image = cv2.imread(image_path)
    
    # Check if image was loaded successfully
    if original_image is None:
        print(f"Error: Could not load image from {image_path}")
        return
    
    # Convert BGR to RGB for proper display with matplotlib
    original_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    
    # Convert to grayscale
    grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    
    # Display both images side by side
    plt.figure(figsize=(12, 5))
    
    # Display original image
    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title('Original Image')
    plt.axis('off')
    
    # Display grayscale image
    plt.subplot(1, 2, 2)
    plt.imshow(grayscale_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Save the grayscale image
    output_path = 'photo_gray.jpg'
    cv2.imwrite(output_path, grayscale_image)
    print(f"Grayscale image saved as: {output_path}")
    
    return original_image, grayscale_image

# Example usage
if __name__ == "__main__":
    # Replace 'photo.jpg' with your actual image path
    image_path = 'photo.jpg'
    
    try:
        original, grayscale = load_and_convert_grayscale(image_path)
        print("Task 1 completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure you have an image file named 'photo.jpg' in the same directory")