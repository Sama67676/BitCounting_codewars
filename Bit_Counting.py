def count_bits(n):
    x=bin(n).replace("0b", "")
    num=0
    for i in x:
        if i=='1':
            num +=1
    return num

#or
#return bin(n).count("1")

#or 
#return bin(n)[2:].count('1')

x=int(input("Enter here: "))
print(count_bits(x))
