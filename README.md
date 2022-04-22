# Elias Fano

this is my first assignment in the module Expert Systems and artificial intelligence in the Universiy of Piraeus it was about Elias fano encoding/decoding fore more details check [this article](https://www.antoniomallia.it/sorted-integers-compression-with-elias-fano-encoding.html)

## Steps of the Algorithm 

1- First step we get integers from a file (example_1.txt or example_2.txt) and put the numbers in a list of a string.

```python
file_name = sys.argv[-1]
with open(file_name, 'rt') as file: 
    numbers = file.read().splitlines() 
    file.close() 
```

2- Convert string into integers find the biggest in the universe m to calculate the size of the representation of the binary number 
the size of the represntation = log2(m) rounded to the unit.

```python
numbers = [int(i) for i in numbers] 
m = max(numbers)  
binary_size = math.log2(m) 
binary_size = int (binary_size // 1) + 1
```
3- Convert the integers in the list in binary format.

```python
binary_numbers = [] 
for item in numbers:
    binary_numbers.append(bin(item)[2:].zfill(binary_size)) 
```

4- Calculate the size of the lower bits ( how many bits the lower bits have from the totall of all bits ).

```python
n = len(numbers) 
l = int (math.log2(m)-math.log2(n))
```

5- Create lower_bits from the numbers and put in one long list of string's.

```python
L = [] 
for j in range(n):
    L.append(binary_numbers[j][binary_size-l:binary_size]) 

L =''.join(L)
```

6- Make the U string size multiple of 8 by adding '0' in the end of the string.

```python
if(len(L) % 8 != 0):
    rest_bit = 8 - (len(L)%8)
    for i in range(rest_bit):
        L = L + '0'
```

7- Print U on shape of bytes.

```python
for i in range(0, len(L), 8):  
    print(L[i:i+8])
```

8- Create the Upper_bits the size of the upper bits are the first (binary_size - l) item 

```python
upper_bits = []

for k in range(n):
    upper_bits.append(binary_numbers[k][:binary_size-l]) 
```

## output 


