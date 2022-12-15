class Date:
    """docstring for Date."""
    def __init__(self, day, month, year, hour, minute):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
    def __str__(self):
        return "Date: {}/{}/{} {}:{}".format(self.day, self.month, self.year, self.hour, self.minute)

def writeToFile(inputStr, fileDir):
    # The same with Try_Resources in java
    with open(fileDir, "w") as writter:
        writter.write(inputStr)

def readTestCaseFromFile(fileDir):
    # The same with Try_Resources in java
    with open(fileDir, "r") as reader:
        line = reader.readline()
        result = []
        while line:
            # print("Line: ", line.strip())
            splitedArr = line.strip().rsplit("=")
            match splitedArr[0]:
                case "fName" | "sName" | "id":
                    result.append(splitedArr[1])
                case "sDate" | "eDate":
                    dateArr = splitedArr[1].rsplit(",")
                    result.append(Date(dateArr[0], dateArr[1], dateArr[2], dateArr[3], dateArr[4]))
                case _:
                    print("Default Switch Case condition statement!")
            line = reader.readline()
        return result

def readSolutionFromFile(fileDir):
    # The same with Try_Resources in java
    with open(fileDir, "r") as reader:
        line = reader.readline()
        result = []
        while line:
            # print("Line: ", line.strip())
            result.append(line.strip())
            line = reader.readline()
        return ", ".join(result)
