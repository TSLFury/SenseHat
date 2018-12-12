sense = SenseHat()

for i in range(1,6):
    sense.show_letter( str(i) )
    sleep(1)

for i in range(5, -1, -1):
    sense.show_letter( str(i) )
    sleep(1)

sense = SenseHat()

G =[0, 255, 0]

for i in range(5, -1, -1):
    sense.show_letter( str(i), G)

sense = SenseHat()

G = [0, 255, 0]
R = [255, 0, 0]
B = [255, 0, 255]

for i in range(5, -1, -1):
    sense.show_letter( str(i), R)
    sleep(1) 
