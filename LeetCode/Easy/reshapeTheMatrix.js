// data : 21-10-08
// level : easy

// LeetCode: 566. Reshape the Matrix
// url: https://leetcode.com/problems/reshape-the-matrix/submissions/
// Problem
// 1. multiple dimensional array and to-be numbers of row and column are given.
// 2. Reshape the matrix following the to-be numbers.
// 3. If reshping matrix is not possible, return the original matrix.

/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
 var matrixReshape = function(mat, r, c) {
    let arr = []
    let m = [].concat(...mat)   // Turn into 1D Array

    let arrLength = m.length / r    // length of elements for each array
    
    if(!Number.isInteger(arrLength)) {  // if the division number is not integer, then return the original shape of matrix
        return mat
    }
 
    for(let i=0; i < r; i++) {
        let temp = []
        
        for(let j=0; j < arrLength; j++) {
            temp.push(m.shift());        
        }
              
        arr.push(temp)
    }
    
    return arr
    
};