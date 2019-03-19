#! /usr/bin/python
def Encode(data):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
    bit_str = ""
    base64_code = ""

    for char in data:
        bin_key = bin(char).lstrip("0b")
        bin_key = bin_key.zfill(8)
        bit_str += bin_key

    brackets = [bit_str[x:x+6] for x in range(0,len(bit_str),6)]

    for bracket in brackets:
        if(len(bracket) < 6):
            bracket = bracket + (6-len(bracket))*"0"
        base64_code += alphabet[int(bracket,2)]


    if(len(brackets) != 76 and len(brackets) % 3 == 2):
        base64_code += "="
    if(len(brackets) != 76 and len(brackets) % 3 == 1):
        base64_code += "=="

    return base64_code

def make(filename):
    w = open(filename + 'base.txt', "w")
    with open(filename + '.txt', "rb") as f:
        byte = f.read(57)
        while byte:
            w.write(Encode(byte))
            w.write("\n")
            byte = f.read(57)
        w.close()
    f.close()

make('evangelie')
make('tiger')
make('uganda')
