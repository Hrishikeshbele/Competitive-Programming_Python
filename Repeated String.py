'''
problem : hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

'''
# Complete the repeatedString function below.
def repeatedString(s, n):
    ans=0 # count no of a in whole string
    k=0 # count no of a in extra string 
    z=0 # count no of a in short string if n<len(s)
    for i in s:
        if i=='a':
            ans+=1
    if n<len(s):
        for j in s[:n]:
            if j=='a':
                z+=1
        return z
    else:
        for j in s[:n%len(s)]:
            if j=='a':
                k+=1
        return ans*(n//len(s))+k
    
    
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
