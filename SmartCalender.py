from datetime import datetime
import logging

def free_time(x,bounds,time)->list:
    '''
    Function to check free time for employees
    param1: x — schedule
    param2: bounds - working hours
    param3: time  -  meeting duration
    returns list of free time for meeting
    '''
    new=[]
    b_start=datetime.strptime(bounds[0],"%H:%M")
    b_end=datetime.strptime(bounds[1],"%H:%M")
    start=datetime.strptime(x[0][0],"%H:%M")
    end=datetime.strptime(x[len(x)-1][1],"%H:%M")
    min_start=(b_start-start).seconds/60
    min_end=(b_end-end).seconds/60
    if min_start >= float(time):
        new.append([bounds[0],x[0][0]])
    for i in range(len(x)-1):
        if ((datetime.strptime(x[i+1][0],"%H:%M")-datetime.strptime(x[i][1],"%H:%M")).seconds/60) >=float(time):
            new.append([x[i][1],x[i+1][0]])
    if min_end >= float(time):
        new.append([x[len(x)-1][1],bounds[1]])
    return new

def meeting_time(calendar1,calendar2,time)->list:
    '''
    Function to compare the time of person1 and person2
    param1: calender1 : Free time hrs for person1
    param2: calender2 : Free time hrs for person2
    param3: time : meeting time duration
    returns list of free meeting time
    '''
    pres=[]
    final=[]
    for i in range(len(calendar1)):
        for j in range(len(calendar2)):
            if datetime.strptime(calendar1[i][1],"%H:%M")<=datetime.strptime(calendar2[j][1],"%H:%M"):
                if datetime.strptime(calendar1[i][0],"%H:%M")>=datetime.strptime(calendar2[j][0],"%H:%M"):
                    if ((datetime.strptime(calendar1[i][1],"%H:%M")-datetime.strptime(calendar1[i][0],"%H:%M")).seconds/60) >= float(time) :
                        pres.append([calendar1[i][0],calendar1[i][1]])
                else:
                    if ((datetime.strptime(calendar1[i][1],"%H:%M")-datetime.strptime(calendar2[j][0],"%H:%M")).seconds/60) >= float(time) :
                        pres.append([calendar2[j][0],calendar1[i][1]])
            else:
                if datetime.strptime(calendar1[i][0],"%H:%M")>=datetime.strptime(calendar2[j][0],"%H:%M"):
                    if ((datetime.strptime(calendar2[j][1],"%H:%M")-datetime.strptime(calendar1[i][0],"%H:%M")).seconds/60) >= float(time) :
                        pres.append([calendar1[i][0],calendar2[j][1]])
    for i in range(len(pres)):
        if datetime.strptime(pres[i][0],"%H:%M")<datetime.strptime(pres[i][1],"%H:%M"):
            final.append([pres[i][0],pres[i][1]])
    return final
