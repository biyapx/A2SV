# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

def printn(n):
    if n>0:
        printn(n-1)
        print(n)
