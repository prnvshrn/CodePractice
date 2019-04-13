const maxCoins = (coins) => {
    var ans = 0;
    var queue = [];
    queue.push([0, 0, 0, 3, []]);
    while(queue.length != 0){
        var[curr, stack, idx, amt, path] = queue.shift();
        //if(stack >= coins.length || idx>=coins[stack].length) continue;
        //console.log(curr, stack, idx, amt);
        if(amt == 0){
            console.log(path);
            ans = Math.max(ans, curr);
            continue;
        }
        if(stack + 1 < coins.length){
            queue.push([curr, stack+1, 0, amt, path]);
            queue.push([curr+coins[stack][idx], stack+1, 0, amt-1, path.concat(coins[stack][idx])]);}
        if(idx<coins[stack].length)
            queue.push([curr+coins[stack][idx], stack, idx+1, amt-1, path.concat(coins[stack][idx])]);
    }
    console.log(ans);
}

var coins = [[1,3,62], [1,25,4], [18,2,13]];
maxCoins(coins);

