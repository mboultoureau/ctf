import base64

off = "RV7WSVLWe1q4XzviYk[3X{3iQVXWXzO}bnP|eYC6MUDxfR?@"

def reverseCommentCaVa(value):
    result = ""
    for index, letter in enumerate(value):
        result += chr(ord(letter) - index % 4)

    return base64.b64decode(result).decode("utf-8")

print(reverseCommentCaVa(off))