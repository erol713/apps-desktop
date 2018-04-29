import string

def alphabet_number(text):
    slova=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    result = []
    for n in text:
        for i,l in enumerate(slova):
            if n==l:
                result.append(slova.index(l)+1)
        for i in result:
            if i>26:
                result[result.index(i)] = i-26
    string_result= " ".join(str(x) for x in result)
    print("´" + string_result + "´")

alphabet_number("The sunset sets at twelve o' clock.")
