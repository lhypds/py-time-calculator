from datetime import datetime

# get user input
startStr = input("Enter start time(H:M:S): ")
endStr = input("Enter end time(H:M:S): ")

# convert time string to datetime
start = datetime.strptime(startStr, '%H:%M:%S')
end = datetime.strptime(endStr, '%H:%M:%S')

# print result
print("Start: " + str(start))
print("End: " + str(end))
print("Time diff: " + str(end - start))
print("Seconds:" + str((end - start).total_seconds()))
