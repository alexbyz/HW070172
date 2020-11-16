import regex

recordIdealtype = {
    "recodType": "recordType",
    "citationKey": "citationKey",
    "title": "title",
    "author": "author",
    "date": "date",
    "location": "location"
}

record = {}

def readFile():     #reads in the file
    infile = input("inputfile: ")
    infile = open(infile, "r", encoding="UTF-8")
    
    data =""    #string to read the file into

    for line in infile:
        data = data + line
    return data

def getRecords(inString):    #splits the long string along '\n@'
    return inString.split("\n@")

def main():   

    data = readFile()
    records = getRecords(data)    
    
    for i in range(len(records)):   #loops throug the records   

        entry = records[i].split(',\n')
        #print(entry)
        firstEntry = entry[0].split('{')
        recordType = firstEntry[0].strip()
        citationKey = firstEntry[1].strip()
        record["recodType"] = recordType
        record["citationKey"] = citationKey

        for x in range(1,len(entry)-1,1):
            key, value = entry[x].split("=")
            #print(key,"\t", value)            
            if key.strip() in recordIdealtype:
                record[key] = value             
        print(record)        
    
main()