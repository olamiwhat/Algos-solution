/*
 * Programming Quiz: Laugh (5-4)
 */

var laugh = function(num){
    var text = "";
    for(var i = 1; i <= num; i += 1 ){
    text += "ha";
    }
return text + "!";
};
console.log(laugh(3));
