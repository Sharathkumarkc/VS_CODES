# python program to check Leap year for given number of years
year_list = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
for year in year_list:
    if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        print(f'{year} is Leap')
    else:
        print(f'{year} is not Leap')