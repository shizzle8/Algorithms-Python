import os

#Parameter 'a' takes in a string
def check(a):

    #This varianle stores key value pairs of an open and closed brace
    store = {'[':']','{':'}','(':')'}

    #Checks if odd number characters and returns NO since it will not be balanced
    if(len(a)%2!=0):
        return print('NO')

    else:
        for i in range(len(a)):
            #Wrap around to catch indexError and Key input error, which should return NO if anything is caught
            try:
                #First algorithm to check if the first two characters are a balanced pair
                if(store[a[0]]==a[1]):
                    
                    #if it continues to have two balanced pairs then go to the next or return NO since it wont be balanced
                    if(store[a[i*2]]==a[i*2+1]):
                    
                        continue
                    else:
                        
                        return print("NO")

                #Second Algorith checks whether there is a nested braces balance by splitting the string in half and comparing them    
                elif(store[a[:(int(len(a)/2))][i]]==a[int(len(a)/2):][len(a[int(len(a)/2):])-1-i]):
                   
                    continue
        
                else:
                    return print('NO');
                
            except IndexError:
                pass
                
        #Finally return YES when it has passed all the checks of the algorithm
        return print ('YES')



check('{[()]}')
