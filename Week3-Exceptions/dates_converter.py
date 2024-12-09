month_list=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#prompts the user for a date in month-day-year order, formatted like 9/8/1636 or September 8, 1636
while True:
    date=input("Date: ")

    try:
        m,d,y= date.strip().split("/") #strip to remove whitespace and split fnc. to get 3 different inputs

        if int(d)<=31 and int(m)<=12: #adding conditions for days and months
            print(f"{y}-{int(m):02}-{int(d):02}")
            break

    except ValueError: # Exception to catch date like December 2, 2024
        mm,dd,yyyy=date.split(" ")
        month= month_list.index(mm)+1
        dd=int(dd.strip(","))

        if int(dd)<=31 and month<=12:
            print(f"{yyyy}-{month:02}-{dd:02}") #formating
            break