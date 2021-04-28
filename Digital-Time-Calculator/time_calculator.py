def add_time(start, duration,weekday=False):
  
  locale=len(locals())
  checker=False
  if(weekday==True):
    checker=True
  now_time = start.split(':',1)
  now_time.append(now_time[1].split(' ')[0])
  now_time.append(now_time[1].split(' ')[1])
  add_time = duration.split(':')
  del now_time[1]

  hours= int(now_time[0])
  minutes=0
  counter=0
  bool1=False
  ampm=''
  nextday=''

  if(int(now_time[1])+int(add_time[1])>=60):
    minutes=int(now_time[1])+int(add_time[1])-60
    hours+=1
    if(now_time[0]=='11'):
      counter=1
      temp=0
      bool1=True
  else:
    minutes = int(now_time[1])+int(add_time[1])

  if((hours+ int(add_time[0]))>=12):
    temp=hours
    if(bool1==True and hours==12  ):
      temp=0
    elif(bool==True):
      temp=temp-1
    if(hours==12):
      hours=0
    zeroaddtime=add_time[0]
    hours=(hours+ int(add_time[0])) - int((hours+int(add_time[0]))/12)*12
    for i in range(int(add_time[0])):
      temp=temp+1
      if(temp>11):
        counter=counter+1
        temp=0
  else:hours=(hours+ int(add_time[0])) - int((hours+int(add_time[0]))/12)
  if(hours==0 ):
    hours=12

  if((now_time[2].upper())=='PM'):
    if(counter==1):
      ampm=' AM'
      nextday=' (next day)'
    elif(counter==2):
       ampm=' PM'
       nextday=' (next day)'
    elif(counter>2 and counter%2!=0):
      nextday=" " + "(" +str(int((counter+1)/2))+ ' days later)'
      ampm=' AM'
    elif(counter>2 and counter%2==0):
      nextday=" " +"("+ str(int((counter)/2))+ ' days later)'
      ampm=' PM'
    else:
      ampm=' PM'
  else:

    if(counter==1):
      ampm=' PM'

    elif(counter==2 or counter==3):

      if(counter==2):
        ampm=' AM'
        nextday=' (next day)'

      else:
        ampm=' PM'
    
    elif(counter>1 and counter%2==0):
      nextday= " " + "("+str(int((counter)/2)) + ' days later)'
      ampm=' AM'

    elif(counter>1 and counter%2!=0):
      nextday=" " + "("+str(int((counter+1)/2))+ ' days later)'
      ampm=' PM'
    
    else:
      ampm=' AM'

  if(isinstance(weekday,str)):

    if( len(str(minutes))<2 and counter%2==0):
      new_time=  str(hours) + ":0" + str(minutes) + ampm +", "+ weekdays(counter,weekday,now_time[2])+ nextday
    elif(len(str(minutes))<2 and counter%2!=0):
      new_time= str(hours) + ":0" + str(minutes) + ampm + ", " +weekdays(counter,weekday,now_time[2])+ nextday
    elif( ):
      new_time=  str(hours) + ":" + str(minutes) +ampm + ", " +weekdays(counter,weekday,now_time[2])+ nextday
    elif((len(str(minutes)))<2):
      new_time=  str(hours) + ":0" + str(minutes) + ampm + ", " +weekdays(counter,weekday,now_time[2])+ nextday
    else:new_time=  str(hours) + ":" + str(minutes) +ampm + ", " +weekdays(counter,weekday,now_time[2])+ nextday
    return new_time

  else:
    if(len(str(minutes))<2 and counter%2==0):
      new_time=  str(hours) + ":0" + str(minutes) + ampm + nextday
    elif(len(str(minutes))<2 and counter%2!=0):
      new_time=   str(hours) + ":0" + str(minutes) + ampm + nextday
    elif( ):
      new_time=   str(hours) + ":" + str(minutes) +ampm + nextday
    elif((len(str(minutes)))<2):
      new_time=  str(hours) + ":0" + str(minutes) + ampm + nextday
    else:new_time=  str(hours) + ":" + str(minutes) +ampm + nextday
    return new_time

def weekdays(count,day,ampm):
  weekdays= ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','Sunday']
  weekdaysindex=0
  
  for i in range(len(weekdays)):
    if (weekdays[i]==day.capitalize()):
      weekdaysindex=i
      break;
  if(ampm=='PM'):
    for i in range(1,count+1):
      if(i%2!=0):
        try:
          weekdays[weekdaysindex+1]
          weekdaysindex=weekdaysindex+1
        except :
          weekdaysindex=0
  if(ampm=='AM'):
    
    for i in range(1,count+1):
      if(i%2==0):
        
        try:
          weekdays[weekdaysindex+1]
          weekdaysindex=weekdaysindex+1
        except :
          weekdaysindex=0
 
  return weekdays[weekdaysindex]
  
      