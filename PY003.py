# python program to convert kilometer to miles
#1 mile = 1.6034km

value = int(input('1.enter value 1: To convert kilometer to mile\n 2.enter value 2 : To convert miles to kilometer\n'))
if value == 1:
    print('you have selected :: km to mile converstion')
    km = float(input('Enter kilometer: '))
    kmmile = km / 1.60
    print(f'Equivalent value of {km} km is{round(kmmile,2)} miles')
elif value == 2:
    print('you have selected :: miles to km converstion')
    miles = float(input('Enter miles: '))
    mileskm = miles * 1.60
    print(f'Equevalent value of {miles} km is{round(mileskm,2)} miles')
else:
    print('you have selected invalide input')