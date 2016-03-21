#draw random houndstooth picasso art

import random
import PIL
from PIL import Image, ImageDraw

def generate_coord():
    xy_coord = []
    for i in range(2):
        xy_coord.append(random.randint(75,675))
    xy_coord = tuple(xy_coord)
    return xy_coord

def generate_list_coords(points):
    list_coords = []
    for coord in range(points):
        xy_coord = generate_coord()
        list_coords.append(xy_coord)
    return list_coords

def generate_color():
    rgb = []
    for value in range(3):
        rgb.append(random.randint(0,255))
    rgb = tuple(rgb)
    return rgb

def draw_lines(points,draw,im,color):
    list_coords = generate_list_coords(points)
    print("RGB",color)
    draw.polygon(list_coords, fill=color)
    im.show()

def create_image(points,color):
    im = Image.new("RGB", (750,750), (255,255,255))
    draw = ImageDraw.Draw(im)
    draw_lines(points,draw,im,color)

def main():
    points = 40
    #rgb_input = "#" + input("What color in hex code? (#rrggbb) #")
    rgb_random = generate_color()
    create_image(points,rgb_random)
    
main()
    
