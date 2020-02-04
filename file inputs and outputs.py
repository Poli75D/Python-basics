#File inputs/outputs
var2 = open("file3.txt", "x") #jeżeli plik nie istnieje, tworzy plik w lokalizacji kodu źródłowego
print(var2.name)
var2.close()

var2 = open("file3.txt", "a") #umożliwia pisanie w pliku, wrzuca nowy tekst na początek pliku, tworzy plik w lokalizacji kodu źródłowego jeśli nie istnieje
var2.write("Hello world, connection made.")
var2.close

var2 = open("file3.txt", "w") #umożliwia pisanie w pliku, NADPISUJE zawartość, tworzy plik w lokalizacji kodu źródłowego, jeśli nie istnieje
var2.write("Hello world, connection made, you have lost previous data.")
var2.close

var2 = open("file3.txt", "r") #umożliwia odczyt danych w pliku
string1 = var2.read(2)
print(string1)
var2.close()

#Basic operations on file handling
import os
os.rename("file3.txt", "betterfile3.txt") #zwraca błąd, jeśli nie znajdzie
os.remove("file2.txt") #zwraca błąd, jeśli nie znajdzie
