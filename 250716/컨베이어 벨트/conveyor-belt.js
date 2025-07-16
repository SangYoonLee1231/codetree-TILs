const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const [n, t] = input[0].split(' ').map(Number);
const u = input[1].split(' ').map(Number);
const d = input[2].split(' ').map(Number);

// Please write your code here.
function solution() {
    const array = [...u, ...d];

    function moveElems(array) {
        let temp = array[2*n - 1];

        for (let i = 2*n - 1; i >= 1; i--) {
            array[i] = array[i - 1];
        }
        array[0] = temp;
    }

    function printArray(array) {
        for (let i = 0; i < t; i++) {
            moveElems(array);
        }

        for (let i = 0; i < 2; i++) {
            for (let j = 0; j < n; j++) {
                process.stdout.write(`${array[n*i + j]} `);
            }
            console.log();
        }
    }

    printArray(array);
}

solution();