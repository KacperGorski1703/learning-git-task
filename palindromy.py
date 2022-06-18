def palindromy(word):
    result = word[::-1].lower() == word.lower()
    print(result)
palindromy("kajak")

palindromy("kanapka")

palindromy("Kajak")