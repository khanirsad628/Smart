from SmartCalender import meeting_time,free_time
import logging

def main():
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
    working_hours_p1=['09:00','18:00']
    working_hours_p2=['09:00','18:00']
    person1=[['09:15','10:30'],['11:00','14:00'],['17:00','17:30']]
    person2=[['10:00','11:30'],['12:30','14:30'],['16:30','17:00']]
    time_def=30
    calendar1=free_time(person1,working_hours_p1,time_def)
    calendar2=free_time(person2,working_hours_p2,time_def)
    meetings=meeting_time(calendar1,calendar2, time_def)
    if len(meetings)==0:# no free time is there
        msg = "There is conflict in time for meeting"
        logging.info(msg)
    else:
        for i in range(len(meetings)):
            msg = str(i+1)+'. possible time for the meeting is : '+str(meetings[i])
            logging.info(msg)

if __name__ == "__main__":
    main()

