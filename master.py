import numpy as np
from PIL import Image
import cv2 as cv
import math
import os
# os.mkdir('C:/Users/Admin/OneDrive/Documents/Prgramming/Projects/Data_set_SUAS/imag_text')
# os.mkdir('C:/Users/Admin/OneDrive/Documents/Prgramming/Projecxts/Data_set_SUAS/Images')
# def canvas(canvas_height=512,canvas_width=512):
canvas_height=200
canvas_width=200
canvas= np.zeros((canvas_height,canvas_width,3), np. uint8)
# cv.imshow('canvas',canvas)
cv.waitKey(0)
cv.imwrite('canvas.png',canvas)

def writeText(path):
    #Images\Star_trans.png
    # path = path[1:-4]
    object= cv.imread(path,cv.IMREAD_UNCHANGED)
    cv.putText(object,'F',(int(canvas_height/2),int(canvas_width/2)),cv.FONT_HERSHEY_SIMPLEX,1,(200,45,66),3)
    cv.imshow('xc',object)
    cv.waitKey(0)
    cv.imwrite('image_text'+path[1:-4]+'_Text.png', object)
    return 'image_text'+path[1:-4]+'_Text.png'


def convertImage(path):
    img = Image.open(path)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []

    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    save_path= 'Images'+path[10:-9] + "_trans.png"
    print(save_path)
    img.save(save_path, "PNG")
    print("Successful")
    return save_path


'''
Shapes!!
'''
#Circle
def circle(radius=60):
    # canvas()
    canvas= np.zeros((canvas_height,canvas_width,3), np. uint8)
    cv.circle(canvas,(int(canvas_height/2),int(canvas_width/2)), radius, (0,0,255), -1)
    cv.imshow('circle',canvas)
    cv.waitKey(0)
    cv.imwrite('circle.png',canvas)
    path = './circle.png'
    text=writeText(path)
    convertImage(text)

# circle()
#rectangle

def rectangle(length=100,width=70):
    canvas= np.zeros((canvas_height,canvas_width,3), np. uint8)
    cv.rectangle(canvas,( int(canvas_height/2-length/2),int(canvas_width/2-width/2)),(int(canvas_height/2+length/2),int(canvas_width/2+width/2)),(255,0,0),-1)
    cv.imshow('rectangle',canvas)
    cv.waitKey(0)
    cv.imwrite('rectangle.png',canvas)
    path= './rectangle.png'
    text=writeText(path)
    convertImage(text)


#Triangle
def triangle(side=100):
    canvas= np.zeros((canvas_height,canvas_width,3), np. uint8)
    pt1=(int(canvas_width/2),int(canvas_height-side/(3**(0.5))))
    pt2=(int(canvas_width/2-side/2),int(canvas_height*0.5/(3**(0.5))))
    pt3=(int(canvas_width/2+side/2),int(canvas_height*0.5/(3**(0.5))))
    triangle_cnt = np.array( [pt1, pt2, pt3] )
    cv.drawContours(canvas, [triangle_cnt], 0, (0,255,0), -1)
    cv.imshow('triangle',canvas)
    cv.waitKey(0)
    cv.imwrite('triangle.png',canvas)
    path= './triangle.png'
    text=writeText(path)
    convertImage(text)

#semicircle
def semicircle(radius=80):
    canvas= np.zeros((canvas_height,canvas_width,3), np. uint8)
    cv.ellipse(canvas, (int(canvas_height/2),int(canvas_width/2)), (radius,radius), 0, 180, 360, (00,255,255), -1)
    cv.imshow('semicircle',canvas)
    cv.waitKey(0)
    cv.imwrite("semicircle.png",canvas)
    path="./semicircle.png"
    text=writeText(path)
    convertImage(text)

def hexagone(length=50):
    canvas= np.zeros((canvas_height,canvas_width,3), np. uint8)
    a=length*0.5*(3**(0.5))
    b=length*0.5
    pt1=(int(canvas_width/2-a),int(canvas_height/2+b))
    pt2=(int(canvas_width/2),int(canvas_height/2+length))
    pt3=(int(canvas_width/2+a),int(canvas_height/2+b))
    pt4=(int(canvas_width/2+a),int(canvas_height/2-b))
    pt5=(int(canvas_width/2),int(canvas_height/2-a))
    pt6=(int(canvas_width/2-a),int(canvas_height/2-b))
    hex=np.array([pt1,pt2,pt3,pt4,pt5,pt6])
    cv.drawContours(canvas, [hex], 0, (0,255,0), -1)
    cv.imshow('Hexagon',canvas)
    cv.waitKey(0)
    cv.imwrite('Hexagon.png',canvas)
    path= './Hexagon.png'
    text=writeText(path)
    convertImage(text)

