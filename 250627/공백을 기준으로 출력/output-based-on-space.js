const fs = require('fs');
const inputArray = fs.readFileSync(0).toString().trim().split('\n');
const input = inputArray.map((elem) => elem.split(' '));

input.forEach((array) => array.forEach((elem) => {
    process.stdout.write(elem);
}))