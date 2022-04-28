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
9- Create all possible combinatation of 0's and 1's ('000','001','010','011','100','101'........) the length of the binary number equal to the size of number of upper bits.

```python
a = 0
list_of_possiblites = [] 
for i in range(2**(binary_size-l)):
    list_of_possiblites.append(bin(a)[2:]) 
    a = a + 1 
combinations = []  
for item in list_of_possiblites:
    combinations.append(item.zfill(binary_size-l)) 
```

10- Compare the upper bits of everynumber and count how many time the same combination's repeat we add 1's with number of repetation and separate with 0 

```python
U = []  
for item in combinations:
    count = upper_bits.count(item) 
    for j in range(count):
        U.append('1')  
    U.append('0') 
```

11- Repeat the same step's of priniting L with U 

```python
U =''.join(U) 

 
print('U')
if(len(U) % 8 != 0):
    rest_bit = 8 - (len(U)%8)
    for i in range(rest_bit):
        U = U + '0'


for i in range(0, len(U), 8):  
        print(U[i:i+8])
```

12 - convert the strings U and L to byte array's 

```python
L = int(L, 2).to_bytes(len(L) // 8, byteorder='big')
U = int(U, 2).to_bytes(len(U) // 8, byteorder='big')
```

13 - using ByteArray print the hash code generated from U and L together 

```python
m = hashlib.sha256()
m.update(L)
m.update(U)
digest = m.hexdigest()
print(digest) 
```
## output

1- Execute the script with the first example :

python elias_fano.py example_1.txt 

Result:
```bush
l 3
01011100
00111010
01001100
11100100
U
00110100
01101010
11001000
ff94079dbe887ca366d8a759da92e13a860d8a733c6a9125429d51a9b1b6a5c8
```

2- Execute the script with the second example :

python elias_fano.py example_2.txt 

Result:
```bush
l 4
01101101
00101101
10111100
10000001
00110000
00111000
01110111
00001011
01101000
10101000
10010111
11111001
01101000
10101100
11001110
10100110
01011011
00101011
10011110
00000001
01000101
10010101
01111000
01111111
01111110
U
01001011
01100001
00110001
11010010
01010101
10110000
00100101
01001101
01101010
11000110
10001000
01101001
10111000
11000110
d3bba2253709f6dba0bcdd5be5dfd4e18597fe3b497c15592365f0578051a2c7
```

## Social Media

[LinkedIn](https://www.linkedin.com/in/abdelheq-mokhtari/)

[stackoverflow](https://stackoverflow.com/users/13501362/abdelheq-mokhtari)

[Twitter](https://twitter.com/Abdelheq_mokh)

[FaceBook](https://www.facebook.com/hakoo.mokhtari/) 
