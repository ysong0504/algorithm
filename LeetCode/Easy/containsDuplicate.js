// data : 21-10-04
// level : easy
// Array, Hash Table, Sorting

// LeetCode: 217. Contains Duplicate
// url: https://leetcode.com/problems/contains-duplicate/
// Problem : Return true if elements in a given array appears at least twice.

// solution
// 1. create a temp variable where prev index of element is saved
// 1. sort number in order
// 2. Use loop to compare each number.

/**
 * @param {number[]} nums
 * @return {boolean}
 */
 const containsDuplicate = function(nums) {
    let temp;
    nums.sort() // sort numbers in order
    for(let i=0; i<nums.length; i++) {
        if (temp == nums[i]) {
            return true
        }
        temp = nums[i]
    }
    return false
};