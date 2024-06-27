year=int(input())
month=int(input())
if month==2:
    if(year%4==0 and year%100!=0)or year%400==0:
        Days=29
    else:
        Days=28
elif month==4 or month==6 or month==9 or month==11:
    Days=30
else:
    Days=31
print(str(Days)+" Days")
