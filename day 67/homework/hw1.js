const object = {}

const info = {
    name: 'mika',
    age: 15,
    city: 'tbilisi'
}
console.log(info.name)
console.log(info.age)
console.log(info.city)
info.job='developer'


const infos ={
    name: 'mika',
    age: 15,
    ads: {
        city: 'tbilisi',
        portal: 12.56,

    }

}

infos.age = 16


const a = 11
const b = 12
const full = (a>10) && (b>10)
console.log(full)

const any = (a>10) || (b<10)
console.log(any)


const age = 25;
const hasID = true;
const canEnter = (age >= 18) && hasID || !hasID;
console.log(canEnter); 


const ages = 15
const agers = string(ages)
console.log(agers)
console.log(typeof(agers))

const bool = true
const strbool = string(bool)
console.log(bool)
console.log(typeof(strbool))


const number = "546"
const intnumber = Number(number);
console.log(intnumber);
console.log(typeof (intnumber));

console.log(Number(true))
console.log(Number(false))


const non = "string"
const test = Number(non)
console.log(test)
console.log(typeof(test))