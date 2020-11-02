def getBinaryImage(originalImage, threshold):
    """
    :type originalImage: Image (from PIL)
    :type threshold: int
    :return type: Image (from PIL)
    """
    from PIL import Image
    # New image with the same size and 'binary' format.
    binaryImage = Image.new('1', originalImage.size)
    # Scan each column in original image.
    for c in range(originalImage.size[0]):
        # Scan each row in original image.
        for r in range(originalImage.size[1]):
            # Get pixel value in original image at (c, r).
            originalPixel = originalImage.getpixel((c, r))
            if (originalPixel >= threshold):
                # Put pixel value '1'  to binary image.
                binaryImage.putpixel((c, r), 1)
            else:
                # Put pixel value '0'  to binary image.
                binaryImage.putpixel((c, r), 0)
    # Return binary image.
    return binaryImage

if __name__ == '__main__':
    from PIL import Image
    import numpy as np

    # Load image from file.
    originalImage = Image.open('lena.bmp')
    # Get binary image.
    binaryImage = getBinaryImage(originalImage, 128)
    # Save binary image fo file.
    binaryImage.save('binary.bmp')