import struct


def binary(f):
    s = struct.pack('>f', f)
    return struct.unpack('>i', s)[0]



def float_number(num1, num2):
    onebits = binary(float(num1))
    twobits = binary(float(num2))
    print(onebits)
    print(twobits)
    sign1 = (onebits >> 31) & 1
    print(sign1)
    sign2 = (int(twobits) >> 31) & 1
    print(sign2)
    expo1 = int((int(onebits) >> 23) & 255)
    expo2 = int((int(twobits) >> 23) & 255)
    mantisa1 = int(int(onebits) & (int(pow(2, 23) - 1)))
    mantisa2 = int(int(twobits) & (int(pow(2, 23) - 1)))
    mantisa3 = ((1 << 23) | int(mantisa1)) * ((1 << 23) | int(mantisa2))
    print('MANTISA MULTIPLICATION')
    print('num 1 mantisa', f'{int(mantisa1):024b}', '\nX')
    print('num 2 mantisa', f'{int(mantisa2):024b}')
    print('Mantisa Multiplication  =', f'{int(mantisa3):048b}')
    mantisa3 = int(mantisa3) >> 23
    expoaddition = (1 if (1 << 24) & int(mantisa3) > 0 else 0)

    print('-----------------')
    if expoaddition > 0:
        print('Nomalize')
        mantisa3 = int(mantisa3) >> 1
        mantisa3 = int(mantisa3) & (~(1 << 23))  #
    else:
        print('NO Normalization needed')
        mantisa3 = int(mantisa3) & (~(1 << 23))  #

    print(f'{int(mantisa3):023b}')

    sign = 1 & (sign1 + sign2)
    print('sign:', sign1, 'XOR', sign2, ' = ', sign, '\n')

    print('exponent:')
    print('exp1', f'{int(expo1):08b}')
    print('exp2', f'{int(expo2):08b}')

    expo = int(expo1) + int(expo2) - 127 + int(expoaddition)
    print('-127 +', expoaddition, '\n=', f'{int(expo):08b}', '-----', int(expo))

    resultmask = int(mantisa3)
    resultmask = int(resultmask) | (expo << 23)
    resultmask = int(resultmask) | (sign << 31)

    aaaa= float(pow(-1,sign)*pow(2,expo-127)*(1+(mantisa3/pow(2,23)))) #float
    print(aaa)
    print(f'{int(resultmask):032b}')











print("input float numbers")
num1 = input('1st float :')
num2 = input('2nd float :')
# print(f'{binary(float(num1)):032b}')
float_number(num1, num2)
