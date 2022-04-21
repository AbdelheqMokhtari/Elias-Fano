# Elias Fano

this is my first assignment in the module Expert Systems and artificial intelligence in the Universiy of Piraeus it was about Elias fano encoding/decoding 

## Steps of the Algorithm 

1- First step we get integers from a file (example_1.txt or example_2.txt) and put the numbers in a list of a string 

```python
file_name = sys.argv[-1]
with open(file_name, 'rt') as file: 
    numbers = file.read().splitlines() 
    file.close() 
```

2- Convert string into integers find the biggest in the universe m to calculate the size of the representation of the binary number 
the size of the represntation = log2(m) rounded to the unit 

```python
numbers = [int(i) for i in numbers] 
m = max(numbers)  
binary_size = math.log2(m) 
binary_size = int (binary_size // 1) + 1
```
3- convert the integers in the list in binary format 

```python
binary_numbers = [] 
for item in numbers:
    binary_numbers.append(bin(item)[2:].zfill(binary_size)) 
```

4- calculate the size of the lower bits ( how many bits the lower bits have from the totall of all bits ) 

```python
n = len(numbers) 
l = int (math.log2(m)-math.log2(n))
```

5- create lower_bits from the numbers and put in one long list of string's 
```python
L = [] 
for j in range(n):
    L.append(binary_numbers[j][binary_size-l:binary_size]) 

L =''.join(L)
```
## output 


