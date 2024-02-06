var isAnagram = function(s, t) {
    if(s.length !== t.length){
        return false;
    }
    const counter = new Map();
    
    for(let char of s){
        counter.set(char, (counter.get(char) || 0) +1 );
    };
    for(let char of t){
        if (!counter.has(char) || counter.get(char) == 0){
            return false;
        }
        counter.set(char, counter.get(char) - 1)
    }

    return true;
};


// I tried to find a logic at first of how to do this in JavaScript, but I had to resort to the community tab to understand how HashMaps work, never before used them
// However, CodingNinja's tutorial made perfect sense and his code explanation even more so. 



