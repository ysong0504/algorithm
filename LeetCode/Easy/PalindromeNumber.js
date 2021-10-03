// data : 21-10-03
// level : easy

// LeetCode: 9. Palindrome Number
// url: https://leetcode.com/problems/palindrome-number/
// Problem : Return true if the sequence of number is palindrome.
// Things to consider
// 1. Try to solve the problem without converting integer to string!

// solution
// 1. Add each digit number to an array using while loop.
// 2. compare the numbers from each side using for loop.


/**
 * @param {number} x
 * @return {boolean}
 */

 const isPalindrome = function(x) {
    let arr = []

   
    if (x < 0) {     // 음수일 시 false 반환
        return false;
    } else if (x < 10) {    // 한자릿수일 시 true 반환
        return true;
    }
    
    while (x > 0) {
        arr.push(x % 10)
        x = parseInt(x / 10)
    }

    for (let i = 0; i < arr.length; i++) {
        if(arr[i] !== arr[arr.length-1-i]) {
           return false
       }
    }
    
    return true;
    
};