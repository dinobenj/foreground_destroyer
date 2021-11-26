# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:08:03 2021

@author: Benjamin#2
"""
from PIL import Image
import random
from timeit import time

def back_pixels(input_image, sample_size):
    avg_pixel = []

    for i in range(sample_size):
        r = input_image.getpixel((i, 0))[0]
        g = input_image.getpixel((i, 0))[1]
        b = input_image.getpixel((i, 0))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-i-1, 0))[0]
        g = input_image.getpixel((width-i-1, 0))[1]
        b = input_image.getpixel((width-i-1, 0))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((i, height-1))[0]
        g = input_image.getpixel((i, height-1))[1]
        b = input_image.getpixel((i, height-1))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-1-i, height-1))[0]
        g = input_image.getpixel((width-1-i, height-1))[1]
        b = input_image.getpixel((width-1-i, height-1))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])


        r = input_image.getpixel((0, i))[0]
        g = input_image.getpixel((0, i))[1]
        b = input_image.getpixel((0, i))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-1, i))[0]
        g = input_image.getpixel((width-1, i))[1]
        b = input_image.getpixel((width-1, i))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((0, height-1-i))[0]
        g = input_image.getpixel((0, height-1-i))[1]
        b = input_image.getpixel((0, height-1-i))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])

        r = input_image.getpixel((width-1, height-i-1))[0]
        g = input_image.getpixel((width-1, height-i-1))[1]
        b = input_image.getpixel((width-1, height-i-1))[2]
        if [r, g, b] not in avg_pixel:
            avg_pixel.append([r, g, b])
    return avg_pixel

#inp = input("Enter image: ")
#input_image = Image.open(inp)


input_image = Image.open("shit.png")
width, height = input_image.size
pixel_map = input_image.load()

a = 0
b = 0
c = 0

anchor_pixel = input_image.getpixel((0, 0))

i = 0
l = 0
finder = 0
sample_size = 50
avg_pixel = back_pixels(input_image, sample_size)
for i in range(width):
    for j in range(height):
        r = input_image.getpixel((i, j))[0]
        g = input_image.getpixel((i, j))[1]
        b = input_image.getpixel((i, j))[2]
        if [r,g,b] in avg_pixel:
                continue
        else:
            Color = [a,b,c]
            Color[0] = random.randint(0,255)
            Color[1] = random.randint(0,255)
            Color[2] = random.randint(0,255)
            pixel_map[i, j] = (Color[0], Color[1], Color[2])


input_image.save("deez.png")
input_image.show()

"""
aaa
Test based on image with monocolor background:

time without if statements checking if pixel already in array: ~19s
time with if statements checking if pixel already in array: ~11s

"""
