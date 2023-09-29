#Create an elevator program using python in array

currentFloor = int(input("Your current floor: "))
floorLevels = ["Ground Floor", "1st Floor", "2nd Floor", "3rd Floor", "4th Floor", "5th Floor"]

while True:
    destination = int(input("Which floor do you want to go? : "))
    while True :
        if currentFloor < destination:
            currentFloor = currentFloor + 1
        elif currentFloor > destination:
            currentFloor = currentFloor - 1
        if currentFloor == destination:
            print(f"Now on you're destination which is {floorLevels[currentFloor]}")
            break
        print(f" Currently in this floor {floorLevels[currentFloor]}")
