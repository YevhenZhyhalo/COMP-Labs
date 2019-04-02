def divide(num1,num2):

    remainderAndQuotient=int(num1)
    divisor = int(num2)
    product =0
    divisor = int(divisor) << 32
    SetLSBone = False
    for i in range(33):
        print('Step',i+1,':')
        print('Divisor is')
        if int(divisor) <= int(remainderAndQuotient):
            remainderAndQuotient = remainderAndQuotient - divisor
            SetLSBone =True
            print('less')
        else:
            print('more')
        print('then remainder\n','Shift remainder left')
        remainderAndQuotient = int(int(remainderAndQuotient)<<1)

        if SetLSBone==True:
            SetLSBone=False
            remainderAndQuotient =int(int(remainderAndQuotient)|1)
            print('Set remainder lsb to 1')


        print('\nDIVISOR\n',f'{int(divisor):064b}','\n REMAINDER AND QUOTIENT \n',f'{int(remainderAndQuotient):064b}')
    quoitient = int(int(remainderAndQuotient)&(pow(2, 33)-1))
    remainder =int( int(remainderAndQuotient)>>33)
    print('QUOTIENT\n', f'{int(quoitient):064b}', quoitient, '\nREMAINDER \n', f'{int(remainder):064b}',remainder)


print("input numbers")
num1 = input('1st :')
num2 = input('2nd :')
divide(num1,num2)

