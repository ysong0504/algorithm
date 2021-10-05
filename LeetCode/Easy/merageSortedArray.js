// data : 21-10-05
// level : easy

// LeetCode: 88. Merge Sorted Array
// url: https://leetcode.com/problems/merge-sorted-array/submissions/
// Problem : Merge two given arrays into the first array in an ascending order.

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

 const merge = function(nums1, m, nums2, n) {
    
    nums1.splice(m, nums1.length)
    nums2.splice(n, nums2.length)
    
    nums1.push(...nums2)
    
    nums1.sort((a,b) => a - b)  // for numerical sorting
    // nums1.sort() // for alphabetical sorting
};