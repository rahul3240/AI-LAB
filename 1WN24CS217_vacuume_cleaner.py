
def vacuum_agent(location, status_A, status_B):
    if location == 'A' and status_A == 'Dirty':
        return 'SUCK'
    elif location == 'B' and status_B == 'Dirty':
        return 'SUCK'
    elif status_A == 'Dirty':
        return 'LEFT'
    elif status_B == 'Dirty':
        return 'RIGHT'
    else:
        return 'NO-OP'


def vacuum_simulation(location, status_A, status_B):

    print("\nActions Performed:")

    while True:
        action = vacuum_agent(location, status_A, status_B)

        if action == 'NO-OP':
            print("No-Operation")
            break

        if action == 'SUCK':
            if location == 'A':
                status_A = 'Clean'
            else:
                status_B = 'Clean'

        elif action == 'LEFT':
            location = 'A'

        elif action == 'RIGHT':
            location = 'B'

        print(action, "-> Location:", location, "| Room A:", status_A, "| Room B:", status_B)

    print("\nFinal Environment:")
    print("Final Location:", location)
    print("Room A:", status_A)
    print("Room B:", status_B)


location = input("Enter initial location (A/B): ").upper()
status_A = input("Enter Room A status (Clean/Dirty): ").capitalize()
status_B = input("Enter Room B status (Clean/Dirty): ").capitalize()

vacuum_simulation(location, status_A, status_B)
