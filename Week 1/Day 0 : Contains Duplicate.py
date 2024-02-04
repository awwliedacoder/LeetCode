        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


// Own JavaScript Solution

var containsDuplicate = function(nums) {

    for(let i=0; i < nums.length; i++){
        if(nums[0] != nums[i]){
