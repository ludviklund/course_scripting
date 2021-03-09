import json
import re


def calendar():
    programs = {}
    days = ("monday", "tuesday", "wednesday",
            "thursday", "friday")
    hours = {"01:00": "", "02:00": "", "03:00": "", "04:00": "",
             "05:00": "", "06:00": "", "07:00": "", "08:00": "",
             "09:00": "", "10:00": "", "11:00": "", "12:00": "",
             "13:00": "", "14:00": "", "15:00": "", "16:00": "",
             "17:00": "", "18:00": "", "19:00": "", "20:00": "",
             "21:00": "", }
    for day in days:
        programs[day] = hours

    while True:
        print("s - Store program\nl - List daily program\nx - Exit")
        val = input("Choose from the list: ")
        if val == "s":
            day = input("Which day?: ")
            hour = input("What time: ") + ":00"
            program = input("What is the program?: ")
            programs[day][hour] = program
        elif val == "l":
            day = input("Which day?: ")
            for i in programs[day]:
                print(i + " " + programs[day][i])
        elif val == "x":
            break
        else:
            print("Unknown command.")


def wordsused():
    count = {}
    file = open(
        "/Users/ludviklund/Documents/Skole/Scripting/lab2/python.txt").read()
    clean_string = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,\n]", '', file).split()
    for word in clean_string:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    for k, v in count.items():
        if v > 2:
            print(k, ":", v)


def main():
    print("Remove comment for the task you want to test.")
    # calendar()
    # wordsused()


if __name__ == "__main__":
    main()
