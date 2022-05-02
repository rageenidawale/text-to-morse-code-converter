# Create a dictionary that contains the letters and their morse code as the key value pair.
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
                   '-': '-....-', '(': '-.--.', ')': '-.--.-'}

# Take the input sentence from the user
sentence = input("Enter the sentence you want to encrypt: ").upper()

# Convert the sentence into a list
lst = list(sentence)

# Replace each char of the list with its morse and keep the space as is
morse_code_list = []
for char in lst:
    if char == " ":
        # adds an extra space to distinguish words from letters
        morse_code_list.append(" ")
    elif char not in MORSE_CODE_DICT:
        # char not in morse code dict are special chars and can be ignored
        pass
    else:
        morse_code_list.append(MORSE_CODE_DICT[char])

# Add space between each morse and convert it into a sentence.
morse_code_sentence = " ".join(morse_code_list)

print(morse_code_sentence)
