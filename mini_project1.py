import os
import csv
import json

FileNames = []
CamelCount = []
def main():
    collect_all_csv_filenames()
    read_csv()
    write_data()
    print(str(len(CamelCount)) + " teams are CamelCase")


def collect_all_csv_filenames():
#creating everyone.csv file
    if os.path.isfile(os.getcwd() + "/everyone.csv") == False:
        every = open('everyone.csv', 'a')
        for filename in os.listdir(os.getcwd()):
            if filename.endswith("csv") and filename != "mlp6.csv" and filename != "ejc40.csv" \
                    and filename != "as553.csv" and filename != "ttw6.csv" and filename!= "everyone.csv":
                with open(filename) as csvDataFile:
                    csvReader = csv.reader(csvDataFile)
                    for row in csvReader:
                        every.write(str(row)+ "\n")
        every.close()





def read_csv():
    for filename in os.listdir(os.getcwd()):
        #Threw out csv files below in addition to mlp6 because they were multiple lines and/or empty
        if filename.endswith("csv") and filename != "mlp6.csv" and filename != "ejc40.csv" \
                and filename != "as553.csv" and filename != "ttw6.csv" and filename!= "everyone.csv":
            FileNames.append(filename)
            check_no_spaces(filename)
            check_camel_case(filename)



def write_data():
    fieldnames = ("FirstName", "LastName", "NetID", "Github", "Teamname")

    for filename in os.listdir(os.getcwd()):
        if filename.endswith("csv") and filename != "mlp6.csv" and filename != "everyone.csv":
            csvfile = open(filename, 'r')
            jsonf = filename[:-3]
            jsonfile = open(jsonf + 'json', 'w')
            reader = csv.DictReader(csvfile, fieldnames)
            for row in reader:
                json.dump(row, jsonfile)
                jsonfile.write('\n')
            jsonfile.close()
            csvfile.close()



def check_no_spaces(filename):
        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                if " " in row[4]:
                    print(filename + " has a space in the team name")


def check_camel_case(filename):
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if row[4] != row[4].lower() and row[4] != row[4].upper():
                global CamelCount
                if row[4] not in CamelCount:
                    CamelCount.append(row[4])



if __name__ == "__main__":
    main()
