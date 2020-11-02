if __name__ == '__main__':
    from PIL import Image
    import numpy as np

    # Define kernel for erosion.
    kernel = np.array([\
        [0, 1, 1, 1, 0], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [0, 1, 1, 1, 0]])
    # Define center of kernel for erosion.
    centerKernel = (2, 2)
    # Load image from file.
    originalImage = Image.open('lena.bmp')
    # New image with the same size and 'grayscale' format.
    erosionImage = Image.new('L', originalImage.size)
    # Scan each column in original image.
    for r in range(originalImage.size[0]):
        # Scan each row in original image.
        for c in range(originalImage.size[1]):
            # Record local min. pixel value.
            localMinPixel = 255
            # Scan each column in kernel.
            for x in range(kernel.shape[0]):
                # Scan each row in kernel.
                for y in range(kernel.shape[1]):
                    # Only check value '1' in kernel.
                    if (kernel[x, y] == 1):
                        # Calculate destination x, y position.
                        destX = r + (x - centerKernel[0])
                        destY = c + (y - centerKernel[1])
                        # Avoid out of image range.
                        if ((0 <= destX < originalImage.size[0]) and \
                            (0 <= destY < originalImage.size[1])):
                            # Get pixel value in original image at (destX, destY).
                            originalPixel = originalImage.getpixel((destX, destY))
                            # Update local min. pixel value.
                            localMinPixel = min(localMinPixel, originalPixel)
            # Paste local min. pixel value on original image.
            erosionImage.putpixel((r, c), localMinPixel)
    # Save image fo file.
    erosionImage.save('erosion.bmp')