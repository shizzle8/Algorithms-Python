import re
def arithmetic_arranger(problems,boolting=False):
    arranged_problems=''
    top=''
    second=''
    third=''
    fourth=''
    if(boolting==True):
      for i in problems:
        temp = i.split()
      
        if(len(problems)>5):
          return "Error: Too many problems."

        if(temp[1]!='+' and temp[1]!='-'):
          return "Error: Operator must be '+' or '-'."
        if(len(temp[0])>4 or len(temp[2])>4):
          return "Error: Numbers cannot be more than four digits."
        if(not (temp[0].isnumeric() and temp[2].isnumeric())):
          return "Error: Numbers must only contain digits."
            
          
        if(len(temp[0])>len(temp[2])):
          top += '  ' + temp[0] + '    '
          second+= temp[1] + ' ' +temp[2].rjust(len(temp[0]))+ '    '
          third+= charr_2(len(temp[0])+2,'-')+ '    '
          if(temp[1]=='+'):
            x= len(str((int(temp[0]))))+2-len(str(int(temp[0]) + int(temp[2])))
       
            fourth+=  charr_2(2, ' ') + str((int(temp[0]) + int(temp[2])))+ '    '
          else:
            x= len(str((int(temp[0]))))+2-len(str(int(temp[0]) - int(temp[2])))
          
            fourth+= charr_2(x, ' ') + str((int(temp[0]) - int(temp[2])))+ '    '

        
        
          
        elif(len(temp[2])>len(temp[0])):
          top += '  ' + temp[0].rjust(len(temp[2])) + '    '
          second += temp[1] + ' ' + temp[2].rjust(len(temp[0]))+ '    '
          third+= charr_2(len(temp[2])+2,'-')+ '    '  
          if(temp[1]=='+'):
            x= len(str((int(temp[2]))))+2-len(str(int(temp[0]) + int(temp[2])))
            fourth+= charr_2(x,' ') + str((int(temp[0]) + int(temp[2])))+ '    '
          else:
            x= len(str((int(temp[2]))))+2-len(str(int(temp[0]) - int(temp[2])))
            fourth+= charr_2(x,' ') + str((int(temp[0]) - int(temp[2])))+ '    '
          

        else:
          top += '  ' + temp[0] + '    '
          second += temp[1] + ' ' + temp[2]+ '    '
          third+= charr_2(len(temp[0])+2,'-')+ '    '
          if(temp[1]=='+'):
            x= len(str((int(temp[0]))))+2-len(str(int(temp[0]) + int(temp[2])))
            fourth+= charr_2(x,' ') + str((int(temp[0]) + int(temp[2])))+ '    '
          else:
            x= len(str((int(temp[0]))))+2-len(str(int(temp[0]) - int(temp[2])))
            fourth+= charr_2(x,' ') + str((int(temp[0]) - int(temp[2])))+ '    '
      arranged_problems+= top.rstrip() + '\n' + second.rstrip() + '\n' + third.rstrip() + '\n' +fourth.rstrip()

    else:
      for i in problems:
        temp = i.split()
        if(len(problems)>5):
          return "Error: Too many problems."
        if((temp[1]!='+') and (temp[1]!='-')):
          return "Error: Operator must be '+' or '-'."
        if(len(temp[0])>4 or len(temp[2])>4):
          return "Error: Numbers cannot be more than four digits."
        if(not (temp[0].isnumeric() and temp[2].isnumeric())):
          return "Error: Numbers must only contain digits."
            
        if(len(temp[0])>len(temp[2])):
          top += '  ' + temp[0] + '    '
          second+= temp[1] + ' ' +temp[2].rjust(len(temp[0]))+ '    '
          third+= charr_2(len(temp[0])+2,'-')+ '    '
          if(temp[1]=='+'):
            fourth+= '  ' + str((int(temp[0]) + int(temp[2])))+ '    '
          else:
            fourth+= '  ' + str((int(temp[0]) - int(temp[2])))+ '    '

        
        
          
        elif(len(temp[2])>len(temp[0])):
          top += '  ' + temp[0].rjust(len(temp[2])) + '    '
          second += temp[1] + ' ' + temp[2].rjust(len(temp[0]))+ '    '
          third+= charr_2(len(temp[2])+2,'-')+ '    '  
          if(temp[1]=='+'):
            fourth+= '  ' + str((int(temp[0]) + int(temp[2])))+ '    '
          else:
            fourth+= '  ' + str((int(temp[0]) - int(temp[2])))+ '    '
          

        else:
          top += '  ' + temp[0] + '    '
          second += temp[1] + ' ' + temp[2]+ '    '
          third+= charr_2(len(temp[0])+2,'-')+ '    '
          if(temp[1]=='+'):
            fourth+= '  ' + str((int(temp[0]) + int(temp[2])))+ '    '
          else:
            fourth+= '  ' + str((int(temp[0]) - int(temp[2])))+ '    '
      arranged_problems+= top.rstrip() + '\n' + second.rstrip() + '\n' + third.rstrip()
        
    
    return arranged_problems

def charr_2(numm,charr):
  text = ''
  for i in range (numm):
    text+=charr
  return text