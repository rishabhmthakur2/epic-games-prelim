"""
Refactor this method as best you can.
public string Foobar(int a, int b)
{
int countA = 0;
for (int i = 0; i <= a; i++)
{
countA = countA + i;
}
string result = "Sum of A: ";
result += string.Format("{0}", countA);
int countB = 0;
for (int j = 0; j <= b; j++)
{
countB += j;
}
result += "; Sum of B: ";
result += string.Format("{0}", countB);
return result;
}
"""
# Refactored function in python
def foobar(a, b):
    # The original function does a sum of first n terms. First for first a terms and then first b terms.
    # Knowing that the first n terms, when added account to n * (n-1) / 2
    sumA = a * (a + 1) / 2 # Calculating sum for a
    sumB = b * (b + 1) / 2 # Calculating sum for b
    return "Sum of A: %d; Sum of B: %d" % (sumA, sumB) # Returing a string in the required format

print(foobar(5, 6))