# python program to convert degree,minutes and seconds into decimal degree

degree = int(input('Enter degree::: '))
minutes = int(input('Enter minutes::: '))
seconds = float(input('Enter seconds::: '))


if minutes < 60 and seconds < 60 :
    dd= degree + (minutes/60) + (seconds/3600)
