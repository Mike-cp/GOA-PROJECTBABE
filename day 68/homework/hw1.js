const userInput = prompt("Enter a number:");
const number = Number(userInput);

if (number > 0) {
  alert("The number is positive.");
} else if (number < 0) {
  alert("The number is negative.");
} else if (number === 0) {
  alert("The number is zero.");
} else {
  alert("That's not a valid number!");
}


const ageInput = prompt("Enter your age:");
const age = Number(ageInput);

if (age >= 18) {
  alert("You can vote!");
} else if (age >= 0) {
  alert("You are not eligible to vote.");
} else {
  alert("Please enter a valid age.");
}


const num1 = Number(prompt("Enter the first number:"));
const num2 = Number(prompt("Enter the second number:"));

if (num1 > num2) {
  alert(`${num1} is larger than ${num2}.`);
} else if (num2 > num1) {
  alert(`${num2} is larger than ${num1}.`);
} else if (num1 === num2) {
  alert("Both numbers are equal.");
} else {
  alert("Invalid input.");
}

function booleanToString(b) {
  return b.toString();
}
function countSheeps(arrayOfSheep) {
  return arrayOfSheep.filter(Boolean).length;
}
function disemvowel(str) {
  return str.replace(/[aeiouAEIOU]/g, '');
}
class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min(...args);
  }
}
function positiveSum(arr) {
  return arr.filter(n => n > 0).reduce((a, b) => a + b, 0);
}
function numberOfDivisors(n) {
  let count = 0;
  for(let i = 1; i <= n; i++) {
    if(n % i === 0) count++;
  }
  return count;
}
class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min(...args);
  }
}
function isPalindrome(x) {
  const str = x.toLowerCase().replace(/[^a-z0-9]/g, '');
  return str === str.split('').reverse().join('');
}
function boolToWord(bool) {
  return bool ? "Yes" : "No";
}

function sumTwoSmallestNumbers(numbers) {
  const sorted = numbers.filter(n => n > 0).sort((a,b) => a-b);
  return sorted[0] + sorted[1];
}
