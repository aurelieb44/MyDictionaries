content = open("info_security.txt", "r")

content_file = content.read()

outfile = open("encrypted.txt", "w")

alphabet = {
    "A": "@",
    "a": "#",
    "B": "1",
    "b": "&",
    "C": "§",
    "c": "4",
    "D": "8",
    "d": "(",
    "E": "=",
    "e": "^",
    "F": "!",
    "f": "$",
    "G": "%",
    "g": "9",
    "H": "+",
    "h": "7",
    "I": "-",
    "i": ")",
    "J": "5",
    "j": ":",
    "K": "3",
    "k": "2",
    "L": "?",
    "l": ";",
    "M": "<",
    "m": "6",
    "N": "*",
    "n": "€",
    "O": ">",
    "o": ",",
    "P": "'",
    "p": ".",
    "Q": "/",
    "q": "_",
    "R": "£",
    "r": "ù",
    "S": "é",
    "s": "ô",
    "T": "è",
    "t": "}",
    "U": "¿",
    "u": "µ",
    "V": "{",
    "v": "‡",
    "W": "ß",
    "w": "¶",
    "X": "Ñ",
    "x": "©",
    "Y": "¥",
    "y": "Þ",
    "Z": "ø",
    "z": "ñ",
}


for letter in content_file:
    if letter in alphabet:
        outfile.write(alphabet[letter])  # printing encrypted text
    else:
        outfile.write(letter)  # printing spaces,commas, periods...

outfile.close()
