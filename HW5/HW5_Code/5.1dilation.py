if __name__ == '__main__':
    from PIL import Image
    import numpy as np

    # Define kernel for dilation.
    kernel = np.array([\
        [0, 1, 1, 1, 0], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [0, 1, 1, 1, 0]])
    # Define center of kernel for dilation.
    centerKernel = (2, 2)
    # Load image from file.
    originalImage = Image.open('lena.bmp')
    # New image with the same size and 'grayscale' format.
    dilationImage = Image.new('L', originalImage.size)
    # Scan each column in original image.
    for r in range(originalImage.size[0]):
        # Scan each row in original image.
        for c in range(originalImage.size[1]):
            # Record local max. pixel value.
            localMaxPixel = 0
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
                            # Update local max. pixel value.
                            localMaxPixel = max(localMaxPixel, originalPixel)
            # Paste local max. pixel value on original image.
            dilationImage.putpixel((r, c), localMaxPixel)
    # Save image fo file.
    dilationImage.save('dilation.bmp')