import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**colours):
    self.contents=[]
    #print("OOOOOOOOOOOOOOIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    for i in colours:
      for j in range(colours[i]):
        self.contents.append(i)
    #print(self.contents)
  # I CHANGED SELF.CONTENTS TO LOCALCONTENNNNTS
  def draw(self,number):
    localContent=copy.copy(self.contents)

    random1=[]
    #print(self.contents)
   # print(number, '---', len(localContent) )
    if(number>len(localContent)):

      return localContent
    else:
      for i in range(number):
        random1.append(random.choice(localContent))
        localContent.remove(random1[i])
  
      return random1

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  expList1 = createList(expected_balls)
  #print(len(expList1),'OOOOOOOOOOOGGGGGGGGGGGGGGGGGGA')
  counter=0
  if(num_balls_drawn>len(hat.contents) or num_balls_drawn<len(expList1)):
    return 1.0
  else:
    for x in range(num_experiments):
      expList = createList(expected_balls)
      #print(hat.contents,'saysyaysyaysaysyays')#
      list1 = hat.draw(num_balls_drawn)
     # print(list1, 'STARTTTTTTTTTTTT')
     # print(hat.contents,'saysyaysyaysaysyays')
      for y in range(len(expList1)):
      
      
        
        # print(len(expList),'hahahha')
        #print(expList,'mamamamma')
        for z in range(len(list1)):

          if(expList1[y]==list1[z]):
           # print(counter,'looooooooooooooooooool')
            list1.pop(z)
            expList.pop(0)
            break
          
        if(len(expList)==0):
          #print('assasasasas')
          counter=counter+1
          break
      #print('--------------------------------')
    # print(expList)

    
  #print(counter,'tetetete')
  return counter/num_experiments

def createList(dictionary):
  list1=[]
  #print(type(dictionary))
  for i,j in dictionary.items():
    for x in range(j):
      list1.append(i)
  return list1 