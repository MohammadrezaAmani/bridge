const path = require("path");
const vm = require("vm");
const sharedMemory = require("./shared_memory");

const shmFd = sharedMemory.createSharedMemory();

async function runFunction(obj) {
  sharedMemory.writeToSharedMemory(shmFd, "");
  const filePath = path.resolve(__dirname, obj.path);
  console.log(filePath);
  const script = new vm.Script(`
        const obj = require("${filePath}");
        const func = obj.${obj.name};
        console.log(func)
        const result = func(...${JSON.stringify(obj.args)});
        result;
    `);

  const context = {
    require,
    console,
    JSON,
    setTimeout,
    setInterval,
    setImmediate,
  };

  const result = {
    result: script.runInNewContext(context),
    op: "response",
    uuid: obj.uuid,
  };
  sharedMemory.writeToSharedMemory(shmFd, JSON.stringify(result));
  console.log(JSON.stringify(result));
}

const obj = JSON.parse(sharedMemory.readFromSharedMemory(shmFd));
runFunction(obj);
