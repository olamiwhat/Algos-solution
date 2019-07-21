// Solving the Palindrome challenge in several ways


// Testing a single word and returning a string
function palindrome(string){
	let newString = "";
	for (let i = string.length-1; i >= 0; i--){
		newString += string[i];
	}
	if (string.toLowerCase() == newString.toLowerCase()){
		return `"${string}" reads as "${newString}" backwards, therefore, ${string} is a Palindrome.`
	} else {
		return `"${string}" reads as "${newString}" backwards, therefore, ${string} is NOT a Palindrome.`
	}
}

console.log(palindrome("freakish"));

/*****************************************************************************/

// Testing a single word and returning true or false
function isPalindrome(string){
	let newString = "";
	for (let i = string.length-1; i >= 0; i--){
		newString += string[i];
	} if (string.toLowerCase() == newString.toLowerCase()){
		return true;
	}
	return false;
}

console.log(isPalindrome('freakish'));

/*****************************************************************************/

// Testing phrases that are palindrome  - Phrases with spaces only
function wordIsPalindrome(string){
	let newString = "";
	if (string.search(' ')){
		string = string.split(' ').join('')
	}
	for (let i = string.length-1; i >= 0; i--){
		newString += string[i];
	} if (string.toLowerCase() == newString.toLowerCase()){
		return true;
	}
	return false;
}

console.log(wordIsPalindrome('Goliath run'));



