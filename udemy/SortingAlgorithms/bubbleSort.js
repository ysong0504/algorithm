// Bubble sort
// - ascending numeric order
// - compare and swap and so on..

const swap = (arr, idx1, idx2) => {
    [arr[idx1], arr[idx2]] = [arr[idx1], arr[idx2]]
}

// my first attempt
// problem of this solution is that, it still goes up the last index where already sorted

// let arr = [4,7,5,0,1]

// for (let i=0; i<arr.length; i++) {
//     for(let j=0; j<arr.length; j++) {
//         if (arr[j] > arr[j+1]) {
//             [arr[j],arr[j+1]] = [arr[j+1],arr[j]]
//             console.log(arr)
//         }
//     }
// }

// better way1
let arr = [4,5,7,0,1]
let isSwapped;  // this variable makes the time complexity O(n)
                // without this, the time complexity would have been O(n2) as both loop have to go through all the way

for (let i = arr.length; i > 0; i--) {  // 끝에서부터 점점 범위를 줄이고 싶을 때
    isSwapped = false;
    for(let j=0; j < i-1; j++) {    // in that way, this loop doesn't repeat comparing the index that is already sorted 
        if (arr[j] > arr[j+1]) {
            [arr[j],arr[j+1]] = [arr[j+1],arr[j]]
            isSwapped = true
            console.log(arr)
        }
    }
    if(!isSwapped) break;
}






