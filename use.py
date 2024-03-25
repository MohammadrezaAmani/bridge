# producer.py

import time
import shared_memory2

# Create shared memory
shm_fd = shared_memory2.create_shared_memory()

# Produce data
for i in range(10):
    data = f"Data from Python {i}"
    shared_memory2.write_to_shared_memory(shm_fd, data)
    print(f"Produced: {data}")
    time.sleep(1)

# Close shared memory
import os

os.close(shm_fd)
