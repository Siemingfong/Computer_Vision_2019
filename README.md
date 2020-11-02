# CV2019Fall
Computer Vision I at NTU 2019 Fall.

# Indrocution
This course has 10 homeworks. The 10 homeworks are as follows:
1. Basic Image Manipulation
2. Basic Image Manipulation
3. Histogram Equalization
4. Mathematical Morphology - Binary Morphology
5. Mathematical Morphology - Gray Scaled Morphology
6. Yokoi Connectivity Number
7. Thinning
8. Noise Removal
9. General Edge Detection
10. Zero Crossing Edge Detection

# Table of Contents
<!--ts-->
   0. [Environment]()
   1. [Basic Image Manipulation]()
   2. [Basic Image Manipulation]()
   3. [Histogram Equalization]()
   4. [Mathematical Morphology - Binary Morphology]()
   5. [Mathematical Morphology - Gray Scaled Morphology]()
   6. [Yokoi Connectivity Number]()
   7. [Thinning]()
   8. [Noise Removal]()
   9. [General Edge Detection]()
   10. [Zero Crossing Edge Detection]()
<!--te-->

# Environment
* Programming Language: Python 3
* Programming IDE: Visual Studio Code
* Operating System: Windows 10 x64

# HW1: Basic Image Manipulation
* Part 1 of this homework is writing a program to generate the following images from lena.bmp.
   * Up-side-down lena.bmp.
   * Right-side-left lena.bmp.
   * Diagonally mirrored lena.bmp.
   * Code: [HW1.1]()
   
* Part 2 of this homework is using any kind of software to do the following things:
   * Rotate lena.bmp 45 degrees clockwise.
   * Shrink lena.bmp in half.
   * Binarize lena.bmp at 128 to get a binary image.
   * Code: [HW1.2]()
         
* [Report]()

# HW2: Basic Image Manipulation
* Part 1 of this homework is to binarize lena.bmp with threshold 128 (0-127, 128-255).
   * Code: [HW2.1]()
   
* Part 2 of this homework is to draw the histogram of lena.bmp.
   * Code: [HW2.2]()
   
* Part 3 of this homework is to find connected components with following rules:
   * Draw bounding box of regions.
   * Draw cross at centroid of regions.
   * Omit regions that have a pixel count less than 500.
   * Code: [HW2.3]()
   
* [Report]()

# HW3: Histogram Equalization
* This homework is to do histogram equalization with following rules:
   * Adjust the brightness of lena.bmp to one-third.
   * Do histogram equalization on dark image.
   * Show the histogram of the final image.
   * Code: [HW3.1]()
   
* [Report]()

# HW4: Mathematical Morphology - Binary Morphology
* This homework is to do binary morphology with following rules:
   * Please use the octagonal 3-5-5-5-3 kernel.
   * Please use the “L” shaped kernel to detect the upper-right corner for hit-and-miss transform.
   * Please process the white pixels (operating on white pixels).
   * Five images should be included in your report: Dilation, Erosion, Opening, Closing, and Hit-and-Miss.
   * Code: [HW4.1]()
   
* [Report]()

# HW5: Mathematical Morphology - Gray Scaled Morphology
* This homework is to do gray scaled morphology with following rules:
   * Please use the octagonal 3-5-5-5-3 kernel.
   * Please take the local maxima or local minima respectively.
   * Four images should be included in your report: Dilation, Erosion, Opening, and Closing.
   * Code: [HW5]()
   
* [Report]()

# HW6: Yokoi Connectivity Number
* This homework is to do Yokoi connectivity number with following rules:
   * Please binarize leba.bmp with threshold 128.
   * Please down sampling binary.bmp from 512x512 to 64x64, using 8x8 blocks as unit and take the topmost-left pixel as the down sampling data.
   * Print Yokoi connectivity number to text file.
   * Code: [HW6]()

* [Report]()

# HW7: Thinning
* This homework is to do thinning operation with following rules:
   * Please binarize leba.bmp with threshold 128.
   * Do thinning operation on binary image.
   * Code: [HW7]()
   
* [Report]()

# HW8: Noise Removal
* This homework is to do noise removal with following rules:
   * Generate Gaussian noise with amplitude of 10 and 30.
   * Generate salt-and-pepper noise with probability of 0.1 and 0.05.
   * Use the 3x3 and 5x5 box filter on noise images.
   * Use the 3x3 and 5x5 median filter on noise images.
   * Use opening-then-closing and closing-then-opening filter on noise images.
   * Calculate the signal-to-noise-ratio (SNR) of noise images.
   * Code: [HW8]()
   
* [Report]()

# HW9: General Edge Detection
* This homework is to do general edge detection with following rules:
   * Robert’s operator with threshold of 12.
   * Prewitt’s edge detector with threshold of 24.
   * Sobel’s edge detector with threshold of 38.
   * Frei and Chen’s gradient operator with threshold of 30.
   * Kirsch’s compass operator with threshold of 135.
   * Robinson’s compass operator with threshold of 43.
   * Nevatia-Babu 5x5 operator with threshold of 12500.
   * Code: [HW9]()

* [Report]()

# HW10: Zero Crossing Edge Detection
* This homework is to do zero crossing edge detection with following rules:
   * Laplacian mask 1 with threshold of 15.
   * Laplacian mask 2 with threshold of 15.
   * Minimum variance Laplacian with threshold of 20.
   * Laplacian of Gaussian with threshold of 3000.
   * Difference of Gaussian with threshold of 1.
   * Code: [HW10]()

* [Reference]()
