const path = require("path");
const vm = require("vm");

async function runFunction(obj) {
  const filePath = path.resolve(__dirname, obj.path);
  console.log(filePath);
  const script = new vm.Script(`
        const obj = require("${filePath}");
        const func = obj.${obj.func};
        console.log(obj)
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

  const result = script.runInNewContext(context);

  console.log("Output:", result);
}

const obj = {
  path: "./script.js",
  sha: "f3b4e4e6d5f4c3f5b",
  func: "hello",
  args: ["Alice", 30],
};

runFunction(obj);
