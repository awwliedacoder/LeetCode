var maxOperations = function(nums, k) {
    nums.sort(function(a, b){return a-b});    
    let ops = 0
    let i = 0 
    let j = nums.length-1

    while(i <j ){
        let sum = nums[i] + nums[j]
        if(sum == k){
            ops++
            j--;
            i++;
        } 
        else if (sum > k) j--
        else i++;
    }
    return ops    
};

/*
Don't know if I should be proud or not, but this is a community answer, I couldn't wrap my head around the first consept of pointers, due to never having even used them- This coding really hard... and headaches.. are real..
*/
// Own Solution 14 / 51 testcases passed

var maxOperations = function(nums, k) {
    let counter = 0
    let i = 0
    while(i < nums.length){
        for(let j = i + 1 ; j < nums.length; j++){
            if(nums[i] + nums[j] == k){
                nums.splice(nums[i], nums[j])
                counter++
            }
    }   i++
    }   
    return counter
};
