// function compareNums (num1, num2) {
//     console.log(num1 >= num2)
//     console.log(num1 < num2)
//     console.log(num1 <= num2)
//     console.log(num1 == num2)
//     console.log(num1 === num2)
//     console.log(num1 != num2)
//     console.log(num1 !== num2)
//     console.log(num1 > num2)
// }

// compareNums (12, 17)
// compareNums (12, 19)
// compareNums (12, 7)




document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const inputValue = event.target.elements.userInput.value;
    alert(inputValue);
});