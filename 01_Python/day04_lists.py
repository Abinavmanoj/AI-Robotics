distance = [ 10 , 20 , 25, 40 , 12 , 60 , 70 , 13 , 90 , 100 ]
danger_count = 0
safety_count = 0
fast_count = 0

for d in distance:
    if d < 30:
        print("stop")
        danger_count = danger_count + 1
    elif 30 <= d <= 70:
        print("move slow")
        safety_count = safety_count + 1
    else:
        print("move fast")
        fast_count = fast_count + 1

print("Dangerous readings:", danger_count)
print("Safety readings:", safety_count)
print("Fast readings:", fast_count)