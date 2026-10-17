#Sum of Arithmetic Series

def sumOfSeries(n, a, d):
    return n * (2 * a + (n - 1) * d) // 2

n = int(input("Enter number of terms: "))
a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))

print("Sum of arithmetic series:", sumOfSeries(n, a, d))