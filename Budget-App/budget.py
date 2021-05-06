import sys
import math
class Category:


  def __init__(self, category):
    self.category = category
    self.ledger=[]
  
  def deposit(self,amount,description):
    self.ledger.append({'amount': float(amount), "description": description})
  
  
  def withdraw(self,amount,description=False):
    total=0
   
    for i in range(len(self.ledger)):
      
      total+=self.ledger[i]['amount']
    if(total<amount):
      return False
    else:
      total= total-amount
      if(isinstance(description,str)):
        self.ledger.append({'amount':  float(amount*-1),'description': description})
      else:
        self.ledger.append({'amount':  float(amount*-1),'description': ''})
      return True

  def get_balance(self):
    total=0
    for i in range(len(self.ledger)):
      total+=float(self.ledger[i]['amount'])
    
    return float(total)
  
  def transfer(self,amount,budget):
    total=0
    for i in range(len(self.ledger)):
      total+=self.ledger[i]['amount']
    if(total<amount):
      return False
    else:
      total= total-amount
      self.ledger.append({'amount': float(amount*-1), 'description': 'Transfer to ' + budget.category})
      budget.deposit(amount,'Transfer from '+ self.category)
      return True

  def check_funds(self, amount):
    if(self.get_balance()<amount):
      return False
    else:return True
  
  def __str__(self):
    length1=0
    topline='*************' + self.category +'*************\n'
    bottomline=""
    bottomline1=''
    #print(topline.index(self.category))
    #print(self.ledger)
    for x in range (len(self.ledger)):
      
      if(len(str(self.ledger[x]['amount']).split('.')[1])==1):
        bottomline=  appening(' ', len(topline)-len(str(self.ledger[x]['amount'])+'0')-1) + str(self.ledger[x]['amount'])+'0'
       
        length1=len(appening(' ', len(topline)-len(str(self.ledger[x]['amount'])+'0')-1))
      else:
        bottomline=  appening(' ', len(topline)-len(str(self.ledger[x]['amount']))-1) + str(self.ledger[x]['amount'])
        
        length1=len(appening(' ', len(topline)-len(str(self.ledger[x]['amount']))-1))
        #print(bottomline[26],'asfasfsf')
      for i in range(length1-1):
        #print(self.ledger[x]['description'][i])
       # print(bottomline[i],'232323')
        #print(i)
        #print(len(appening(' ', len(topline)-len(str(self.ledger[x]['amount']))-1)))
        
        #print(self.ledger[x]['description'][1])
        #print(type(bottomline))
        #print(type(self.ledger[x]['description'][1]))
        try:
          bottomline = list(bottomline)
          bottomline[i]=self.ledger[x]['description'][i]
            
            #print(self.ledger[x]['description'][i])
          #print(bottomline[i],'poooooooooooooooooooooooooooop')
        except:
            break;
         
       # bottomline.replace(appening(' ', len(topline)-len(str(self.ledger[x]['amount']))-1), str(self.ledger[x]['description']))
       # print(''.join(bottomline),'test')
      bottomline1+=''.join(bottomline)
      #print(bottomline1,'lol')
      bottomline1+="\n"
    #print(bottomline, 'lololol')
   
    if(len(str(self.get_balance()).split('.')[1])==1):
      return topline+ bottomline1  + "Total: " + str(self.get_balance()) + '0'
    else: return topline+ bottomline1  + "Total: " + str(self.get_balance()) 
#########################

def create_spend_chart(listOfCategories):
  title = "Percentage spent by category\n"
  name=[]
  percent=''
  cater=''
  biggestlength=(sys.maxsize*-1)
  x=0
  y=0
  t=0
 # print(len(listOfCategories))
  for i in range(len(listOfCategories)):
    name.append(listOfCategories[i].category)
    if(len(listOfCategories[i].category)>biggestlength):
      biggestlength=len(listOfCategories[i].category)
  
  for i in range(100,-1,-10):
    if(len(str(i))<3):
        percent += appening(' ', 3-len(str(i))) + str(i) + '|' 
        
    else: percent+= str(i) + '|' 

    for j in range(len(listOfCategories)):
      if(t>10):
        break
      else:
       percent+= ' ' + str(percentageGraph(listOfCategories[j],total(listOfCategories))[t]) + ' '
     # print(str(percentageGraph(listOfCategories[j])[t]),'MAMAMAMAMAMAMAMAMA')
    
    t=t+1
    #if(t>9):

    percent+= "\n"
    
 # print(name[x][y])
 # print(biggestlength)
  #print(len(listOfCategories)
  percent+= '    '+appening('-', len(listOfCategories)*3+1) + '\n'
  
  while(y<biggestlength*len(listOfCategories)):
    #print(y,'  lol')
    cater+= ' '
    try:
      #print('kl')
      if(x==0):
        cater+= '    ' + name[x][y] + ' '
      elif(x== len(listOfCategories)-1):
        cater+= name[x][y]
      else:
        cater+= name[x][y] + ' '
    except:
      if(x==0):
        cater+= '    ' + ' ' + ' '
      elif(x== len(listOfCategories)-1):
        cater+= ' '
      else:
        cater+= ' ' + ' '
    x=x+1
    if(x>=len(listOfCategories)):
      #print('lol')
      y=y+1
      cater+= '\n'
      x=0
     
    #global total1
    #total1 = total(listOfCategories)
  
  #print(total(listOfCategories),'lolollol')
  return title + percent + cater
  #print(percent + cater)
#print(mainTotal,'XXXDDDDDDDDDDDDDDDDDD')
def total(list1):
  total=0
  for i in range(len(list1)):
    for j in range(len(list1[i].ledger)):
      if(list1[i].ledger[j]['amount']<0):
        total+= list1[i].ledger[j]['amount']
  return (total*-1)


def appening(char1,size):
  text = ''

  for i in range(size):
    text+=char1
  return text

def percentageGraph(category,total):
  #category=listOfCategories[0]
  graph=[]
 # print(total1)
  percent1=(math.ceil((category.ledger[0]['amount'] -category.get_balance())/total*100))
  percentadd = int([y for y in str(percent1)][0]) 
  #print(mainTotal,'POOOOOOOOOOOOOOP')
  
  if(len(str(percent1))==1 and percent1<5):
    percent1=0
  elif(len(str(percent1))==1 and percent1>4):
    percent1=10
  elif(int([y for y in str(percent1)][1])<5):
    percent1 = percent1 - 10
    percent1 = percent1 + (percentadd)*(10)-percent1
  
  else:
     percent1 = percent1 + 10
     percent1 = percent1 + (percentadd)*(10)-(percent1-10)

  for i in range(11):
    if(i>=(10)-percent1/10):
      graph.append('o')
    else:
      graph.append(' ')
    
  return graph

#def create_spend_chart(categories):


 

  