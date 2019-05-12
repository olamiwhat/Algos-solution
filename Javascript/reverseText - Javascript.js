
# Write a method that will take a string as input, and return a new
# string with the same letters in reverse order.
#
# Don't use String's reverse method; that would be too simple.


function reverseText(text){
    var newText = ""; //*creates a new string to hold the new text//
    for(i = text.length - 1; i >= 0; i--){
      newText += text[i]; //*"newText" becomes an addition of the "elements" in "text" as the code iterates thru each element in "text"//
    };
    return newText;
};

//""*text.length - 1"  counts the element in "text" starting from the last element.//
