def alternatingCharacters(s):
    numDeletions = 0
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            numDeletions+=1
    return numDeletions

#Taking input
q = int(input())  #The number of queries
#Next q line contains string s
for i in range(q):
    s: str = input()
    print(alternatingCharacters(s))

