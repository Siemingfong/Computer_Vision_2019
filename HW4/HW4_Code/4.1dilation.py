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
    # Load image from file.
    originalImage = Image.open('binary.bmp')
    # Get center position of kernel.
    centerKernel = tuple([x // 2 for x in kernel.shape])
    # New image with the same size and 'binary' format.
    dilationImage = Image.new('1', originalImage.size)
    # Scan each column in original image.
    for r in range(originalImage.size[0]):
        # Scan each row in original image.
        for c in range(originalImage.size[1]):
            # Get pixel value in original image at (r, c).
            originalPixel = originalImage.getpixel((r, c))
            # If this pixel is object (1, white).
            if (originalPixel != 0):
                # Paste kernel on original image at (r, c).
                # Scan each column in kernel.
                for x in range(kernel.shape[0]):
                    # Scan each row in kernel.
                    for y in range(kernel.shape[1]):
                        # Only paste '1' value from kernel.
                        if (kernel[x, y] == 1):
                            # Calculate destination x, y position.
                            destX = r + (x - centerKernel[0])
                            destY = c + (y - centerKernel[1])
                            # Avoid out of image range.
                            if ((0 <= destX < originalImage.size[0]) and \
                                (0 <= destY < originalImage.size[1])):
                                # Paste '1' value on original image.
                                dilationImage.putpixel((destX, destY), 1)

    # Save image fo file.
    dilationImage.save('dilation.bmp')
