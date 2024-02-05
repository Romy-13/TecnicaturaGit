def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char

    return nuevo_texto


def es_palindromo(texto):
    texto = no_space(texto)
    print(texto)


es_palindromo = "Amo la paloma"

print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
