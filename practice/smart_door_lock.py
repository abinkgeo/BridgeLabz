def door_lock(correct, attempts):
    for attempt in attempts:
        if attempt == correct:
            return "ACCESS GRANTED"
    return "LOCKED"

correct_pin = input("Enter the correct pin")
attempts = [input("Enter the pin"), input("Enter the pin"), input("Enter the pin")]
print(door_lock(correct_pin, attempts))
