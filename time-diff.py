from datetime import datetime, timedelta

# get user input
startStr = input("Enter start time(H:M:S): ")
endStr = input("Enter end time(H:M:S): ")

# convert time string to datetime
start = datetime.strptime(startStr, '%H:%M:%S')
end = datetime.strptime(endStr, '%H:%M:%S')

# print result
if end > start:
    print("Time diff: " + str(end - start))
    print("Seconds:" + str((end - start).total_seconds()))
else:
    print("Time diff: " + str(end - start + timedelta(days=1)))
    print("Seconds: " + str((end - start).total_seconds() + 86400))