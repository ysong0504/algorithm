// data : 21-10-10
// level : easy

// LeetCode: 242. Valid Anagram
// url: https://leetcode.com/problems/valid-anagram/
// Problem
// 1. Strings, s and t are given.
// 2. Return true if t is an anagram of s
// * anagram is a different form of a word using the same letters.

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */



const isAnagram = function(s, t) {
    t = t.split('')
    for(let i=0; i<t.length; i++) {
        if(!s.includes(t[i])) {
            return false;
        }
        
        s = s.replace(t[i],'')
    }
    
    if(s) {
        return false;
    }
    
    return true;
};