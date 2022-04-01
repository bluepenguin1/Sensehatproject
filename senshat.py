from sense_hat import SenseHat
from time import sleep, strftime #provides date/time formatted as a string

sense = SenseHat()

#Data

colors = {
    
    'r': [255, 0, 0],
    'n': [135, 80, 22],
    'w': [255, 255, 255],
    'e': [0, 0, 0], #e stands for empty/black
    'y': [255, 255, 0],
    'g': [0, 128, 0],
    'b': [0, 0, 255],
    'i': [75, 0, 130],
    'v': [143, 0, 255]    
    
    
}


# Pictures
with open("/home/pi/Pictures/pictures.txt", "r") as f: #opens pictures.txt file in read mode
    all_pics = f.readlines() #reads whole file into a list called all pics, each line of the file then becomes one item in list 
    
    
def display_pic(pic_string):
    
    # Get rid of newline and split the line into a list
    pic_string = pic_string.strip("\n")
    pic_string = pic_string.split(",")
    
    #Look up each letter in the dictionary 
    pic_list = []
    for letter in pic_string:
        pic_list.append(colors[letter])

    sense.set_pixels(pic_list)

door = all_pics[1]

#Main Program

while True: 

    sense.clear()
    display_pic(all_pics[7])

    day = int(strftime("%d")) # Results in '23' , 
    month = strftime("%d/%m/%y") # Results in 'October'
    whole_date = strftime("%d/%m/%y") #Results in '23/10/17'

    event = sense.stick.wait_for_event()
    if event.action == "pressed" and event.direction == "middle":
        today = int(strftime("%d"))
        month = strftime("%B")

    if month == 'December' and day < 25:
        sense.show_message(str(day)) # convert day to a string
        display_pic(all_pics[day])
        sleep(5)

display_pic(pic_string)
