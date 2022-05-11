import sounddevice as sd
import soundfile as sf
import numpy as np
from scipy.io.wavfile import write

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

# Listen and record the morse code
dot = 'sounds/dot.wav'
dash = 'sounds/dash.wav'
space = 'sounds/space.wav'
# Create and array to create a combined audio
sound_array = []
# Create a pause to distinguish between each character
pause = np.zeros([20000, 2], dtype="float32")

for code in morse_code_sentence:
    if code == ".":
        data, fs = sf.read(dot)
    elif code == "-":
        data, fs = sf.read(dash)
    else:
        data, fs = sf.read(space)

    # Append the sounds whether dot/dash/space to the sound array
    sound_array.append(sd.playrec(data,
                                  fs,
                                  channels=2,
                                  dtype="float32",
                                  blocking=True))
    # Append a pause after each character
    sound_array.append(pause)

# Create a numpy array
new = np.vstack(sound_array)
# Write this numpy array to the output.wav file
write(f'output.wav', 44100, new)
