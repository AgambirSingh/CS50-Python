def main():
    # Prompt the user to input a time
    time = input("Time: ")
    # Convert the input time to a float representing hours
    converted_time = convert(time)
    # Check the converted time and print the corresponding meal time
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")

def convert(time):
    # Split the input time into hours and minutes
    hr, min = time.split(":")
    # Convert hours to an integer
    hr = int(hr)
    # Convert minutes to a fraction of an hour
    min = (int(min) / 60)
    # Sum hours and fractional hours to get the total time in hours
    time = hr + min
    return time

# Ensure the main function is called when the script is executed
if __name__ == "__main__":
    main()
