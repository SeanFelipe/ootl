x_increment = 160
y_increment = 160




xygrid = []   # square brackets are Python lists

for i in range(2):
    for j in range(3):
        circley = (i + 1) * y_increment
        circlex = (j + 1) * x_increment
        xygrid.append((circlex, circley))

#print xygrid


for pair in xygrid:
    print pair
