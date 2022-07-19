# -*- coding: utf-8 -*-

def is_palindrome(words:str):
    return words == words[::-1]


if __name__ == "__main__":
    print("esto es un palindromo ?")
    word_input = input("Ingrese palabra para averiguar")
    try:
        word_input = word_input.replace(" ","").lower()
        if is_palindrome(word_input):
            print("Es palindromo")
        else:
            print("No es palindromo")
    except e:
        print("Existe un error",e)