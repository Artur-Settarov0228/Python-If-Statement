raqam = int(input('raqaminzni kiriting men sizga qaysi kampaniyaligini aytib berman :'))
kod = raqam[:2]
#birnchi urinda bosh kodini ajratibb olamiz
if kod in ['90' , '91']:
    print('Beeline')
elif kod in ['93' , '94']:
    print('ucell')
elif kod in ['88']:
    print('Mobiuz')
else:
    print("boshqa opiratorlani bilmayman uzur")
