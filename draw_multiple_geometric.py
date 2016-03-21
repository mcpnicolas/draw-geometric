#draw random houndstooth picasso art (4)

import random
import PIL
from PIL import Image, ImageDraw

def generate_coord(xy_min,xy_max):
    xy_coord = []
    if len(xy_min) == 1:
        for i in range(2):
            xy_coord.append(random.randint(xy_min[0],xy_max[0]))
    else:
        xy_coord.append(random.randint(xy_min[0],xy_min[1]))
        xy_coord.append(random.randint(xy_max[0],xy_max[1]))
    xy_coord = tuple(xy_coord)
    return xy_coord

def generate_list_coords(points,xy_min,xy_max):
    list_coords = []
    for coord in range(points):
        xy_coord = generate_coord(xy_min,xy_max)
        list_coords.append(xy_coord)
    return list_coords

def generate_color():
    rgb = []
    for value in range(3):
        rgb.append(random.randint(0,255))
    rgb = tuple(rgb)
    return rgb

def hex_code_color(rgb):
    hex_color = "#"
    for color in rgb:
        hex_color_0x = hex(color)
        if len(hex(color)) == 3:
            hex_color += "0" + hex_color_0x[2:].upper()
        else:
            hex_color += hex_color_0x[2:].upper()
    return hex_color

def draw_lines(points,draw,im):
    all_coords_list = []
    list_coords_1 = generate_list_coords(points,[75],[375])
    list_coords_2 = generate_list_coords(points,[375],[675])
    list_coords_3 = generate_list_coords(points,[375,675],[75,375])
    list_coords_4 = generate_list_coords(points,[75,375],[375,675])
    all_coords_list.append(list_coords_1)
    all_coords_list.append(list_coords_2)
    all_coords_list.append(list_coords_3)
    all_coords_list.append(list_coords_4)
    for i in range(4):   
        color = generate_color()
        hex_color = hex_code_color(color)
        print(hex_color)
        draw.polygon(all_coords_list[i], fill=color)
    im.show()

def create_image(points):
    im = Image.new("RGB", (750,750), (255,255,255))
    draw = ImageDraw.Draw(im)
    draw_lines(points,draw,im)

'''
#research options for im.save()
def choose_save():
    opt = input("Save? (Y/N) ")
    if opt.islower() == 'y':
        im.save('geometric.bmp')
'''

def main():
    points = 35
    #rgb_input = "#" + input("What color in hex code? (#rrggbb) #")
    create_image(points)
    #choose_save()
    
main()
    
