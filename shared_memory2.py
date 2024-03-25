# shared_memory.py

import ctypes

shared_lib = ctypes.CDLL("./shared_memory.so")

# Define function prototypes
shared_lib.create_shared_memory.restype = ctypes.c_int
shared_lib.write_to_shared_memory.argtypes = [ctypes.c_int, ctypes.c_char_p]
shared_lib.read_from_shared_memory.argtypes = [ctypes.c_int]
shared_lib.read_from_shared_memory.restype = ctypes.c_char_p


# Python functions to interact with shared memory
def create_shared_memory():
    return shared_lib.create_shared_memory()


def write_to_shared_memory(shm_fd, data):
    shared_lib.write_to_shared_memory(shm_fd, data.encode())


def read_from_shared_memory(shm_fd):
    return shared_lib.read_from_shared_memory(shm_fd).decode()
