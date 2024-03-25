// shared_memory.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

#define SHM_SIZE 1024

int create_shared_memory() {
    int shm_fd = shm_open("/my_shared_memory", O_CREAT | O_RDWR, 0666);
    if (shm_fd == -1) {
        perror("shm_open");
        exit(1);
    }
    ftruncate(shm_fd, SHM_SIZE);
    return shm_fd;
}

void write_to_shared_memory(int shm_fd, char* data) {
    void* ptr = mmap(0, SHM_SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (ptr == MAP_FAILED) {
        perror("mmap");
        exit(1);
    }
    memcpy(ptr, data, strlen(data) + 1);
    munmap(ptr, SHM_SIZE);
}

char* read_from_shared_memory(int shm_fd) {
    void* ptr = mmap(0, SHM_SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);
    if (ptr == MAP_FAILED) {
        perror("mmap");
        exit(1);
    }
    char* data = (char*)malloc(SHM_SIZE);
    strcpy(data, (char*)ptr);
    munmap(ptr, SHM_SIZE);
    return data;
}
