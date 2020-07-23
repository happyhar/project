import time
run = raw_input("Start? > ")
mins = 0
# Only run if the user types in "start"
timing = input("Enter the timings")
if run == "start":
    # Loop until we reach  minutes running
    while mins != int(timing):
        print("You were Deceived. Your Time Is Over At {}".format(mins))
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1
    # Bring up the dialog box here
