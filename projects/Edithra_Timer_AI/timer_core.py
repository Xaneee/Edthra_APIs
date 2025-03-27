# Edithra Timer Core


# Mutation (2025-03-26T09:38:28.786468):



# Mutation (2025-03-26T09:48:17.642437):
import time

def countdown(minutes):
    for i in range(minutes, 0, -1):
        print(f"{i} minutes remaining")
        time.sleep(60)

countdown(5)

