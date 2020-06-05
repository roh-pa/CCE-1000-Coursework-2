#!/usr/bin/env python
#Authors:
#Rohini Paligadu M00696984
#Julia Estelle Perrine M00682697

from random import randint
import opc
import time
import random
import sys
from pyfirmata import Arduino, util

#connect arduino to python
board = Arduino('COM5')
time.sleep(1)
it = util.Iterator(board)
it.start()
time.sleep(2)
#define analog pin where potentiometer is connected
#To use analog ports, it is probably handy to start an iterator thread.
#Otherwise the board will keep sending data to your serial, until it overflows 

#defining variables 
numLEDs = 360
client = opc.Client('localhost:7890')

blue = [(0,0,255)]*numLEDs
black = [ (0,0,0) ] * numLEDs
white = [ (255,255,255) ] * numLEDs
green = [(0,255,0)]* numLEDs
orange = [(255,128,0)]* numLEDs
red = [(255,0,0)]* numLEDs
pink = [(255,153,255)]* numLEDs
light_orange = [(1,190,200)]* numLEDs
dark_orange = [(18,255,255)]* numLEDs
yellow = [(0,255,255)]* numLEDs

#use potentiometer to control brightness of leds
def potentiometerLED():    

    a0 = board.get_pin('a:0:i')#input from A0    
    time.sleep(1)
    print("Use the potentiometer to adjust the brighness of the LEDs")

    for x in range (0, 1000):
        time.sleep(0.01)
        potValue = a0.read() #read value from potentiometer
        print(potValue)
        potValue = int(potValue*255.9)            
        led_colour=[(potValue,potValue,potValue)]*360
        client.put_pixels(led_colour)
        client.put_pixels(led_colour)
                                       
                       
#colour switch
def switchColour():
        timeout = 15 #seconds
        timeout_start = time.time()
        #loop runs for 15s
        try:
                while time.time() < timeout_start + timeout:
                        time.sleep(0.05) #lower cpu usage
                        client.put_pixels(black)
                        time.sleep(0.5)
                        client.put_pixels(white)
                        time.sleep(0.5)
                        client.put_pixels(red)
                        time.sleep(0.5)
                        client.put_pixels(blue)
                        time.sleep(0.5)
                        client.put_pixels(yellow)
                        time.sleep(0.5)
                        client.put_pixels(green)
                        time.sleep(0.5)
                        client.put_pixels(pink)
                        time.sleep(0.5)
                        client.put_pixels(light_orange)
                        time.sleep(0.5)
                        client.put_pixels(dark_orange)
                        time.sleep(0.5)
                        led_colour=[(0,0,0)]*360
                        time.sleep(0.5)
                        led_colour=[(100,75,75)]*360
                        print (led_colour)
        except KeyboardInterrupt:
                print("Interrupt detected. . .exiting")
        except RuntimeError:
                print("An error has occurred. Restart.")
        except:
                print("Something went wrong. Please try again.") #end of switchColour

#print leds horizontally
def diagonalHorizontal():
        led_colour=[(0,0,0)]*360
        client.put_pixels(led_colour)
        timeout = 30 #seconds
        timeout_start = time.time()
        #loop runs for 30s
        try:
                while time.time() < timeout_start + timeout:
                        
                        time.sleep(0.05)
                        for x in range (0,10) :
                                red  = random.randint(0,0)
                                green = random.randint(0,0)
                                blue = random.randint(245,256)
                                led_colour[x]=(red,green,blue)
                                time.sleep(0.05)
                                print(led_colour[x])
                                client.put_pixels(led_colour)
                                client.put_pixels(led_colour)
                                
                        time.sleep(0.05)               
                        for x in reversed (range (71,81)) :
                                red  = random.randint(0,0)
                                green = random.randint(200,256)
                                blue = random.randint(0,0)
                                led_colour[x]=(red,green,blue)
                                time.sleep(0.05)
                                print((red,green,blue))
                                client.put_pixels(led_colour)
                                client.put_pixels(led_colour)

                        time.sleep(0.05)
                        for x in range (141,151) :
                                red  = random.randint(20,200)
                                green = random.randint(0,0)
                                blue = random.randint(0,0)
                                led_colour[x]=(red,green,blue)
                                time.sleep(0.05)
                                print((red,green,blue))
                                client.put_pixels(led_colour)
                                client.put_pixels(led_colour)

                        time.sleep(0.05)
                        for x in  reversed (range (211,221)) :
                                red  = random.randint(210,230)
                                green = random.randint(0,32)
                                blue = random.randint(0,200)
                                led_colour[x]=(red,green,blue)
                                time.sleep(0.05)
                                print((red,green,blue))
                                client.put_pixels(led_colour)
                                client.put_pixels(led_colour)

                        time.sleep(0.05)
                        for x in range (281,291) :
                                red  = random.randint(0,250)
                                green = random.randint(20,67)
                                blue = random.randint(0,255)
                                led_colour[x]=(red,green,blue)
                                time.sleep(0.05)
                                print((red,green,blue))
                                client.put_pixels(led_colour)
                                client.put_pixels(led_colour)

                        time.sleep(0.05)
                        for x in  reversed (range (351,360)) :
                                red  = random.randint(0,200)
                                green = random.randint(0,245)
                                blue = random.randint(255,256)
                                led_colour[x]=(red,green,blue)
                                time.sleep(0.05)
                                print((red,green,blue))
                                client.put_pixels(led_colour)
                                client.put_pixels(led_colour)
                        
        except KeyboardInterrupt:
                print("Interrupt detected. . .exiting")
        except RuntimeError:
                print("An error has occurred. Restart.")
        except:
                print("Something went wrong. Please try again.") #end of diagonalHorizontal

