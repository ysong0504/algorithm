// Selection Sort
// similar to Bubble sort but places small values into sorted position

// how to
// 1. Store an index of the smallest value found by comparing current item to the next one in the array
// 2. Swap the smallest value and the first element that loop has begun with

// time complexity : O(n2)
// bubble : keep swaping
// selection : swap once in each loop

let arr = [4,5,7,0,1]



for(let i=0; i<arr.length; i++) {
    let minIdx = i

    for(let j=i+1; j<arr.length; j++) { // 앞에서부터 범위를 줄이고 싶을 때
        if(arr[j] < arr[minIdx]) {
            minIdx = j
        }
    }

    [arr[minIdx], arr[i]] = [arr[i], arr[minIdx]]
    console.log(arr, minIdx)

}

