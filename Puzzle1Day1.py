""" Brennan Link
Advent of code puzzle one day one """

def main():
    #import numpy as we'll want to make quick work of grabbing our values from a text file
    import numpy as np

    #set our initial variables, and in the case of total, a starting value of zero
    values = []
    total = 0

    #get our list of values from our textfile, and put them into our array as ints.
    values = np.genfromtxt('puzzleinput/puzzleinput.txt', autostrip=True, unpack=True, dtype=np.int)
    #print values

    #Loop over each value in the array, and for each value, add or subtract from our eventual total
    for (i, value) in enumerate(values):
        print i, value
        total += value
        print "OUR SUM CHANGED, AND IS NOW: %s" % total

    print 'OUR TOTAL IS: %s' % total

#run our stuff
if __name__ == '__main__':
    main()

