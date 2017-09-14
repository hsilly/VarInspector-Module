#!/usr/bin/env python
class Time:
    def __init__(self):
        self.zero = False
    def findHour(self, string):
        self.hourlist = []
        colon = False
        #strvarname = ''.join(self.findVarName(string, globals()))
        strvarname = self.findVarName(string, globals())
        for l in string:
            if l.isalpha() == True:
                raise TypeError('Alpha numeric character "'+l+'" found in var "'+str(strvarname)+'"')
            if l != ":" and colon != True:
                self.hourlist.append(l)
            if l == ":":
                colon = True
        hour = ''.join(self.hourlist)
        return hour
    def findMin(self, string):
        minuteslist = []
        colon = False
        for l in string:
            if l == ":":
                colon = True
            if l!=":" and colon == True:
                minuteslist.append(l)
        minutes = ''.join(minuteslist)
        return minutes
    def totalsec(self, string):
        #varname = ''.join(self.findVarName(string, globals()))
        hour = self.findHour(string)
        minutes = self.findMin(string)
        if int(minutes) == 0:
            self.zero = True
        minsec = int(hour)*60
        totalsec = minsec + int(minutes)
        return totalsec
    def dectime(self, string):
        hour = self.findHour(string)
        minutes = self.findMin(string)
        decstr = str(hour)
        decmins = float(minutes)/60.0
        return decstr + str(decmins)[1::]
    def findcolon(self, string):
        prev = ''
        colon = False
        checkup = False
        done = False
        for l in string:
            if checkup == True:
                try:
                    this = int(l)
                    if colon == True:
                        colon == False
                        done = True
                    if done == False:
                        colon = True
                except ValueError:
                    checkup = False
            if l == ":":
                if prev == 'numb':
                    checkup = True
            else:
                try:
                    this = int(l)
                    prev = "numb"
                except ValueError:
                    prev = "string"
        return colon
    '''def findcolon2(self, string):
        prev = ''
        colon = False
        checkup = False
        done = False
        delete = True
        prevnumb = []
        times = 0
        for l in string:
            if checkup == True:
                try:
                    this = int(l)
                    if times == 2:
                        done = True
                    elif colon == True and done != True:
                        colon = False
                        # this one
                        done = True
                    if done == False and times < 2:
                        colon = True
                    #checkup = False
                    prevnumb.append(l)
                    delete = False
                    times += 1
                except ValueError:
                    checkup = False
            if l == ":":
                if prev == 'numb':
                    checkup = True
                    prevnumb.append(l)
            else:
                try:
                    this = int(l)
                    prev = "numb"
                    prevnumb.append(l)
                except ValueError:
                    prev = "string"
                    if delete == True:
                        prevnumb = []
        if colon == True:
            return prevnumb
        else:
            return False'''
        
    def addTime(self, timeStr, adding, hourormin):
        this = self.totalsec(timeStr)
        time = int(this)
        #if self.findcolon(adding) == True:
        for l in str(adding):
            try:
                this = int(l)
            except ValueError:
                varname = self.findVarName(adding, globals())
                raise ValueError('Non-numeric value found in var "'+varname+'".')
        if hourormin.lower() == 'hour' or hourormin.lower() == 'h':
            time += (int(adding)*60)
        if hourormin.lower() == 'minute' or hourormin.lower() == 'min' or hourormin.lower() == 'm':
            time+=int(adding)
        totalhours = int(time/60)
        totalsec = time%60
        if self.zero == True:
            return str(totalhours)+':'+str(totalsec)+'0'
        else:
            return str(totalhours)+':'+str(totalsec)
        
        
    def findVarName(self, obj, namespace):
        for l in namespace:
            if namespace[l] is obj:
                return str(l)
Time = Time()
print Time.addTime('7:00','7','h')
class Variables:
    def findVarName(self, variable, namespace):
        for l in namespace:
            if namespace[l] is variable:
                return l
    def findVarType(self, variable):
        string = False
        numbers = False
        neither = False
        prev = ''
        nex = ''
        checkup = False
        for l in variable:
            try:
                this = int(l)
                numbers = True
                checkup = False
                prev = "numb"
            except ValueError:
                if checkup == True:
                    string = True
                    neither = True
                checkup = False
                if l == ".":
                    if prev == "numb":
                        checkup = True
                    else:
                        neither = True
                elif l.isalpha() == True:
                    string = True
                    prev = "string"
                else:
                    neither = True
        if checkup == True:
            neither = True
        print string
        print numbers
        print neither
        vartype = []
        if string == True:
            vartype.append('string')
        if numbers == True:
            vartype.append('numbers')
        if neither == True:
            vartype.append('neither')
        return vartype 
Variables = Variables()









