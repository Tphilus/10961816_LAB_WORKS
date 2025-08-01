# 10961816_LAB_WORKS
################################################

# Image Processing Tasks

This project contains Python scripts for basic image processing operations including grayscale conversion, color space transformations, and binary thresholding.

## Required Libraries

Install the following Python libraries before running the scripts:

```bash
pip install opencv-python matplotlib numpy
```

Or using conda:
```bash
conda install opencv matplotlib numpy
```

## File Structure

Make sure your project directory has the following structure:

```
project_directory/
├── photo.jpg                    # Your input image
├── task1_grayscale.py          # Task 1 script
├── task2_color_spaces.py       # Task 2 script  
├── task3_binary_thresholding.py # Task 3 script
└── requirements.txt            # Dependencies (optional)
```

## Usage Instructions

### Task 1: Image Loading and Grayscale Conversion

```bash
python task1_grayscale.py
```

**Outputs:**
* Displays original and grayscale images
* Saves `photo_gray.jpg`

### Task 2: Color Space Conversion and Histogram

```bash
python task2_color_spaces.py
```

**Outputs:**
* Displays original, grayscale, HSV, and LAB images
* Saves `photo_grayscale.jpg`, `photo_hsv.jpg`, `photo_lab.jpg`
* Displays and saves histogram as `grayscale_histogram.png`

### Task 3: Binary Thresholding

```bash
python task3_binary_thresholding.py
```

**Outputs:**
* Answers the theoretical question (pixel value 180 → 255)
* Demonstrates binary thresholding with multiple threshold values
* Saves multiple binary threshold images

## Task 3 Answer

**Question:** A pixel in a grayscale image has a value of 180. If the threshold for binary thresholding is set to 150, what is the new pixel value?

**Answer:** **255**

**Explanation:** Since 180 > 150 (pixel value is above threshold), the new pixel value becomes 255.

## Key Features

### Task 1 Features:
* Error handling for missing image files
* Side-by-side display of original and grayscale images
* Proper color space conversion for display

### Task 2 Features:
* Multiple color space conversions (RGB, Grayscale, HSV, LAB)
* Comprehensive histogram analysis with statistics
* Automatic file saving with descriptive names

### Task 3 Features:
* Theoretical question answered with explanation
* Practical demonstration with multiple threshold values
* Custom implementation showing the thresholding logic
* Visual comparison of different threshold effects

## Notes

* All scripts include comprehensive error handling
* Comments explain each step of the process
* Images are properly converted for matplotlib display (BGR→RGB)
* Histogram includes statistical information (mean, standard deviation)
* Binary thresholding demonstrates both OpenCV and custom implementations

## Troubleshooting

**"Could not load image" error:**
* Ensure `photo.jpg` exists in the same directory as the script
* Check that the image file is not corrupted
* Verify the file extension matches the filename in the script

**Import errors:**
* Install required libraries using pip or conda
* Ensure Python version compatibility (Python 3.6+)

**Display issues:**
* If plots don't show, try adding `plt.show()` or running in an interactive environment
* For Jupyter notebooks, use `%matplotlib inline`



# DCIT 412 Computer Vision Lab Assignment

**University of Ghana**  
*All rights reserved*

**Department of Computer Science**

## Instructions

### 1. Repository Setup

- Create a new GitHub repository named `STUDENTID_LAB_WORKS` (e.g., `10907000_LAB_WORKS`)
- Follow the GitHub account **theboybrey** at [github.com/theboybrey](https://github.com/theboybrey)
- Invite **theboybrey** as a collaborator to your repository

### 2. Repository Structure

- Set the default branch name to your surname (e.g., rename `main` or `master` to `bentil`)
- Organize tasks as subdirectories within the main repository
- Ensure a clear and consistent commit history, as it will be reviewed for evaluation

## Tasks

### Task 1: Image Loading and Grayscale Conversion

Write a Python script that:

- Loads an image file (e.g., `photo.jpg`)
- Converts the image to grayscale
- Displays both the original and grayscale images
- Saves the grayscale image as `photo_gray.jpg`

### Task 2: Color Space Conversion and Histogram

Write a Python script that:

- Loads a color image
- Converts the image to the following color spaces: Grayscale, HSV, and LAB
- Displays each converted image
- Saves each converted image with appropriate filenames (e.g., `photo_grayscale.jpg`, `photo_hsv.jpg`, `photo_lab.jpg`)
- Plots and displays the histogram of the grayscale image

### Task 3: Binary Thresholding Question

A pixel in a grayscale image has a value of 180. If the threshold for binary thresholding is set to 150, what is the new pixel value after applying binary thresholding? 

*(Assume output values are 0 for pixels below the threshold and 255 for pixels above the threshold.)*

## Submission Notes

- Ensure all scripts are well-documented with comments explaining the code
- Verify that all outputs (images, histograms) are correctly saved and displayed
- Maintain a clean commit history with descriptive messages for each task