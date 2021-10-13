// data : 21-10-13
// level : easy
// Array, Dynamic Programming

// LeetCode: 118. Pascal's Triangle
// url: https://leetcode.com/problems/pascals-triangle/
// Problem : Given an integer numRows, return the first numRows of Pascal's triangle.

// solution
// 1. create a temp variable where prev index of element is saved
// 1. sort number in order
// 2. Use loop to compare each number.


/**
 * @param {number} numRows
 * @return {number[][]}
 */


// 0. Both ends of each row contains 1
// 1. i represents each row of a pascals'triangle
// 2. j represents an element in the row
// 3. j = [i-1][j] + [i-1][j-1]


const generate = function(numRows) {  
    let triangle = new Array(numRows)    
    for (let i = 0; i < numRows; i++) {
        let row = new Array(i+1); // Create an array with size of each row
        [row[0],row[row.length-1]] = [1,1]  // Both ends of each row contains 1

            for (let j = 0; j < row.length-2; j++) {
                if (i < 2) {
                    break;
                }

                row[j+1] = triangle[i-1][j] + triangle[i-1][j+1];
            } 

        triangle[i] = row;
    }
    
    return triangle
};