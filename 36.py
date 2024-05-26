#36 removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
a = "py;th* o:n ! ;py * t*h:o !n"

for i in a:
    if i.isalpha():
        print(i,end="")