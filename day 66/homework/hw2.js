const ask = confirm("გსურთ რომ გაგრძელოთ?");
console.log(ask)

function askr() {
    const asker = confirm("Do you want to continue?");
    console.log("User confirmed:", asker); 
  }


alert(confirm('Do u wana continue?'))


function logclear(){
    e.preventDefault();
    const usernams = document.querySelector('input[name="username"]');
    console.log("usernames", usernams);
}

function clear(){
    e.preventDefault();
    const phone = document.querySelector('input[name="phone"]');
    alert("phone", phone)
}

function email(){
    e.preventDefault();
    const email = document.querySelector('input[name="email"]').value = ''
}