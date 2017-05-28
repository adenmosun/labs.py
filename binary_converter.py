def binary_converter(n):
    if (n >= 0 ) and (n <= 255):
        return str(bin(n)[2:])
    else:
        return 'Invalid input'