#shuffling red, blue and green leds
def runningLightsRandom():
        timeout = 10 #seconds
        timeout_start = time.time()
        #loop runs for 10s
        try:
                while time.time() < timeout_start + timeout:
                        led_colour=[(0,0,0)]*360
                        print (led_colour)
                        time.sleep(0.01)
                        led_colour = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]*360
                        time.sleep(0.02)
                        random.shuffle(led_colour)# changes position of item in a list
                        client.put_pixels(led_colour)
                        print(led_colour)
                        time.sleep(0.02)
        except KeyboardInterrupt:
                print("Interrupt detected. . .exiting")
        except RuntimeError:
                print("An error has occurred. Restart.")
        except:
                print("Something went wrong. Please try again.") #end of runningLightsRandom

def randomColour():
        #print random colours
        led_colour=[(255,255,255)]*360
        client.put_pixels(led_colour)

        try:
                time.sleep(0.01)
                for x in range (0,360) :
                        red  = random.randint(0,256)
                        green = random.randint(0,256)
                        blue = random.randint(0,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)
                time.sleep(0.01)
                for x in reversed(range(0,360)) :
                        red  = random.randint(0,256)
                        green = random.randint(0,256)
                        blue = random.randint(0,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)
                time.sleep(0.01)
                for x in reversed(range(0,360)) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(0,0)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)
                time.sleep(0.01)

                led_colour=[(0,0,0)]*360
                client.put_pixels(led_colour)
        except KeyboardInterrupt:
                print("Interrupt detected. . .exiting")
        except:
                print("Something went wrong. Please try again.") #end of randomColour


