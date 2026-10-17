#Q1. Highest Occurring Element in an Array

def highestOccurringElement(nums):
    freq = {}

    for i in nums:
        freq[i] = freq.get(i, 0) + 1

    max_count = max(freq.values())

    for i in sorted(freq):
        if freq[i] == max_count:
            return i

nums = list(map(int, input("Enter numbers: ").split()))
print("Highest occurring element:", highestOccurringElement(nums))

#Q2. Second Highest Occurring Element in an Array

def secondHighestOccurringElement(arr):
    freq = {}

    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    counts = sorted(set(freq.values()), reverse=True)

    if len(counts) < 2:
        return -1

    second = counts[1]

    for i in sorted(freq):
        if freq[i] == second:
            return i

arr = list(map(int, input("Enter numbers: ").split()))
print("Second highest occurring element:", secondHighestOccurringElement(arr))


# sum of frequencies of highest and lowest occurring elements in an array

def sumOfFrequencies(arr):
    freq = {}

    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    highest = max(freq.values())
    lowest = min(freq.values())

    return highest + lowest

arr = list(map(int, input("Enter numbers: ").split()))
print("Sum of frequencies:", sumOfFrequencies(arr))