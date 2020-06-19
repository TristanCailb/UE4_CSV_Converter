from os import listdir, path
from os.path import isfile, join, splitext

# Get UE4 string tables path to convert : Current script path + /Tables
inputPath = path.dirname(path.abspath(__file__)) + "/Input/"
outputPath = path.dirname(path.abspath(__file__)) + "/Output/"
# Get all CSV files in the directory
csvFiles = [f for f in listdir(inputPath) if isfile(join(inputPath, f)) and splitext(f)[1] == ".csv"]
newFileSuffix = "_Processed.csv"

def convertUeToExcel():
    """ Convert CSV exported file from UE4 String Tables to a CSV file readable by Excel """
    # walk through each csv file
    for f in csvFiles:
        # Get file name without extension
        fName = splitext(f)[0]
        try:
            # Open and read current file (UE4 use UTF-16 LE encoding)
            try:
                file = open(join(inputPath, f), "r", encoding="utf-16le")
                fContent = file.read()
            except:
                file = open(join(inputPath, f), "r", encoding="utf8")
                fContent = file.read()

            # Split each line of the file
            lines = fContent.split("\n")

            # Create new csv file (encoding to UTF-8 to be readable by Excel)
            newF = open(join(outputPath, fName + newFileSuffix), "w", encoding="utf8")

            # Replace first "," by ";" in each line
            for l in lines:
                newLine = l.replace(',', ';', 1) + '\n'
                newF.write(newLine)

            # Close files
            file.close()
            newF.close()

            # File created message
            print("[+] " + fName + newFileSuffix + " created in Output folder.")
        except Exception as e:
            print('[-] An error occured: ' + e)
            quit()

def convertExcelToUe():
    """ Convert CSV exported file from Excel to a CSV file readable by UE4 for String Tables """

    for f in csvFiles:
        fName = splitext(f)[0]

        try:
            file = open(join(inputPath, f), "r", encoding="utf8")
            fContent = file.read()

            lines = fContent.split("\n")

            newF = open(join(outputPath, fName + newFileSuffix), "w", encoding="utf-16le")

            for l in lines:
                newLine = l.replace(';', ',', 1) + '\n'
                newF.write(newLine)

            # Close files
            file.close()
            newF.close()

            # File created message
            print("[+] " + fName + newFileSuffix + " created in Output folder.")
        except Exception as e:
            print('[-] An error occured: ' + e)
            quit()

def banner():
    print(r"""
 _____ _____ ___    _____ _____    _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|  |  |   __| | |  |   __|_   _|  |     |     |   | |  |  |   __| __  |_   _|   __| __  |
|  |  |   __|_  |  |__   | | |    |   --|  |  | | | |  |  |   __|    -| | | |   __|    -|
|_____|_____| |_|  |_____| |_|    |_____|_____|_|___|\___/|_____|__|__| |_| |_____|__|__|
    
Made By Tristan Cailbourdin

    """)

def menu():
    print("    1. Convert from UE4 String Table CSV to Excel CSV")
    print("    2. Convert from Excel CSV to UE4 String Table CSV")
    print("    3. Exit")

    try:
        choice = int(input("Choice: "))
        if choice == 1:
            convertUeToExcel()
        elif choice == 2:
            convertExcelToUe()
        elif choice == 3:
            quit()
    except Exception as e:
        print("Error: " + e)
        quit()

# Main programme
banner()
menu()