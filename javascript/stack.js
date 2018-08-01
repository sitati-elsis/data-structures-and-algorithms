var Stack = function(){
    this.storage = "";
}

Stack.prototype.push = function(val){
    this.storage = this.storage + "-" + val;
};

Stack.prototype.pop = function(){
    var substring = this.storage.slice(this.storage.lastIndexOf("-")+1);
    // updating new stack without the last item
    this.storage = this.storage.substring(0, this.storage.lastIndexOf("-"))
    return substring;
}

Stack.prototype.size = function(){
    return this.storage.length;
}

var food = new Stack();
food.push("Skuma");
food.push("Meat");
food.push("Rice");
var last = food.pop()
console.log(food.storage)
console.log(food.size())
console.log(last)