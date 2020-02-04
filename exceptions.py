def Function1(var1):
    assert(var1 != 0), "Value 0 denies access" #niedozwolone wartości funkcji, skutkuje wyświetleniem błędu z opisem jako podany tekst za nawiasem
    return 10/var1

print(Function1(4))

try:
    file = open("text.txt", "r") #istniejący plik
    file.write("Hi")
except IOError:
    print("File not found, sorry mate")
else:
    print("OK dude")
    file.close()

try:
    file = open("text2.txt", "r") #nieistniejący plik
    file.write("Hi")
except IOError:
    print("File not found, sorry mate")
else:
    print("OK dude")
    file.close()
