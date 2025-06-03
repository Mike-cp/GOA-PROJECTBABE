// const person = {
//     name: "mika",
//     surname: "Giorgadze",
//     academy: "GOA",
//     city: "Tbilisi",
//     role: "student",
//     favColor: "blue",
//     printFullName: function() {
//         console.log(this.name + " " + this.surname);
//     },
//     printFavColor: function() {
//         console.log(this.favColor);
//     }
// };

// console.log(person);

// console.log(person.city);

// person.printFullName();
// person.printFavColor();

// person.favColor = "green";
// console.log(person.favColor);

function userOperations() {
    const result1 = confirm("true or false");
    const result2 = confirm("true or false");
    console.log("AND operation:", result1 && result2);
    console.log("OR operation:", result1 || result2);
}

document.addEventListener("DOMContentLoaded", userOperations);