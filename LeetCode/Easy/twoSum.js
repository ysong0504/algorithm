// data : 21-10-05
// level : easy

// LeetCode: 1. Two Sum
// url: https://leetcode.com/problems/two-sum/submissions/
// Problem : Return the index of elements where sum of which equals to a given target number
// Things to consider
// 1. Try to solve the problem with O(n) time complexity 


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const twoSum = function(nums, target) {

    // first Attempt: Brute Force - O(n2)
    //     result = []
        
    //     for(let i=0; i<nums.length; i++) {
    //        for (let j=i+1; j<nums.length; j++) {
    //            if(target === nums[i] + nums[j]) {
    //                result.push(i,j)
    //                return result
                
    //            }
    //        }
    //     }
        
    // Second Attempt: Hash Table - O(n)
        
    const table = new Map();
        
    
    for(let i=0; i<nums.length; i++) {
        let curNum = target - nums[i]   // 현재 값에서 타겟 값을 충족시키기 위한 숫자를 구한다.
        // console.log(curNum, nums[i], i, nums.indexOf(curNum))

        if(table.has(nums.indexOf(curNum))) {    // 만약 table에 충족시켜주는 값이 있다면 현재 인덱스와 해당 값의 인덱스를 반환한다.
            return [i, nums.indexOf(curNum)]
        }
                
        table.set(i, nums[i])
        

    }
             
          
}