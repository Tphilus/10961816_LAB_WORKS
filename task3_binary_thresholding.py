import cv2
import matplotlib.pyplot as plt
import numpy as np

def binary_thresholding_analysis():
    """
    Answer the binary thresholding question and demonstrate the concept.
    
    Question: A pixel in a grayscale image has a value of 180. 
    If the threshold for binary thresholding is set to 150, 
    what is the new pixel value after applying binary thresholding?
    """
    
    print("=" * 60)
    print("TASK 3: BINARY THRESHOLDING QUESTION")
    print("=" * 60)
    
    # Given values
    pixel_value = 180
    threshold = 150
    
    print(f"Given:")
    print(f"- Original pixel value: {pixel_value}")
    print(f"- Threshold value: {threshold}")
    print(f"- Output values: 0 (below threshold) or 255 (above threshold)")
    print()
    
    # Apply binary thresholding logic
    if pixel_value > threshold:
        new_pixel_value = 255
        comparison = "above"
    else:
        new_pixel_value = 0
        comparison = "below or equal to"
    
    print(f"Analysis:")
    print(f"- {pixel_value} is {comparison} {threshold}")
    print(f"- Therefore, the new pixel value = {new_pixel_value}")
    print()
    print(f"ANSWER: {new_pixel_value}")
    print("=" * 60)
    
    return new_pixel_value

def demonstrate_binary_thresholding(image_path=None):
    """
    Demonstrate binary thresholding on an actual image.
    
    Args:
        image_path (str): Path to input image. If None, creates a sample image.
    """
    
    if image_path and cv2.imread(image_path) is not None:
        # Load and convert to grayscale
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(f"Loaded image from: {image_path}")
    else:
        # Create a sample gradient image for demonstration
        gray_image = np.zeros((200, 400), dtype=np.uint8)
        for i in range(400):
            gray_image[:, i] = int(255 * i / 400)  # Gradient from 0 to 255
        print("Created sample gradient image for demonstration")
    
    # Apply different threshold values
    thresholds = [50, 100, 150, 200]
    
    plt.figure(figsize=(15, 10))
    
    # Display original grayscale image
    plt.subplot(2, 3, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')
    
    # Apply and display binary thresholding with different thresholds
    for i, thresh_val in enumerate(thresholds):
        # Apply binary thresholding
        _, binary_image = cv2.threshold(gray_image, thresh_val, 255, cv2.THRESH_BINARY)
        
        plt.subplot(2, 3, i + 2)
        plt.imshow(binary_image, cmap='gray')
        plt.title(f'Binary Threshold = {thresh_val}')
        plt.axis('off')
        
        # Save the binary image
        cv2.imwrite(f'binary_threshold_{thresh_val}.jpg', binary_image)
    
    # Display histogram with threshold lines
    plt.subplot(2, 3, 6)
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    plt.plot(hist, color='black')
    
    # Add threshold lines
    colors = ['red', 'blue', 'green', 'orange']
    for thresh_val, color in zip(thresholds, colors):
        plt.axvline(thresh_val, color=color, linestyle='--', 
                   label=f'Threshold {thresh_val}')
    
    plt.title('Histogram with Threshold Lines')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print(f"\nBinary threshold images saved:")
    for thresh_val in thresholds:
        print(f"- binary_threshold_{thresh_val}.jpg")

def custom_binary_threshold(image, threshold_value):
    """
    Implement custom binary thresholding to demonstrate the concept.
    
    Args:
        image (numpy.ndarray): Input grayscale image
        threshold_value (int): Threshold value (0-255)
    
    Returns:
        numpy.ndarray: Binary thresholded image
    """
    
    # Create output image
    binary_output = np.zeros_like(image)
    
    # Apply thresholding: 255 if pixel > threshold, 0 otherwise
    binary_output[image > threshold_value] = 255
    binary_output[image <= threshold_value] = 0
    
    return binary_output

# Example usage and testing
if __name__ == "__main__":
    # Answer the specific question
    answer = binary_thresholding_analysis()
    
    print("\n" + "=" * 60)
    print("BINARY THRESHOLDING DEMONSTRATION")
    print("=" * 60)
    
    # Demonstrate binary thresholding
    try:
        # Try to use actual image if available
        demonstrate_binary_thresholding('photo.jpg')
    except:
        # Use sample image if no photo.jpg found
        demonstrate_binary_thresholding()
    
    print("\nTask 3 completed successfully!")
    
    # Additional verification with the specific example
    print(f"\nVerification of the question:")
    test_pixel = 180
    test_threshold = 150
    result = 255 if test_pixel > test_threshold else 0
    print(f"Pixel value {test_pixel} with threshold {test_threshold} → {result}")