#Longest Common Prefix
def longestCommonPrefix(strs):
    prefix = strs[0]

    for s in strs:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix


strs = input("Enter words separated by spaces: ").split()
print(longestCommonPrefix(strs))