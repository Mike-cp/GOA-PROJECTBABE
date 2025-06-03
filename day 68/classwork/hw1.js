function compareNums(num1, num2) {
    if (num1 > num2) {
        console.log(num1);
    } else if (num2 > num1) {
        console.log(num2);
    } else {
        console.log("Numbers are equal");
    }
}

document.body.innerHTML = `
    <input type="number" id="num1" placeholder="Enter first number">
    <input type="number" id="num2" placeholder="Enter second number">
    <button id="compareBtn">Compare</button>
`;

document.getElementById('compareBtn').addEventListener('click', function() {
    const n1 = Number(document.getElementById('num1').value);
    const n2 = Number(document.getElementById('num2').value);
    compareNums(n1, n2);
});