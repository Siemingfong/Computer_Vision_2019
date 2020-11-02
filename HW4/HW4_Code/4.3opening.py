if __name__ == '__main__':
    from PIL import Image
    import numpy as np
    import Mathematical

    # Define kernel for opening.
    kernel = np.array([\
        [0, 1, 1, 1, 0], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [0, 1, 1, 1, 0]])
    # Load image from file.
    originalImage = Image.open('binary.bmp')
    # Get opening image.
    openingImage = Mathematical.opening(originalImage, kernel)
    # Save image fo file.
    openingImage.save('opening.bmp')