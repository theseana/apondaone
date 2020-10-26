import string


alphabet = string.ascii_lowercase
new_alphabet = 'cdefghijklmnopqrstuvwxyzab'

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

mytable = text.maketrans(alphabet, new_alphabet)
print(text.translate(mytable))