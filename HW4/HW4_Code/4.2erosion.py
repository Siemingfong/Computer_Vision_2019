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
    # Load image from file.
    originalImage = Image.open('binary.bmp')
    # Get center position of kernel.
    centerKernel = tuple([x // 2 for x in kernel.shape])
    # New image with the same size and 'binary' format.
    erosionImage = Image.new('1', originalImage.size)
    # Scan each column in original image.
    for r in range(originalImage.size[0]):
        # Scan each row in original image.
        for c in range(originalImage.size[1]):
            # Flag of match.
            matchFlag = True
            # Scan each column in kernel.
            for x in range(kernel.shape[0]):
                # Scan each row in kernel.
                for y in range(kernel.shape[1]):
                    # Only check '1' value from kernel.
                    if (kernel[x, y] == 1):
                        # Calculate destination x, y position.
                        destX = r + (x - centerKernel[0])
                        destY = c + (y - centerKernel[1])
                        # Avoid out of image range.
                        if ((0 <= destX < originalImage.size[0]) and \
                            (0 <= destY < originalImage.size[1])):
                            # If this point doesn't match with kernel.
                            if (originalImage.getpixel((destX, destY)) == 0):
                                # Clear flag of match.
                                matchFlag = False
                                break
                        # It is edge point, it will never match.
                        else:
                            # Clear flag of match.
                            matchFlag = False
                            break
            # Full kernel is match in original image at (r, c).
            if (matchFlag):
                # Paste '1' value on original image.
                erosionImage.putpixel((r, c), 1)
    # Save image fo file.
    erosionImage.save('erosion.bmp')