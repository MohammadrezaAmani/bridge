import ctypes


DLL_PATH = "../utils/shared_memory.so"

shared_lib = ctypes.CDLL(DLL_PATH)

shared_lib.create_shared_memory.restype = ctypes.c_int
shared_lib.write_to_shared_memory.argtypes = [ctypes.c_int, ctypes.c_char_p]
shared_lib.read_from_shared_memory.argtypes = [ctypes.c_int]
shared_lib.read_from_shared_memory.restype = ctypes.c_char_p


def create_shared_memory():
    """
    Creates a shared memory object.

    Returns:
        The created shared memory object.
    """
    return shared_lib.create_shared_memory()


def write_to_shared_memory(shm_fd, data):
    """
    Writes data to the shared memory identified by shm_fd.

    Args:
        shm_fd (int): The file descriptor of the shared memory.
        data (bytes): The data to be written to the shared memory.

    Returns:
        None
    """
    shared_lib.write_to_shared_memory(shm_fd, data)


def read_from_shared_memory(shm_fd):
    """
    Reads data from the shared memory identified by the given file descriptor.

    Args:
        shm_fd (int): The file descriptor of the shared memory.

    Returns:
        The data read from the shared memory.

    """
    return shared_lib.read_from_shared_memory(shm_fd)
