import numpy as np
import os
import subprocess

width = 64

def get_svg(color, shape):

    svghead = '<svg height="{}" width="{}">'.format(width,width)
    svgtail = '</svg>'
    
    if shape == "circle":
        r = np.random.randint(width/2-20)+10
        cx = np.random.randint(r, width-r)
        cy = np.random.randint(r, width-r)
        svgcenter = '<circle cx="{}" cy="{}" r="{}" fill="{}" />'.format(cx,cy,r,color)

    elif shape == "square":

        r = np.random.randint(width/2-10)+5
        cx = np.random.randint(0, width-r*2)
        cy = np.random.randint(0, width-r*2)
        svgcenter = '<rect x="{}" y="{}" width="{}" height="{}" fill="{}"/>'.format(cx,cy,r*2,r*2,color)

    return svghead + svgcenter + svgtail

folder = "shapes-dataset"
if not os.path.exists(folder): 
    os.mkdir(folder)

for color in ["green", "red","blue"]:
    for shape in ["square", "circle"]:
        
        subfolder = folder + "/" + shape + "-" + color
        if not os.path.exists(subfolder): 
            os.mkdir(subfolder)
        
        for i in range(0,10):

            svg = get_svg(color, shape)
            f = open('test.svg', 'w+')
            f.write(svg)
            f.flush()
            
            params = ['convert', 'test.svg', subfolder + "/" + str(i) + ".png"]
            subprocess.check_call(params)
