import random
names = [" joe "," bob "," sueann "," loretta "," grant ",\
         " jenny "," billy "," tucker "," cletus ", " hunter "\
         " gunner "]
#waitingarea is for already seen
waitingarea = []
#traiagearea is now the wait area 
waitarea = []
#doctor comes in
examarea = []
#the amount of areas for the doctors 
examareasSize = 6
#the amount of actual doctors
doctors = 6

def callNurse():
    """move patient from waiting area to wait area"""
    waitarea.append(waitingarea.pop(0))
    sort(waitarea, key=patient.waitNumber)

class Patient:
    def __init__ (self,name):
        self.name = name
def nurse(js):
    js.addPatient2(js.removePantient())

class waitingarea:
    #before the nurse
    def __init__(self):
        self.patientWaiting = []
        self.patientWaitingLonger = []
    def addPatientA (self,patient):
        self.patientWaiting.append(patient)
    def removePatientA(self):
        return self.patientWaiting.pop(0)
    #keeps track of seeing the doc
    def addPatientB(self,patient):
        self.patientWaitingLonger.append(patient)
    def removePatientB(self):
        return self.patientWaitingLonger.pop(0)
    def emptyArea(self): #if area avaible or not
        if self.patientWaiting == []:
            return True
        else:
            return False
    def emptyAreaB(self):
        if self.patientWaiting == []:
            return True
        else:
            return False
class examArea:
    def __init__(self):
        self.areaTime = 0
        self.patient = None
        self.patientTime = 0 #how long patient is in the room for

    def addPatientC(self,js):
        #heading in to waiting area
        self.patient = js.removePatientB()
        self.patientTime = random.randrange(15,21)

    def time(self):
        return self.patientTime

    def emptyAreaC(self):#tells if any of the exam areas open
         if self.patient == None:
             return True
         else:
             return False

    def removePatientC(self):
        x = self.patient
        self.patient = None
        return x
    #gives doctor for an exam area

    #tracks how long patient has been in area
    def timeSpendinArea(self):
        return self.areaTime
    def moreTime(self):
        self.areaTime += 1
#gives more time
WA = waitingarea()

A1 = examArea()
A2 = examArea()
A3 = examArea()
A4 = examArea()
A5 = examArea()
A6 = examArea()

def updateTime():
    nurse(WA)
    if not A1.emptyAreaC():
        A1.moreTime()
        if A1.time() >= A1.timeSpendinArea():
            A1.removePatientC()

    if A1.emptyArea():
        if not WA.emptyAreaB():
            A1.addPatientC(WA)
            
    if not A2.emptyAreaC():
        A2.moreTime()
        if A2.time() >= A2.timeSpendinArea():
            A2.removePatientC()

    if A2.emptyArea():
        if not WA.emptyAreaB():
            A2.addPatientC(WA)

    if not A3.emptyAreaC():
        A3.moreTime()
        if A3.time() >= A3.timeSpendinArea():
            A3.removePatientC()

    if A3.emptyArea():
        if not WA.emptyAreaB():
            A3.addPatientC(WA)

    if not A4.emptyAreaC():
        A4.moreTime()
        if A4.time() >= A4.timeSpendinArea():
            A4.removePatientC()

    if A4.emptyArea():
        if not WA.emptyAreaB():
            A4.addPatientC(WA)

    if not A5.emptyAreaC():
        A5.moreTime()
        if A5.time() >= A5.timeSpendinArea():
            A5.removePatientC()

    if A5.emptyArea():
        if not WA.emptyAreaB():
            A5.addPatientC(WA)

    if not A6.emptyAreaC():
        A6.moreTime()
        if A6.time() >= A6.timeSpendinArea():
            A6.removePatientC()

    if A6.emptyArea():
        if not WA.emptyAreaB():
            A6.addPatientC(WA)
            
