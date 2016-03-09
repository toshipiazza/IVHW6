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

rails_max = 405662.0
django_max = 520017.0
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
        with open('djangodata.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile)
            with open(commitsfile) as f:
                #for each month aka a line in commits file
                for month in f:
                    file = ""
                    date = ""
                    filename = ""
                    extensions = {}
                    files = month.split("|")
                    for s in range(0,len(files)):
                        if (s == 0):
                            temp = files[s].split(" month ago ")
                            if (len(temp) > 1):
                                filename = temp[1]
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
                                if (number == -1):
                                    #something went wrong with the parser
                                    print("debug stuff: ")
                                    print(temp)
                                if (filename == ""):
                                    filename = files[s-1].split(" ")[2]
                                filename, ext = os.path.splitext(filename)
                                if (ext == ""):
                                    if (filename != ""):
                                        ext = os.path.basename(os.path.normpath(filename))
                                if (extensions.has_key(ext)):
                                    number = extensions[ext] + number
                                    extensions[ext] = number
                                    if (number > number_max):
                                        number_max = number
                                else:
                                    extensions.setdefault(ext, [])
                                    extensions[ext] = (number)
                                if (number == 0):
                                    filename = temp[2]

                                else:
                                    filename = temp[3]

                            else:
                                #dont record anything
                                filename = temp[6]
                                continue
                            continue

                    for key in extensions:
                        #put in csv here
                        formatted_number = str("{0:.3f}".format(extensions[key]/django_max))
                        spamwriter.writerow([key,formatted_number,date])
        print("max number is " + str(number_max))
