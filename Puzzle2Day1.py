""" Brennan Link
Advent of code puzzle two day one """

def main():
    # import numpy and itertools,
    # as we'll want to make quick work of grabbing our values from a text file
    # as well as cycling through our values
    import numpy as np
    import itertools

    # set our initial variables
    values = []
    frequency = 0
    seen = set([0])

    # get our list of values from our textfile, and put them into our array as ints.
    values = np.genfromtxt('puzzleinput/puzzleinput.txt', autostrip=True, unpack=True, dtype=np.int)

    # Loop through each value in the array, and for each value, add or subtract from our eventual total
    # we're also checking per each loop in an attempt to find our matching number... 
    for value in itertools.cycle(values):
        frequency += value
        if frequency in seen:
            print frequency 
            break
        seen.add(frequency)

#finally, run our stuff
if __name__ == '__main__':
    main()

