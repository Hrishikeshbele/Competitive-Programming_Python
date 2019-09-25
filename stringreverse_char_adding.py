'''
Jack is awesome. His friends call him little Einstein. To test him, his friends gave him a string. They told him to add the string with its reverse string and follow these rules:

Every ith character of string will be added to every ith character of reverse string.
Both string will contain only lower case alphabets(a-z).
problem explanation:
ex. hello
h e l l o is a string of character (important it should be lower case ) so here is the algorithm to convert h e l l o to w q x q w
first if you take a look at place of h e l l o in numeric order in a to z you can simply map them so
h = 8
e = 5
l = 11
l = 11
o = 15
now take a look what first point in detail tell us
1. Every ith character of string will be added to every ith character of reverse string.
so in these case
h is 1st , e is 2nd , l is 3rd , l is 4th , o is 5th
so 1st + 5th = (place of h + place of o ) = 8 + 15 = 23,you will see that 23rd place belongs to w.
and if sum of index is exceeding the 26 then just start from 1 again i.e substract 26 from sum.
'''
#no of input strings
n=int(input())
for i in range(n):
    str=list(input())
    #reverse string of input string
    str2=list(str[::-1])
    #storing ordinal value of each char in string as list
    str = [ord(i) for i in str]
    str2= [ord(i) for i in str2]
    k = []
    ans=''
    for j in range(len(str)):
        #getting sum of index of char from str and its reverse string like 1 for a
        m=(str[j]+str2[j]-96*2)
        #if sum is < 26 append char corrs that index to k
        if m <= 26:
            k.append(chr(m+96))
        #if sum is > 26 substract 26 from sum and then append corresp char
        elif m > 26:
            m = m-26
            k.append(chr(m+96))
    s = ''
    #creating string of char in k
    for item in k:
        s += item
    print(s)
