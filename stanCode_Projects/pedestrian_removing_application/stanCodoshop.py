"""
File: stanCodoshop.py
Name: Jason Hsu
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** 0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # rgb = []
    # total_red = 0  # The sum of red pixels
    # total_green = 0  # The sum of green pixels
    # total_blue = 0  # The sum of blue pixels
    # for pixel in pixels:
    #     total_red += pixel.red
    #     total_green += pixel.green
    #     total_blue += pixel.blue
    # rgb.append(total_red // len(pixels))
    # rgb.append(total_green // len(pixels))
    # rgb.append(total_blue // len(pixels))

    total_red = sum(pixel.red for pixel in pixels)
    total_green = sum(pixel.green for pixel in pixels)
    total_blue = sum(pixel.blue for pixel in pixels)
    rgb = [total_red//len(pixels), total_green//len(pixels), total_blue//len(pixels)]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    pixel_avg_lst = get_average(pixels)
    # minimum = float('Inf')
    # best = None
    pixel_dist_lst = []
    for pixel in pixels:
        pixel_dist_lst.append((get_pixel_dist(pixel, pixel_avg_lst[0], pixel_avg_lst[1], pixel_avg_lst[2]), pixel))
        # dist = get_pixel_dist(pixel, pixel_avg_lst[0], pixel_avg_lst[1], pixel_avg_lst[2])
        # if dist < minimum:
        #     minimum = dist
        #     best = pixel
    best = min(pixel_dist_lst, key=lambda t: t[0])[1]
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    for x in range(width):
        for y in range(height):
            pixel_lst = []  # Create a pixel list at each (x,y)
            for image in images:
                pixel_lst.append(image.get_pixel(x, y))  # Create a pixel list based on the same (x,y) from each image
            best_pixel = get_best_pixel(pixel_lst)  # Find the best pixel to be put on the blank image
            result.get_pixel(x, y).red = best_pixel.red
            result.get_pixel(x, y).green = best_pixel.green
            result.get_pixel(x, y).blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
