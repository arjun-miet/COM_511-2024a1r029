"""Aim: Write a Python program to implement a Morse Code Translator."""

morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}

choice = input("1. Text to Morse\n2. Morse to Text\nEnter choice: ")

if choice == "1":
    text = input("Enter text: ").upper()

    for word in text.split():
        for ch in word:
            print(morse[ch], end=" ")
        print("/")

elif choice == "2":
    code = input("Enter Morse code: ")
    reverse = {v: k for k, v in morse.items()}

    for word in code.split(" / "):
        for ch in word.split():
            print(reverse[ch], end="")
        print(" ", end="")

else:
    print("Invalid choice")
