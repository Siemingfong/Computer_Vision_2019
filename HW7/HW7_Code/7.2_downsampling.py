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

def downsampling(originalImage, sampleFactor):
    """
    :type originalImage: Image (from PIL)
    :type sampleFactor: int
    :return type: Image (from PIL)
    """
    from PIL import Image
    # Calculate the width and height of downsampling image.
    downsamplingWidth = int(originalImage.size[0] / sampleFactor)
    downsamplingHeight = int(originalImage.size[1] / sampleFactor)
    # New image with the downsampling size and 'binary' format.
    downsamplingImage = Image.new('1', (downsamplingWidth, downsamplingHeight))
    # Scan each column in downsampling image.
    for c in range(downsamplingImage.size[0]):
        # Scan each row in downsampling image.
        for r in range(downsamplingImage.size[1]):
            # Get pixel value in original image at (c * sampleFactor, r * sampleFactor).
            originalPixel = originalImage.getpixel((c * sampleFactor, r * sampleFactor))
            # Put pixel to downsampling image.
            downsamplingImage.putpixel((c, r), originalPixel)
    # Return downsampling image.
    return downsamplingImage

if __name__ == '__main__':
    from PIL import Image
    import numpy as np

    # Load image from file.
    originalImage = Image.open('lena.bmp')
    # Get binary image.
    binaryImage = getBinaryImage(originalImage, 128)
    # Save binary image fo file.
    binaryImage.save('binary.bmp')

    # Get downsampling image.
    downsamplingImage = downsampling(binaryImage, 8)
    # Save downsampling image fo file.
    downsamplingImage.save('downsampling.bmp')