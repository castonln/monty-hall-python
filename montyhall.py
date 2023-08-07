# Monty Hall Sim
from random import randint, choice

door = [False, False, True]
door_dict = {0: False, 1: False, 2: True}
simulations = int(input("Simulations to run: "))


print("\n--- No Switch ---")

no_switch_wins = 0
for i in range(simulations):
    selection = randint(0,2)
    
    if door[selection]:
        no_switch_wins += 1

print(f"Win rate: {no_switch_wins / simulations * 100:.2f}%\n")


print("--- Switch ---")

switch_wins = 0
for i in range(simulations):
    selection = randint(0,2)
    
    if door[selection]:
        continue
    else:
        switch_wins += 1

print(f"Win rate: {switch_wins / simulations * 100:.2f}%\n")


print("--- Switch 2 (My favorite explaination) ---")

switch_wins = 0
for i in range(simulations):
    selection = randint(0,2)
    
    door_options = [0, 1, 2]    # indexes for our doors

    # the host knows what's right and what's wrong. here's what they see

    for door_option, value in enumerate(door):      # ...the host must evaluate the rest of the doors
        if door_option == selection:
            continue                                # they cannot reveal what's behind our selection. that would be pointless
        elif value == True:
            continue                                # they cannot reveal the winning door. that would be pointless
        else:
            revealed_door = door_option             # they have to reveal what's left: a door we didn't select that doesn't win

    door_options.remove(selection)      # we make the assumption our door is wrong (this is right 2/3 of the time)
    door_options.remove(revealed_door)  # we know the revealed door is always wrong
    switch_selection = door_options[0]  # this is not door #0. door_options now contains only one item. this is that item

    # hopefully you can see now that because the host can only reveal non-winning doors, we always choose the winning door if we happen to select the wrong door
    # you have a 1/3 chance of selecting the right door first (and then switching to a wrong door)
    # you have a 2/3 chance of selecting the wrong door first (and then switching to a right door)

    if door[switch_selection]:
        switch_wins += 1
    
print(f"Win rate: {switch_wins / simulations * 100:.2f}%\n")


print("--- Switch 3 (Right vs wrong first selection) ---")

switch_wins = 0
for i in range(simulations):
    selection = randint(0,2)
    
    door_options = [0, 1, 2]    # indexes for our doors

    # the host knows what's right and what's wrong. here's what they see

    if door[selection] == True:     # if we chose the right door...
        revealed_door = choice(door_options[:selection] + door_options[selection+1:])   # ...the other two doors are wrong and it doesn't matter what the host shows
        switch_selection = [door_option for door_option in door_options if door_option != selection and door_option != revealed_door][0]    # and by consequence, our selection is wrong

    else:   # if we chose a wrong door...
        revealed_door = [door_option for door_option in door_options if door_option != selection and door[door_option] != True][0]  # ...the host cannot reveal the correct door
        switch_selection = [door_option for door_option in door_options if door_option != selection and door_option != revealed_door][0]    # so we choose the correct door every time we select a wrong door!

    # hopefully you can see now that because the host can only reveal non-winning doors, we always choose the winning door if we happen to select the wrong door
    # you have a 1/3 chance of selecting the right door first (and then switching to a wrong door)
    # you have a 2/3 chance of selecting the wrong door first (and then switching to a right door)

    if door[switch_selection]:
        switch_wins += 1
    
print(f"Win rate: {switch_wins / simulations * 100:.2f}%\n")


print("--- Switch 4 (Switch 2 w/ list comprehension) ---")

switch_wins = 0
for i in range(simulations):
    selection = randint(0,2)
    
    door_options = [0, 1, 2]    # indexes for our doors

    # the host knows what's right and what's wrong. here's what they see

    for door_option, value in enumerate(door):      # ...the host must evaluate the rest of the doors
        if door_option == selection:
            continue                                # they cannot reveal what's behind our selection. that would be pointless
        elif value == True:
            continue                                # they cannot reveal the winning door. that would be pointless
        else:
            revealed_door = door_option             # they have to reveal what's left: a door we didn't select that doesn't win

    switch_selection = [door_option for door_option in door_options if door_option != selection and door_option != revealed_door][0]

    # hopefully you can see now that because the host can only reveal non-winning doors, we always choose the winning door if we happen to select the wrong door
    # you have a 1/3 chance of selecting the right door first (and then switching to a wrong door)
    # you have a 2/3 chance of selecting the wrong door first (and then switching to a right door)

    if door[switch_selection]:
        switch_wins += 1
    
print(f"Win rate: {switch_wins / simulations * 100:.2f}%\n")