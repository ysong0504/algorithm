// data : 21-10-10
// level : easy

// LeetCode: 383. Ransom Note
// url: https://leetcode.com/problems/ransom-note/
// Problem
// 1. Two strings, magazine and ransomNote are given as parameters.
// 2. return true if magazine includes ransomNote.
// 3. Otherwise, return false


/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
 const canConstruct = function(ransomNote, magazine) {
    ransomNote = ransomNote.split('');  // save each character as an array in order to check whether 'magazine' includes each alphabet (not as a word)
    
    for (let i=0; i<ransomNote.length; i++) {
        if (!magazine.includes(ransomNote[i])) {    // if 'magazine' doesn't include any alphabet from ransomNote, return false
            return false;
        }
        magazine = magazine.replace(ransomNote[i],'');  // if magazine includes the alphabet, removes it from magazine to prevent duplicate comparison 
    }
    
    return true;
};