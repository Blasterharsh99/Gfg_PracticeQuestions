import pdb

def lengthOfLongestSubstring(s):
    maxi = 0
    if len(s)==0:
        return 1
    c = ""
    i=0
    while i<(len(s)):
        if i == 0:
            c += s[i]
            i+=1
        else:
            if s[i] not in c:
                c += s[i]
                i+=1
            else:
                maxi = max(maxi, len(c))
                c = ""
                i=i

    return maxi

iss=input()
print(lengthOfLongestSubstring(iss))