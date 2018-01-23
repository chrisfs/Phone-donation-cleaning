data = open("DailyReport.csv","r")
outfile = open("NewDaily.csv","w")
for line in data:
    if line[-2] != '"':
        line = line.rstrip()
    outfile.write(line)
    
data.close()
outfile.close()

