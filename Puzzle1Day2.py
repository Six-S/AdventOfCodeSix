""" Brennan Link
Advent of Code Day Two Puzzle One """

def main():
    # Let's define some variables that we can mess with
    #values = []
    fileToRead = open("puzzleinput/puzzleinput2.txt", "r")

    #now that we have a file open, let's read the file, and split as we do it.
    codes = fileToRead.read().split()

    # print codes

    for code in codes:
        breakdown = list(code)
        print breakdown


if __name__ == "__main__":
    main();