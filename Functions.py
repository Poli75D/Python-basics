#Funkcja powitalna
def PolusFnctn():
    name1 = input('Wpisz swoje imię: ')
    print('Witaj,',name1.capitalize())
    return
PolusFnctn()

#Funkcja dodawania
def AdditionFtn(number1, number2):
    return number1 + number2
print(AdditionFtn(10,12))

#Funkcja z domyślną wartością zmiennej
def DefaultFtn(x = 2):
    return x
print(DefaultFtn(3))
print(DefaultFtn())

#Funkcja powitalna z domyślną wartością
def PolusFtn2(name2 = 'Bezimienny'):
    name2 = input('Wpisz swoje imię: ')
    str2 = 'Witaj, '
    return str2 + name2
print(PolusFtn2()) #nie zadziała, ponieważ pusty input jest traktowany jako nullstring, nadpisuje brak wartości

#Funkcja powitalna z domyślną wartością 2
def PolusFtn3():
    name3 = input('Wpisz swoje imię: ')
    if name3 == '':
        name3 = 'bezimienny'
    str3 = 'Witaj, '
    print(str3 + name3.capitalize())
    return str3 + name3
PolusFtn3()
    
