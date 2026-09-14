import csv

def openfile():
    #creat a empty list
    data = []
    #open data file
    with open("/Users/sheringelbert/Library/CloudStorage/OneDrive-Personal/Uni Maastricht/5. semester/Programming/life-expectancy/life-expectancy.csv", "r") as infile:
        reader = csv.reader(infile)
        # Skip first line (header)
        next(reader)  
        #define how the data is displayed in the file
        for row in reader:
            country, id, time, expectation = row

            time = float(time)
            expectation = float(expectation)

            data.append((country, id, time, expectation))

    # return data so atht the list can be used for further calculations    
    return data


openfile()