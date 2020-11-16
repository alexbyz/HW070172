class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

def makeStudent(infoStr):
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()),file=outfile)
    outfile.close()

def main():
    print("this program sorts student grade information by GPA")
    filename = input("Filename: ")
    data = readStudents(filename)
    
    choise = input("Sort on pga (g), name (n) or credits (c): ")
    direction = input("ascending (a), decending (d): ")
    if choise == 'g':
        data.sort(key=Student.gpa)             
    elif choise == 'n':
        data.sort(key=Student.getName)
    elif choise == 'c':
        data.sort(key=Student.getHours)
    else:
        print("please check your choise")
        quit()
    
    if direction == 'd':
        data.reverse()
    elif direction == 'a':
        direction = ' '
    else:
        print("please check your choise")
        quit()

    filename = input("Outfile: ")
    writeStudents(data, filename)

main()

