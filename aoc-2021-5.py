
counter = 0
codes = (0, 9, 5, 9, 8, 0, 0, 8, 9, 4, 3, 4, 2, 2, 2, 1, 7, 0, 7, 4,6, 4, 2, 0, 0, 9, 2, 9, 3, 4, 1, 4, 0, 0, 8, 8, 5, 5, 8, 2,)

def grab4():
    global counter
    # counter = global counter
    coords = (codes[counter], codes[counter+1], codes[counter+2], codes[counter+3])
    print(coords)
    if coords[0]==coords[2] or coords[1]==coords[3]:
        print ("vert or hori")

    counter = counter + 4

while counter < len(codes):
    print(counter)
    grab4()
# grab4()
