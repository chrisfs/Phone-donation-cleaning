#import pandas
import csv
def phone(orig):
    test =orig.replace("-","")
    test = test.replace("(","")
    return test
def email(orig):
    if orig.find("@") == -1:
        orig = ""
    return orig
def checkprem(orig):
    if orig == "":
        return orig
    if orig == ' ""':
        return orig
    if len(orig)==3:
        orig = "171"+orig
        return orig
    return orig

infile = open("DailyReport.csv","r",encoding='windows-1252')
InfileReadObj = csv.reader(infile,quoting=csv.QUOTE_ALL)
next(InfileReadObj)
outfile = open("outfile.csv","w", newline='')
outfileWriteObj = csv.writer(outfile,quoting=csv.QUOTE_ALL)
n=1
#n is line number for printing errors in data
for row in InfileReadObj:
    pledge = row
    #print(pledge[43])
    #print(len(pledge[43]))
    #take non numbers out of phone number 
    newphone = phone(pledge[15])
    pledge[15]=newphone
    newphone = phone(pledge[16])
    pledge[16]=newphone
    #remove bad emails
    newemail = email(pledge[17])
    pledge[17]=newemail

    #check prems for 6 digts
    for i in (43,44,56,57,58):
        newprem =checkprem(pledge[i])
        pledge[i]=newprem

    #check for entering prem numbers in quantity field
    for i in (59,60,61,62,63):
        if pledge[i].isdigit():
            if int(pledge[i]) > 99:
                print("Prem quantity err line "+str(n))
            
                        
    outfileWriteObj.writerow(pledge)
    #print(n)
    #print(pledge[43])
    n=n+1
infile.close()
outfile.close()    

