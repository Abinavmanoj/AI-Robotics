while True:
    try:
        distance = int(input("Enter obstacle distance: "))
        print("Distance:", distance)
        
        if distance < 30:
            print("stop")
            break

        elif distance < 70:
            print("slow down")

        else:
            print("keep going fast")

    except ValueError:
        print("please enter a number.")
        break    