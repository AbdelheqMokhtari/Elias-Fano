import hashlib
import math
import sys

"""
    Elias_fano.py : this script compress monotone non-decreasing sequence of n integers using Elias-Fano representation using bytearrays  
    File name: Elias_fano.py
    Author: Abdelheq Mokhtari
    Date created: 4/17/2022
    Date last modified: 4/21/2022
    Python Version: 3.9.9
"""

#reading values from a file 
file_name = sys.argv[-1]
with open(file_name,'rt') as file :
    numbers = [int(line) for line in file] #get values from the file and save it in numbers_list(save numbers as string) 
    file.close() #close the file 



n = len(numbers) # calculate n --> how many elements we have in our list 
m = max(numbers) # calculate m --> the max value 
l = int(math.log2(m) - math.log2(n)) # calculate l --> number bits of lowerbits we can also calculate it as math.log2(m/n)
print("l",l)

# calculate lower_bits 

mask_lower_size = (2**(l))-1 # for example if we have l = 3  the mask = 7 because bin(7) = 111
shift = 8 # this variable to follow the position of the number 
store = 0 # to storee values 
result = [] #to store a list of lowerbits 
for i in range(n):
    lower_bits = numbers[i]& mask_lower_size # get lower bits using mask 
    shift -= l # substracte shift with l every time in the loop for example we have l= 3 the first time it will be 5 means we shift the number 5 times to the left <<

    # this scenario when we have shift greater than 0 
    if(shift > 0): 

        lower_bits <<= shift # shift lower_bits with number sotre in shift 
        store |= lower_bits #or operator with store for example we have store = 11000000 and lower_bits = 00101000 now store will be = 11101000


    # this scenario when we have shift less or equal to 0
    else : 
        saved_lower_bits = lower_bits # we save the lower_bits 
        shift *= (-1) # since our shift variable is negative or 0 so we need to make it positive so we can shift 
        
        lower_bits >>= shift # shiift to the right to get ride of the last (shift) character 
        store |= lower_bits # or operator the put the lower_bits in store 
        result.append(store)# append store in result  
        saved_lower_bits &= ((2**shift) - 1)
        shift = 8 - shift# initial shift again 
        saved_lower_bits <<= shift
        store = saved_lower_bits # saved the rest of bits in store and intial it again 

#after finishing the for loop we save the remeaning store in result because if we didn't reach 0 or negative number store won't bee append in result 

if(store != 0):
    result.append(store) # append the remaing store to result the last byte in L

# set the values to store and shift to work with them again later    
store = 0
shift = 8 


# print the L i can print it in different way using bytearray 
print("L")
for i in range(len(result)):
    format_printing = "{0:b}".format(result[i]).zfill(8)
    print(format_printing)

#create a bytearray using result list  

L = bytearray(result)


#delete all values in result = [] 

del result[:]

#calculate u 

u = int(math.log2(m)+1) - l

# declate list to work with them 

upper_bits = [] # get a list of all upper bits from all the dataset 
count = [] #this list countain numbers from of size 2**u it contains how many any number appairs for example count = [0,2,1,0] means 0 appears 0 times 1 appers twice and 2 appears once ... 

# Calculate U

if( u <= 8): # for now it's only work fine with u <=8
    for i in range(n):
        upper_bits.append(numbers[i]>>l) #shift with l to romove the lower bit and have only upper bits
    for i in range((2**u)):
        count.append(upper_bits.count(i)) # calculate count 
    
    for k in count:
        if (k == 0): # if this number doesn't appears 
            #print(store)
            if(shift == 8): # if we have an empty number
                shift -= 1 
            else :
                store <<= 1 #shift it for example we have store = 110 we shift he become store = 1100
                shift -= 1 #decrement shift with 1 
                if(shift == 0):
                    result.append(store) # save store
                    shift = 8
                    store = 0
        #while(k > 0):
        else : # if the number appears 
            if(store == 0): #if store still equal to zero 
                store = 1 # intial it with 1 
                
            else :
                store <<= 1 # shift to the left so for example we have store = 1101 we will have now store = 11010 
                store |= 1 # and then or operators with 1 so store = 11011 

            k -= 1 # decrement k with one 
            shift -= 1 # decrement shift with one 

            #if shift equal to zero append result with store and intial store with 0
            if(shift == 0):
                result.append(store)
                shift = 8
            #if(store > 128):
            #    new_list_test.append(store)
                store = 0

            # repeat the same step while K > 0     
            while(k>0):
                store <<= 1
                store |= 1
                k -= 1
                shift -= 1
                if (shift == 0):
                    result.append(store)
                    shift = 8
                    store = 0
                
            #if(store > 128):
            #    new_list_test.append(store)
            #    store = 0
            
            #after he finish the loop he shift store again and decremeant shift again 
            store <<= 1
            shift -= 1
            if(shift == 0):
                result.append(store)
                store = 0
                shift = 8

# i will work on a general case where it can work perfectly with u even it's greater than 8                
else :
    print("nothing to do")

# print U
print("U")
for i in range(len(result)):
    format_printing = "{0:b}".format(result[i]).zfill(8)
    print(format_printing)

#result saved on U as a bytearray  
U = bytearray(result)

#delete result 
del result[:]

#hash function and print it 
m = hashlib.sha256()
m.update(L)
m.update(U)
digest = m.hexdigest()
print(digest) 