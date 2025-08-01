import cv2
import matplotlib.pyplot as plt
import numpy as np

def convert_color_spaces_and_histogram(image_path):
    """
    Load a color image, convert to different color spaces, display all images,
    save converted images, and plot histogram of grayscale image.
    
    Args:
        image_path (str): Path to the input image file
    """
    
    # Load the original image
    original_image = cv2.imread(image_path)
    
    # Check if image was loaded successfully
    if original_image is None:
        print(f"Error: Could not load image from {image_path}")
        return
    
    # Convert BGR to RGB for proper display
    original_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    
    # Convert to different color spaces
    grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    lab_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)
    
    # Display all images
    plt.figure(figsize=(15, 10))
    
    # Original image
    plt.subplot(2, 2, 1)
    plt.imshow(original_rgb)
    plt.title('Original Image (RGB)')
    plt.axis('off')
    
    # Grayscale image
    plt.subplot(2, 2, 2)
    plt.imshow(grayscale_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')
    
    # HSV image (convert to RGB for display)
    hsv_rgb = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
    plt.subplot(2, 2, 3)
    plt.imshow(hsv_rgb)
    plt.title('HSV Image')
    plt.axis('off')
    
    # LAB image (convert to RGB for display)
    lab_rgb = cv2.cvtColor(lab_image, cv2.COLOR_LAB2RGB)
    plt.subplot(2, 2, 4)
    plt.imshow(lab_rgb)
    plt.title('LAB Image')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Save all converted images
    cv2.imwrite('photo_grayscale.jpg', grayscale_image)
    cv2.imwrite('photo_hsv.jpg', hsv_image)
    cv2.imwrite('photo_lab.jpg', lab_image)
    
    print("Images saved:")
    print("- photo_grayscale.jpg")
    print("- photo_hsv.jpg") 
    print("- photo_lab.jpg")
    
    # Plot histogram of the grayscale image
    plt.figure(figsize=(10, 6))
    
    # Calculate histogram
    hist = cv2.calcHist([grayscale_image], [0], None, [256], [0, 256])
    
    # Plot histogram
    plt.plot(hist, color='black')
    plt.title('Histogram of Grayscale Image')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.grid(True, alpha=0.3)
    
    # Add some statistics to the plot
    mean_intensity = np.mean(grayscale_image)
    std_intensity = np.std(grayscale_image)
    plt.axvline(mean_intensity, color='red', linestyle='--', 
                label=f'Mean: {mean_intensity:.1f}')
    plt.axvline(mean_intensity + std_intensity, color='orange', linestyle=':', 
                label=f'Mean + Std: {mean_intensity + std_intensity:.1f}')
    plt.axvline(mean_intensity - std_intensity, color='orange', linestyle=':', 
                label=f'Mean - Std: {mean_intensity - std_intensity:.1f}')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Save histogram as image
    plt.savefig('grayscale_histogram.png', dpi=300, bbox_inches='tight')
    print("- grayscale_histogram.png")
    
    return grayscale_image, hsv_image, lab_image

# Example usage
if __name__ == "__main__":
    # Replace with your actual image path
    image_path = 'photo.jpg'
    
    try:
        grayscale, hsv, lab = convert_color_spaces_and_histogram(image_path)
        print("Task 2 completed successfully!")
        
        # Print some basic statistics
        print(f"\nImage Statistics:")
        print(f"Grayscale - Mean: {np.mean(grayscale):.2f}, Std: {np.std(grayscale):.2f}")
        print(f"Original image shape: {cv2.imread(image_path).shape}")
        print(f"Grayscale image shape: {grayscale.shape}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure you have an image file named 'photo.jpg' in the same directory")