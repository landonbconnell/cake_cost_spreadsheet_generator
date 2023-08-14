# converts pounds and gallons to ounces
def convertToOunces(size):
    parts = size.split()
    number = parts[0]
    unit = parts[1]

    if "/" in number:
        numerator, denominator = number.split("/")
        number = float(numerator) / float(denominator)
    else:
        number = float(''.join(filter(lambda x: x.isdigit() or x == '.', number)))

    if "lb" in size or "lbs" in size:
        size = number * 16
    elif "gal" in size:
        size = number * 128
    elif "can" in size:
        size = number * 8
    else:
        size = number

    return size
