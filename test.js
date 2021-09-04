// //helperMethodRecursion
// function outerFunction (input) {
//     var outerScopeVariable = []

//     // recursive function
//     function helper(helperInput) {
//         helper(helperInput--)
//     }
//     helper(input)

//     return outerScopeVariable;
// }

// //for pure recursion tip
// // for arrays, use slice, the spread operator, concat that make copies of arrays instead of mutating them


// // recursion Example/
// // power
// // power(2,0) // 1
// // power(2,2) // 4
// // power(2,4) // 16

// function power(n1, n2){
//     if (n2 === 0) return 1
//     return n1 * power(n1, n2-1) 
// }

// // facotorail
// function factorial(n){
//     if (n === 0) return 1;
//     return n * factorial(n-1);
   
// }

// // productOfArray([1,2,3]) // 6
// // productOfArray([1,2,3,10]) // 60

// var sum = 1
// function productOfArray(arr) {
//     if (arr.length === 0) {
//         let result = sum
//         sum = 1
//         return result;
//     }
//     sum *= arr.pop();
//     return productOfArray(arr);
    
// }

// function productOfArray(arr) {
//     if (arr.length === 0) return 1;
//     return arr[0] * productOfArray[arr.slice(1)]
// }

function solution(price, money, count) {
    let totalSum = 0
    for (let i = 1; i <= count; i++) {
        totalSum += price * i
    }

    return money >= totalSum ? 0 : totalSum - money
    
    if (money >= totalSum) {
        return 0
    }
    return Math.abs(totalSum - money)
}

function solution(price, money, count) {
    let totalSum = 0
    for (let i = count; i != 0; i--) {
        totalSum = totalSum + (price * i)
        console.log(totalSum, price, i)
        if (totalSum > money) {
            return Math.abs(totalSum - money)
        }
    }
        return 0
}

console.log(solution(3,20,4))

function solution(price, money, count) {
    let totalSum = 0
    for (let i = 1; i <= count; i++) {
        totalSum += price * i
    }
    return money >= totalSum ? 0 : totalSum - money
}