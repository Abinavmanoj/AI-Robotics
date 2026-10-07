import numpy as np
sensor_data = np.array([ 
    [2.4, 2.1, 1.8, 0.9, 0.5],
    [3.2, 2.8, 2.5, 1.2, 0.7],
    [4.0, 3.5, 2.9, 2.0, 1.5]
    ])
print("sensor data:")
print(sensor_data)
print("shape:", sensor_data.shape)
print("Minimum:", np.min(sensor_data))
print("Maximum:", np.max(sensor_data))
print("Average:", np.mean(sensor_data))
print("Average of each scan:", np.mean(sensor_data, axis=1))