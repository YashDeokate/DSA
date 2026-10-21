# Question: Write a Python program to check whether
# two given strings are isomorphic or not.

def isIsomorphic(s, t):
    map1 = {}
    map2 = {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] in map1 and map1[s[i]] != t[i]:
            return False

        if t[i] in map2 and map2[t[i]] != s[i]:
            return False

        map1[s[i]] = t[i]
        map2[t[i]] = s[i]

    return True


s = input("Enter first string: ")
t = input("Enter second string: ")

print(isIsomorphic(s, t))