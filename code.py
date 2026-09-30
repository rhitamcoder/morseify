code_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    " ": "/"
}

def text_to_morse(text: str):
    morse_result = []
    for char in usr_in:
        morse_result.append(code_dict[char])
    return " ".join(morse_result)

print("=== Welcome to Morseify 🆘 ===")

while True:
    while True:
        usr_in = input("Kindly provide the items you want to convert into Morse: ").upper()
        if not all(char in code_dict for char in usr_in):
            print("Invalid character detected! Please try again. ⛓️‍💥")
            continue
        else:
            break

    result = text_to_morse(usr_in)
    print(result)

    again = input("Do you want to use the tool again? (y/n): ").lower()
    if again != "y":
        print("Thank You for using Morseify. ☺️")
        break
