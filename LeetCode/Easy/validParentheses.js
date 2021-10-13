// data : 21-10-13
// level : easy
// String, Stack

// LeetCode: 20. Valid Parentheses
// url: https://leetcode.com/problems/valid-parentheses/submissions/
// Problem : Return true if given brackets are in the correct order and closed by the same type of brackets.

// Solution
// 1. Create a stack array
// 2. Add open brackets to the stack
// 3. if there is a close bracket and matches the type of bracket in the stack, then pop the element.
// 4. Repeat 2 and 3 using loop iteration
// 5. if stack length is 0 return true, else false 

/**
 * @param {string} s
 * @return {boolean}
 */
 const isValid = function(s) {
    stack = []
    
    for(let i = 0; i < s.length; i++) {
        if(s[i] == '(' || s[i] == '['  || s[i] == '{') stack.push(s[i])
        else if ( s[i] == ')' && stack[stack.length-1] == '('
          || s[i] == ']' && stack[stack.length-1] == '['
          || s[i] == '}' && stack[stack.length-1] == '{' )  
        {
            stack.pop();    
        } else return false;
    
    }
    
    return true ? stack.length === 0 : false
};