#MESSAGE: print HI USER
def helloUser():
        led_colour=[(0,0,0)]*360
        client.put_pixels(led_colour)

        try:
                time.sleep(0.01)
                for x in range (0,60) :
                        red  = random.randint(255,256)
                        green = random.randint(90,100)
                        blue = random.randint(90,100)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in reversed (range (0,60)) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(0,0)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                #H
                time.sleep(0.01)
                for x in range (301,302) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(255,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (241,242) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(255,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (181,182) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(255,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (121,122) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(255,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (61,62) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(255,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (306,307) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(255,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (246,247) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(255,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (181,187) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(255,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)
                                
                time.sleep(0.01)
                for x in range (126,127) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(255,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                #H
                time.sleep(0.01)
                for x in range (66,67) :
                        red  = random.randint(0,0)
                        green = random.randint(0,0)
                        blue = random.randint(255,256)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (69,76) :
                        red  = random.randint(240,256)
                        green = random.randint(0,0)
                        blue = random.randint(0,0)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (72,73) :
                        red  = random.randint(240,256)
                        green = random.randint(0,0)
                        blue = random.randint(0,0)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (132,133) :
                        red  = random.randint(240,256)
                        green = random.randint(0,0)
                        blue = random.randint(0,0)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (192,193) :
                        red  = random.randint(240,256)
                        green = random.randint(0,0)
                        blue = random.randint(0,0)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (252,253) :
                        red  = random.randint(240,256)
                        green = random.randint(0,0)
                        blue = random.randint(0,0)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)

                time.sleep(0.01)
                for x in range (315,316) :
                        red  = random.randint(240,256)
                        green = random.randint(0,0)
                        blue = random.randint(0,0)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        
                time.sleep(0.01)
                for x in range (309,316) :
                        red  = random.randint(240,256)
                        green = random.randint(0,0)
                        blue = random.randint(0,0)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)

                #print USER
                #U
                for x in range (325,330) :
                        red  = random.randint(2,10)
                        green = random.randint(234,245)
                        blue = random.randint(234,250)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)

                        red  = random.randint(2,10)
                        green = random.randint(234,245)
                        blue = random.randint(234,250)
                        led_colour[264]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[270]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[204]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[210]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[144]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[150]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[84]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[90]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        

                #S
                for x in range (93,99) :
                        red  = random.randint(255,255)
                        green = random.randint(100,100)
                        blue = random.randint(100,100)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                for x in range (213,219) :
                        red  = random.randint(255,255)
                        green = random.randint(100,100)
                        blue = random.randint(100,100)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                for x in range (333,339) :
                        red  = random.randint(255,255)
                        green = random.randint(100,100)
                        blue = random.randint(100,200)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[153]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[278]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                #E
                for x in range (101,108) :
                        red  = random.randint(255,255)
                        green = random.randint(0,0)
                        blue = random.randint(199,200)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                                
                for x in range (221,228) :
                        red  = random.randint(255,255)
                        green = random.randint(0,0)
                        blue = random.randint(199,200)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        
                for x in range (341,348) :
                        red  = random.randint(255,255)
                        green = random.randint(0,0)
                        blue = random.randint(199,200)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[161]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        led_colour[281]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)

                #R
                for x in range (111,116) :
                        red  = random.randint(0,0)
                        green = random.randint(100,100)
                        blue = random.randint(199,200)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        
                for x in range (231,236) :
                        red  = random.randint(0,0)
                        green = random.randint(100,100)
                        blue = random.randint(199,200)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)

                led_colour[176]=(red,green,blue)
                time.sleep(0.01)
                print((red,green,blue))
                client.put_pixels(led_colour)
                led_colour[296]=(red,green,blue)
                time.sleep(0.01)
                print((red,green,blue))
                client.put_pixels(led_colour)
                led_colour[358]=(red,green,blue)
                time.sleep(0.01)
                print((red,green,blue))
                client.put_pixels(led_colour)
                led_colour[171]=(red,green,blue)
                time.sleep(0.01)
                print((red,green,blue))
                client.put_pixels(led_colour)
                led_colour[231]=(red,green,blue)
                time.sleep(0.01)
                print((red,green,blue))
                client.put_pixels(led_colour)
                led_colour[351]=(red,green,blue)
                time.sleep(0.01)
                print((red,green,blue))
                client.put_pixels(led_colour)
                led_colour[291]=(red,green,blue)
                time.sleep(0.01)
                print((red,green,blue))
                client.put_pixels(led_colour)

                for x in range (0,60) :
                        red  = random.randint(255,256)
                        green = random.randint(90,100)
                        blue = random.randint(90,100)
                        led_colour[x]=(red,green,blue)
                        time.sleep(0.01)
                        print((red,green,blue))
                        client.put_pixels(led_colour)
                        client.put_pixels(led_colour)

                time.sleep(0.01)

                #make HI USER blink
                client.put_pixels(led_colour)
                client.put_pixels(black)
                time.sleep(0.5)
                client.put_pixels(led_colour)
                time.sleep(0.5)
                client.put_pixels(black)
                time.sleep(0.5)
                client.put_pixels(led_colour)
                time.sleep(0.5)
                client.put_pixels(black)
                time.sleep(0.5)
                client.put_pixels(led_colour)
                time.sleep(0.5)
                client.put_pixels(black)
                time.sleep(0.5)
                client.put_pixels(led_colour)
        except KeyboardInterrupt:
                print("Interrupt detected. . .exiting")
        except:
                print("Something went wrong. Please try again.") #end of helloUser

#menu to choose from animation
def userInput():
        userInput = int(input("""Press 1 to SWITCH COLOURS,
        Press 2 for HORIZONTAL AND DIAGONAL ANIMATION, 
        Press 3 for RANDOM COLOUR ANIMATION,
        Press 4 to PRINT "HI USER",
        Press 5 to SHUFFLE COLOURS
        Press 6 to CHANGE THE BRIGHTNESS OF THE LEDS BY USING A POTENTIOMETER,
        Press 7 to EXIT : """))
        if(userInput == 1):
                switchColour() 
        if(userInput == 2):
                diagonalHorizontal()    
        if(userInput == 3):
                randomColour()
        if(userInput == 4):
                 helloUser()
        if(userInput == 5):
                 runningLightsRandom()
        if(userInput == 6):
                 potentiometerLED()
        if(userInput == 7):
                print("Quit")
                sys.exit(0)
        if((userInput > 7) or (userInput < 1) ):
                print("\nINVALID CHOICE")
                

#Main to test
if __name__ == "__main__":
    while True:
        try:
                userInput()
        except ValueError:
                print("Error. Please enter a number between 1 and 6 ")
                userInput()
        except:
                print("An error occured. Please try again. ")
                userInput()





        
