import os
import sys
import string
import csv

def num(s):
    try:
        return int(s)
    except ValueError:
        return -1

rails_max = 45904
django_max = 10346
if __name__ == '__main__':
    #creates file named temp.dot
    #argv[0] is the file
    #argv[1] is the csv
    number_max = 0
    if (len(sys.argv) == 2):
        commitsfile = sys.argv[1]
        #open commits to read
        with open(commitsfile) as f:
            #for each month aka a line in commits file
            for month in f:
                file = ""
                date = ""
                files = month.split("|")
                for s in range(0,len(files)):
                    if (s == 0):
                        temp = files[s].split(" month ago ")
                        date = temp[0]
                        if (len(temp) > 1):
                            file = temp[1]
                    else:
                        temp = files[s].split(" ")
                        if (temp[1] != "Bin"):
                            number = num(temp[1])
                            if (number > number_max):
                                number_max = number
                            if (number == -1):
                                #something went wrong with the parser
                                print("debug stuff: ")
                                print(temp)
                        #put in csv here
                        filename = temp[3]
                        continue
        print("max number is " + str(number_max))
