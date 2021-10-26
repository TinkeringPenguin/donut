#! /usr/bin/env python3

import os,time
from math import sin, cos,pi
from numba import njit


def main(speed):
    a=0
    b=0

    fps,rate,=0,0
    print("\x1b[2J",end="")
    # for clearing console (windows and unix systems)
    clear = lambda: os.system("cls")
    if os.name == "posix":
        clear = lambda :print("\x1bc",end="")

    clear()
    @njit
    def faster(a,b,scale):
        height=int(24*scale)
        width=int(80*scale)
        buf=""

        z = [0 for _ in range(4*height*width)]
        screen = [' ' for _ in range(height*width)]
        j=0
        while j<pi*2:
            j+=0.07
            i=0
            while i<pi*2:
                i+=0.02

                sinA=sin(a)
                cosA=cos(a)
                cosB=cos(b)
                sinB=sin(b)

                sini=sin(i)
                cosi=cos(i)
                cosj=cos(j)
                sinj=sin(j)

                cosj2=cosj+2
                mess=1/(sini*cosj2*sinA+sinj*cosA+5)
                t=sini*cosj2*cosA-sinj* sinA

                # 40 is the left screen shift
                x = int(scale*40+scale*30*mess*(cosi*cosj2*cosB-t*sinB))
                # 12 is the down screen shift
                y = int(scale*11+scale*15*mess*(cosi*cosj2*sinB +t*cosB))
                # all are casted to int, ie floored
                o = int(x+width*y)
                # multiplying by 8 to bring in range 0-11 as 8*(sqrt(2))=11
                # because we have 11 luminance characters
                N = int(8*((sinj*sinA-sini*cosj*cosA)*cosB-sini*cosj*sinA-sinj*cosA-cosi *cosj*sinB))
                # if x,y inside screen and previous z-buffer is < mess 
                # i.e. when z[o] is 0 or the prev point is behind the new point
                # so we change it to the point nearer to the eye/ above prev point 
                if 0<y<height and 0<x<width and z[o] < mess:
                    z[o]=mess
                    screen[o]=".,-~:;=!*#$@"[N if N>0 else 0]

        for index, char in enumerate(screen):
            if index % width == 0:
                buf+="\n"
            else:
                buf+=char
        return(buf)

    while True:
        try:
            before=time.time()
            # Automatically adjust Donut scale according to terminal size

            scale=min(os.get_terminal_size().lines/24,os.get_terminal_size().columns/80)*0.9
            print(f"|{fps}|",end="")
            
            print(faster(a,b,scale),end='')
            fps=round(1/(time.time()-before),1)

            #Keep speed of spinning constant as 
            rate=100*speed/fps
            
            clear()
            
            # increments with speed
            a+=0.04*rate
            b+=0.02*rate

        except KeyboardInterrupt:
            # print(faster(a,b,scale),end='')
            print("")
            exit()


if __name__ =="__main__":
    main(speed=0.3)