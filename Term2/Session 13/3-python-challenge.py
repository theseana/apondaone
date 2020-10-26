import string


alphabet = string.ascii_lowercase
# abcdefghijklmnopqrstuvwxyz

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

translated_text = ''

for character in text:
    if character in alphabet:
        if alphabet.index(character)+2 > 24:
            translated_text += alphabet[alphabet.index(character)+2-26]
        else:
            translated_text += alphabet[alphabet.index(character)+2]

    else:
        translated_text += character
print(translated_text)