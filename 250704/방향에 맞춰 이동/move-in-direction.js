const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const moves = input.slice(1);

// Please Write your code here.

const [dx, dy] = [[0, 1, 0, -1], [1, 0, -1, 0]];

const dirNum = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

let [currX, currY] = [0, 0];

moves.forEach((elem) => {
    const [currDir, currDist] = elem.split(' ');

    currX += dx[dirNum[currDir]] * currDist;
    currY += dy[dirNum[currDir]] * currDist;
})

console.log(currX, currY);