import numpy as np
sensor_data = np.array([ 
    2.4, 2.1, 1.8, 0.9, 0.5,
    3.2, 2.8, 2.5, 1.2, 0.7,
    4.0, 3.5, 2.9, 2.0, 1.5
    ])
print("sensor reading:", sensor_data)
print("Minimum:", np.min(sensor_data))
print("Maximum:", np.max(sensor_data))
print("Average:", np.mean(sensor_data))
danger = sensor_data < 1.0
print("Danger readings:", sensor_data[danger])
print("number of danger readings:", np.sum(danger))
danger_percentage = (np.sum(danger)/len(sensor_data))*100
print("Danger percentage:", danger_percentage, "%")