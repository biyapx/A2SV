# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

def dec_to_bin(num):
    if num == 0:
        return ""
    else:
        bit = num % 2
        num = num // 2
        return dec_to_bin(num) + str(bit)