#plus
def plus(length=50):
    canvas= np.zeros((canvas_height,canvas_width,3), np. uint8)
    a=length*1.5
    b=length*0.5
    pt1=(int(canvas_width/2-a),int(canvas_height/2+b))
    pt2=(int(canvas_width/2-b),int(canvas_height/2+b))
    pt3=(int(canvas_width/2-b),int(canvas_height/2+a))
    pt4=(int(canvas_width/2+b),int(canvas_height/2+a))
    pt5=(int(canvas_width/2+b),int(canvas_height/2+b))
    pt6=(int(canvas_width/2+a),int(canvas_height/2+b))
    pt7=(int(canvas_width/2+a),int(canvas_height/2-b))
    pt8=(int(canvas_width/2+b),int(canvas_height/2-b))
    pt9=(int(canvas_width/2+b),int(canvas_height/2-a))
    pt10=(int(canvas_width/2-b),int(canvas_height/2-a))
    pt11=(int(canvas_width/2-b),int(canvas_height/2-b))
    pt12=(int(canvas_width/2-a),int(canvas_height/2-b))
    plus= np.array([pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9,pt10,pt11,pt12])
    cv.drawContours(canvas, [plus], 0, (0,255,0), -1)
    cv.imshow('Trap',canvas)
    cv.waitKey(0)
    cv.imwrite('Plus.png',canvas)
    path= './Plus.png'
    text=writeText(path)
    convertImage(text)


#Trapizium
def trap(length=100):
    canvas= np.zeros((canvas_height,canvas_width,3), np. uint8)
    a=length*0.25*(3**0.5)
    b=length*0.75
    pt1=(int(canvas_width/2-b),int(canvas_height/2-a))
    pt2=(int(canvas_width/2-length/3),int(canvas_height/2+a))
    pt3=(int(canvas_width/2+length/3),int(canvas_height/2+a))
    pt4=(int(canvas_width/2+b),int(canvas_height/2-a))
    trap= np.array([pt2,pt3,pt4,pt1])
    cv.drawContours(canvas, [trap], 0, (0,255,0), -1)
    cv.imshow('Trap',canvas)
    cv.waitKey(0)
    cv.imwrite('Trap.png',canvas)
    path= './Trap.png'
    text=writeText(path)
    convertImage(text)

#Pentagon
def pentagon(length=70):
    canvas= np.zeros((canvas_height,canvas_width,3), np. uint8)
    pt1=(int(canvas_width/2-length*math.cos(math.pi/10)),int(canvas_height/2+length*math.sin(math.pi/10)))
    pt2=(int(canvas_width/2),int(canvas_height/2+length))
    pt3=(int(canvas_width/2+length*math.cos(math.pi/10)),int(canvas_height/2+length*math.sin(math.pi/10)))
    pt4=(int(canvas_width/2+length*math.cos(3*math.pi/10)),int(canvas_height/2-length*math.sin(3*math.pi/10)))
    pt5=(int(canvas_width/2-length*math.cos(3*math.pi/10)),int(canvas_height/2-length*math.sin(3*math.pi/10)))
    pent= np.array([pt1,pt2,pt3,pt4,pt5])
    cv.drawContours(canvas, [pent], 0, (0,255,0), -1)
    cv.imshow('Pentagon',canvas)
    cv.waitKey(0)
    cv.imwrite('Pentagon.png',canvas)
    path= './Pentagon.png'
    text=writeText(path)
    convertImage(text)

#Star
def star(length=40):
    canvas= np.zeros((canvas_height,canvas_width,3), np. uint8)
    a=length*math.sin(18)/math.sin(54)*2
    pt1=(int(canvas_width/2-length*math.cos(math.pi/10)),int(canvas_height/2+length*math.sin(math.pi/10)))
    pt2=(int(canvas_width/2-a*math.cos(3*math.pi/10)),int(canvas_height/2+a*math.sin(3*math.pi/10)))
    pt3=(int(canvas_width/2),int(canvas_height/2+length))
    pt4=(int(canvas_width/2+a*math.cos(3*math.pi/10)),int(canvas_height/2+a*math.sin(3*math.pi/10)))
    pt5=(int(canvas_width/2+length*math.cos(math.pi/10)),int(canvas_height/2+length*math.sin(math.pi/10)))
    pt6=(int(canvas_width/2+a*math.cos(math.pi/10)),int(canvas_height/2-a*math.sin(math.pi/10)))
    pt7=(int(canvas_width/2+length*math.cos(3*math.pi/10)),int(canvas_height/2-length*math.sin(3*math.pi/10)))
    pt8=(int(canvas_width/2),int(canvas_height/2-a))
    pt9=(int(canvas_width/2-length*math.cos(3*math.pi/10)),int(canvas_height/2-length*math.sin(3*math.pi/10)))
    pt10=(int(canvas_width/2-a*math.cos(math.pi/10)),int(canvas_height/2-a*math.sin(math.pi/10)))
    star= np.array([pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9,pt10])
    cv.drawContours(canvas, [star], 0, (0,255,0), -1)
    cv.imshow('Star',canvas)
    cv.waitKey(0)
    cv.imwrite('Star.png',canvas)
    path= './Star.png'
    text=writeText(path)
    convertImage(text)

rectangle()
circle()
triangle()
semicircle()
hexagone()
plus()
trap()
pentagon()
star()

'''| T E X T  O N  T H E  S H A P E S |'''

# object= cv.imread('circle.png',cv.IMREAD_UNCHANGED)
# cv.putText(object,'F',(int(canvas_height/2),int(canvas_width/2)),cv.FONT_HERSHEY_SIMPLEX,1,(200,45,66),3)
# cv.imshow('xc',object)
# cv.waitKey(0)
# cv.imwrite('zz.png', object)
# convertImage('zz.png')