import os
import sys
import string
import csv
import math

def num(s):
    try:
        return int(s)
    except ValueError:
        return -1

rails_max = 45904.0
django_max = 10346.0
current_month = 3
current_year = 16
current_day = "10"

if __name__ == '__main__':
    #creates file named temp.dot
    #argv[0] is the file
    #argv[1] is the csv
    number_max = 0
    if (len(sys.argv) == 2):
        commitsfile = sys.argv[1]
        #open commits to read
        with open('djangodata.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile)
            with open(commitsfile) as f:
                #for each month aka a line in commits file
                for month in f:
                    file = ""
                    date = ""
                    files = month.split("|")
                    for s in range(0,len(files)):
                        if (s == 0):
                            temp = files[s].split(" month ago ")
                            if (len(temp) > 1):
                                file = temp[1]
                                months_ago = int(temp[0])
                                new_month = current_month - months_ago + 1
                                if (new_month <= 0):
                                    year = int(current_year - math.floor((new_month*-1) / 12) - 1)
                                    month = 12 - ((new_month*-1) % 12)
                                    date = str(month) + "/" + current_day + "/" + str(year)
                                else:
                                    date = str(new_month) + "/" + current_day + "/" + str(current_year)
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
                            filename = temp[3]
                            formatted_number = str("{0:.3f}".format(number/django_max))
                            #put in csv here
                            spamwriter.writerow([filename,formatted_number,date])
                            continue
        print("max number is " + str(number_max))
