const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const personLines = input.slice(1, n + 1);

const peoples = [];

// Please Write your code here.
class Person {
    constructor(name, addr, city) {
        this.name = name;
        this.addr = addr;
        this.city = city;
    }
}

personLines.forEach((elem) => {
    const [name, addr, city] = elem.split(" ");;
    peoples.push(new Person(name, addr, city));
})

const sortedPeoples = peoples.sort((a, b) => b.name.localeCompare(a.name));

console.log(`name ${sortedPeoples[0].name}`);
console.log(`addr ${sortedPeoples[0].addr}`);
console.log(`city ${sortedPeoples[0].city}`);
