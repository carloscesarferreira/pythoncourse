#Implement a function seconds(hours,mins,secs) which, given a duration in hours, minutes and seconds, calculates and returns that same duration in seconds

print("Conveting hours, minutes and seconds to seconds\n")
hour = int(input("Type HOUR: "))
minute = int(input("Type MINUTES: "))
second = int(input("Type SECOND: "))
print("\n")

def radians(hour, minute, second):
    hour = hour * 3600
    minute = minute * 60
    second = hour + minute + second
    return second

s = radians(hour, minute, second)

print(hour,":h", minute,":min", second,":sec, correspond to ", s,"seconds")
print("\n")
