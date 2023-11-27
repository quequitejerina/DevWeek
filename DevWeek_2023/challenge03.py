import sys


phrase = 'theA4dxboA3d9xMlXjpA23@Mx45SjpsN"M@tkSD8,j+%zfA52[EMyN05MbD5QrZ5uSOM=s94A71rN MSXgUA26fA2a"XgU&f*"'
tokens = "ADIMNSX"


def decode(phrase):
    for token in tokens:
        idx = phrase.find(token)
        if idx >= 0:
            print(token)
            if token == "A":
                analyse = phrase[idx + 1 : idx + 3]
                replace_with = chr(int(analyse, 16))
                phrase = phrase.replace(f"{token}{analyse}", replace_with, 1)
                return phrase
            elif token == "D":
                amount = int(phrase[idx + 1])
                analyse = phrase[idx + 1 : idx + amount + 2]
                replace_with = ""
                phrase = phrase.replace(f"{token}{analyse}", replace_with, 1)
                return phrase
            elif token == "I":
                end_idx = phrase.find(token)
                amount = int(phrase[end_idx + 1])
                analyse = phrase[idx + 1 : end_idx]
                replace_with = analyse * amount
                phrase = phrase.replace(
                    f"{token}{analyse}{token}{amount}", replace_with, 1
                )
                return phrase
            elif token == "M":
                end_idx = phrase[idx + 1 :].find(token) + (idx + 1)
                analyse = phrase[idx + 1 : end_idx]
                replace_with = analyse.upper()
                phrase = phrase.replace(f"{token}{analyse}{token}", replace_with, 1)
                return phrase
            elif token == "N":
                analyse = phrase[idx + 1]
                replace_with = chr(ord(analyse) + 1)
                phrase = phrase.replace(f"{token}{analyse}", replace_with, 1)
                return phrase
            elif token == "S":
                end_idx = phrase[idx + 1 :].find(token) + (idx + 1)
                analyse = phrase[idx + 1 : end_idx]
                replace_with = ""
                for char in analyse:
                    replace_with += char.lower() if char.isupper() else char.upper()
                phrase = phrase.replace(f"{token}{analyse}{token}", replace_with, 1)
                return phrase
            elif token == "X":
                end_idx = phrase[idx + 1 :].find(token) + (idx + 1)
                analyse = phrase[idx + 1 : end_idx]
                replace_with = ""
                phrase = phrase.replace(f"{token}{analyse}{token}", replace_with, 1)
                phrase = phrase.replace(f"{analyse}", replace_with)
                return phrase
    sys.exit()


while True:
    phrase = decode(phrase)
