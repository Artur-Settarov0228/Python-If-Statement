omonat = int(input('omonat summasini kiriting :'))
if omonat < 100000 :
    print('5%')
elif 10000 < omonat <50000 :
    print('7%')
elif omonat > 50000 :
    print('10%')
else:
    print(' boshqa % bilmayman ')