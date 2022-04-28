import hashlib
import math
import sys

"""
    Elias_fano.py : this script compress monotone non-decreasing sequence of n integers using Elias-Fano representation 
    File name: Elias_fano.py
    Author: Abdelheq Mokhtari
    Date created: 4/17/2022
    Date last modified: 4/21/2022
    Python Version: 3.9.9
"""

# read int from a file 

file_name = sys.argv[-1]
with open(file_name, 'rt') as file: #open the file 
    numbers = file.read().splitlines() #get values from the file and save it in numbers_list(save numbers as string) 
    file.close() #close the file 

numbers = [int(i) for i in numbers] 
m = max(numbers)  
binary_size = math.log2(m) 
binary_size = int (binary_size // 1) + 1  

# covert numbers in list(numbers) to binary 
binary_numbers = [] 
for item in numbers:
    binary_numbers.append(bin(item)[2:].zfill(binary_size)) 
n = len(numbers) # calculate how many numbers we have in our list 
l = int (math.log2(m)-math.log2(n)) # calculate the size of the lower bits we can use (Math.log2(m/n))
print('l',l) # print the size of the lower bits   



L = [] 
for j in range(n):
    L.append(binary_numbers[j][binary_size-l:binary_size]) 

L =''.join(L) 
# make L from multiples of 8 
if(len(L) % 8 != 0):
    rest_bit = 8 - (len(L)%8)
    for i in range(rest_bit):
        L = L + '0' # complete L with 0 till he become multiple of 8

for i in range(0, len(L), 8):  
    print(L[i:i+8]) #print L as shape of bytes 

# split Upper Bits         
upper_bits = []

for k in range(n):
    upper_bits.append(binary_numbers[k][:binary_size-l]) # we calculate the upper bits from the first bits of binary number 
    
# create all possible paterns and combination that can 1 and 0 format with a specif length     
a = 0
list_of_possiblites = [] # list to save all possible values 
for i in range(2**(binary_size-l)):
    list_of_possiblites.append(bin(a)[2:]) # create a list of binary numbers from 0 to 2^(binary_size-l) ['0','1','10',...]
    a = a + 1 # increament a 
combinations = [] #list to format the possible values with a fixed size 
for item in list_of_possiblites:
    combinations.append(item.zfill(binary_size-l)) # the fixed size (binary_size-l) and that's the size of the upper_bits 

# calculate Upper Bits    
U = [] # create an empty list 
for item in combinations:
    count = upper_bits.count(item) #count how a specific number appears in the upper_bits for example how many times 0011 appears 
    for j in range(count):
        U.append('1') #we add 1 the times of the appearns 
    U.append('0') #to sperate between values 

#remove the last 0 of the U because they are not necassery 
while (U[-1]=='0'):
    U.pop()  #remove the last item in the list 

# make U a one string 

U =''.join(U) #join all items of the List L together 

# make U from multiples of 8 
print('U')
if(len(U) % 8 != 0):
    rest_bit = 8 - (len(U)%8)
    for i in range(rest_bit):
        U = U + '0'

#print U 
for i in range(0, len(U), 8):  
        print(U[i:i+8])#print 8 values and break the line

#convert L and U to Bytes to pass the in update method 
L = int(L, 2).to_bytes(len(L) // 8, byteorder='big')
U = int(U, 2).to_bytes(len(U) // 8, byteorder='big')

#hash function and print it 
m = hashlib.sha256()
m.update(L)
m.update(U)
digest = m.hexdigest()
print(digest) 