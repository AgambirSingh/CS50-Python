import re


def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    try:
        search = re.search(r"^(?P<shr>\d{1,2})(:(?P<smin>\d{2}))? (?P<spd>AM|PM) to (?P<ehr>\d{1,2})(:(?P<emin>\d{2}))? (?P<epd>AM|PM)$", s)
        if search:
            start_hour = int(search.group("shr"))
            start_minute = search.group("smin")
            start_period = search.group("spd")
            end_hour = int(search.group("ehr"))
            end_minute = search.group("emin")
            end_period = search.group("epd")

            # minutes may or may not be in user input
            if start_minute == None:
                start_minute = 0
            if end_minute == None:
                end_minute = 0
            start_minute = int(start_minute)
            end_minute = int(end_minute)

            if start_minute >= 60 or end_minute >= 60:
                raise ValueError
            elif start_hour > 12 and start_period == "PM":
                raise ValueError
            elif end_hour > 12 and  end_period == "PM":
                raise ValueError

            if "PM" in start_period and start_hour != 12:
                start_hour = int(start_hour) + 12
            if "PM" in end_period and end_hour != 12:
                end_hour = end_hour + 12
            # convert 12 AM to 0:00
            if "AM" in start_period and start_hour== 12:
                start_hour = 0
            if "AM" in end_period and end_hour == 12:
                end_hour = 0

            return(f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}")

        else:
            raise ValueError

    except AttributeError:
        raise ValueError


if __name__ == "__main__":
    main()