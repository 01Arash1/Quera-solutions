n = int(input())

i = n//2
j = 1

while i>=1 :
    print ( i*' '+j*'*'+i*2*' '+j*'*' )
    i-=1
    j+=2

print(n * 2 * '*') 

i = n//2
j = 1

while i >= 1 :
    print( j*' '+(i*2-1)*'*'+j*2*' '+(i*2-1)*'*' )
    j += 1
    i -= 1