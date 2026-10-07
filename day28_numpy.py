import numpy as np
sensor_data = np.array([15, 60, 80,12,4,38])
print("sensor data:", sensor_data)
print("Number of reading:", len(sensor_data))
print("maximum:", np.max(sensor_data))
print("minimum:", np.min(sensor_data))
print("Average:", np.mean(sensor_data))