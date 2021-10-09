// data : 21-10-04
// level : easy
// Array, Hash Table, String, Queue

// LeetCode: 387. First Unique Character in a String
// url: https://leetcode.com/problems/first-unique-character-in-a-string/
// Problem : Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

// solution
// 1. create a table to save alphabets as a key and each 횟수 as a value.
// 2. value 가 1인 (즉, 한번만 사용된) key를 찾은 후
// 3. key에 해당하는 인덱스 값을 찾아 반환한다.

/**
 * @param {string} s
 * @return {number}
 */
 var firstUniqChar = function(s) {
    let m = {};  // 각 알파벳의 횟수를 저장할 테이블 생성
    let ans;
    
    for(let i=0; i<s.length; i++) {
        if(m[s[i]]) {      // 만약 테이블에 해당 알파벳이 존재 시 개수만 올려준다.
            m[s[i]] += 1
            continue
        }
        
        m[s[i]] = 1 // 첫 알파벳이라면 1과 함께 map에 저장
    }
    
    if(!Object.values(m).includes(1)) {
        return -1
    }
    

    for (const[k,v] of Object.entries(m)) {      
        if (v == 1) {
            ans = k
            break
        }
    }

    return s.indexOf(ans)


};