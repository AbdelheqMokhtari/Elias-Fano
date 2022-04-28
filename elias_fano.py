import hashlib
import math
import sys







file_name = sys.argv[-1]
with open(file_name,'rt') as file :
    numbers = [int(line) for line in file] #get values from the file and save it in numbers_list(save numbers as string) 
    file.close() #close the file 

n = len(numbers)
m = max(numbers)
l = int(math.log2(m) - math.log2(n))
print("l",l)
mask_lower_size = (2**(l))-1 # for example if we have l = 3  the mask = 7 because bin(7) = 111
flag = 8
store = 0
result = []
for i in range(n):
    lower_bits = numbers[i]& mask_lower_size
    flag -= l
    if(flag > 0):

        lower_bits <<= flag
        store |= lower_bits

    else : 
        saved_lower_bits = lower_bits
        flag *= (-1)
        saved_lower_bits &= ((2**flag) - 1)
        lower_bits >>= flag
        store |= lower_bits
        result.append(store)
        flag = 8 - flag
        saved_lower_bits <<= flag
        store = saved_lower_bits

if(store != 0):
    result.append(store)
    store = 0
    flag = 8 

print("L")
for i in range(len(result)):
    format_printing = "{0:b}".format(result[i]).zfill(8)
    print(format_printing)

L = bytearray(result)

del result[:]

u = int(math.log2(m)+1) - l

upper_bits = []
count = []
if( u <= 8):
    for i in range(n):
        upper_bits.append(numbers[i]>>l)
    for i in range((2**u)):
        count.append(upper_bits.count(i))
    
    for k in count:
        if (k == 0):
            #print(store)
            if(flag == 8):
                flag -= 1
            else :
                store <<= 1
                flag -= 1
                if(flag == 0):
                    result.append(store)
                    flag = 8
                    store = 0
        #while(k > 0):
        else :
            if(store == 0):
                store = 1
                
            else :
                store <<= 1
                store |= 1

            k -= 1
            flag -= 1

            if(flag == 0):
                result.append(store)
                flag = 8
            #if(store > 128):
            #    new_list_test.append(store)
                store = 0
            while(k>0):
                store <<= 1
                store |= 1
                k -= 1
                flag -= 1
                if (flag == 0):
                    result.append(store)
                    flag = 8
                    store = 0
                
            #if(store > 128):
            #    new_list_test.append(store)
            #    store = 0
        
            store <<= 1
            flag -= 1
            if(flag == 0):
                result.append(store)
                store = 0
                flag = 8
else :
    print("nothing to do")

print("U")
for i in range(len(result)):
    format_printing = "{0:b}".format(result[i]).zfill(8)
    print(format_printing)

U = bytearray(result)

del result[:]


m = hashlib.sha256()
m.update(L)
m.update(U)
digest = m.hexdigest()
print(digest) 