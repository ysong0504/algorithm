// data : 21-10-07
// level : easy

// LeetCode: 350. Intersection of Two Arrays II
// url: https://leetcode.com/problems/intersection-of-two-arrays-ii/
// Problem : Find the intersection of two given arrays

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
 var intersect = function(nums1, nums2) {
    arr = []
    
    // 오름차순 정렬 진행
    nums1.sort((a,b) => a - b)
    nums2.sort((a,b) => a - b)
    
    while (nums2.length!=0) {
        // 마지막 인덱스 값을 기준으로 비교 
        if (nums1[nums1.length-1] == nums2[nums2.length-1]) {
            // 만약 값이 같을 시 arr 배열에 넣어주고 기존 배열에서는 pop()을 이용하여 제거
            arr.push(nums1.pop())
            nums2.pop();
        } else if (nums1[nums1.length-1] > nums2[nums2.length-1]) {
            // 만약 nums1 값이 더 크다면 nums2와 밸런스를 맞추도록 pop() 진행
            nums1.pop();
        } else {
            nums2.pop();
        }
    }
    return arr
};