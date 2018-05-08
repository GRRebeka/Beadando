
###Write a program that automatically converts English text to Morse code and vice versa###



morse_abc={'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..',
'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-',
'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..',
'0': '-----', '1': '.----', '2': '..---',
'3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..',
'9': '----.', '!':'--.--', ',':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-'}

def encode(code):

    szoveg=code.upper()
    morse = ''
    for i in szoveg:
        for kulcs,ertek in morse_abc.items():
            if i == kulcs:
                morse+=ertek+' '

    # for szo in szoveg:
    #     for betu in szo.split(' '):
    #         morse +=morse_abc[betu]
    #     morse += '|'
    print(morse)


def decode(code):
    betu = code.split(' ')
    eng_txt = ''
    for i in betu:
        for kulcs, ertek in morse_abc.items():
            if i == ertek:
                eng_txt += kulcs
        eng_txt+=' '
    print(eng_txt)


code=input('Add meg a szoveget: ')
if code[0]=='.' or code[0]=='-' :
    decode(code)
else:
    encode(code)
