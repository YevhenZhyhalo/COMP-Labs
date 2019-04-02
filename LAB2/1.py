def multiply(num1,num2):
    multiplier = num1
    multiplicand =num2
    product =0
    for i in range(32):
        print('Step',i+1,':')
        print('MULTIPLICAND\n',f'{int(multiplicand):064b}','\n MULTIPLIER \n',f'{int(multiplier):064b}')
        lsb = int(int(multiplier)&1)

        if lsb ==1 :
            product += int(multiplicand)
            print('ADD Multiplicand and Product')
        print('Product: \n',f'{int(product):064b}')
        print("Shift multiplicand left")
        print("Shift multiplier right")
        multiplicand = int(multiplicand)<< 1
        multiplier = int(multiplier )>> 1

        print('MULTIPLICAND\n',f'{int(num1):064b}','\n MULTIPLIER \n',f'{int(num2):064b}')
        print('Product: \n', f'{int(product):064b}')
        print(num1 , " x ", num2  ," = " , product)


print("input numbers")
num1 = input('1st :')
num2 = input('2nd :')
multiply(num1,num2)
#'190'.ljust(8, '0')

