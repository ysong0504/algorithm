// data : 21-09-27
// level : easy

// LeetCode: 7. Reverse Integer
// url: https://leetcode.com/problems/reverse-integer/
// Problem : Return the reversed number of given number, 'x'
// Things to consider
// 1. if the reversed number is outside of range of 32-bit integer (-2^31, 2^31 - 1), return 0


/**
 * @param {number} x
 * @return {number}
 */

 var reverse = function(x) {
    
    Min = -Math.pow(2,31)
    Max = Math.pow(2,31)-1

    let a = Math.abs(x);
    a = String(a).split('').reverse().join(''); // convert into string in order to sort numbers as an array and get them reversed.
    
    if (a <= Min || a >= Max) {   // if the number is bigger than 32 bit integer, return 0
        return 0
    }
 
    return x < 0 ? -a : a   // if the given number was negative, then add '-' in front.

};