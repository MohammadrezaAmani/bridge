// consumer.js

const sharedMemory = require("./shared_memory");

// Create shared memory
const shmFd = sharedMemory.createSharedMemory();

// Consume data
setInterval(() => {
  const data = sharedMemory.readFromSharedMemory(shmFd);
  console.log("Consumed:", data);
}, 1000);

