func isRuneIn(s []rune, r rune) bool {
	for _, j := range s {
		if j == r {
			return true
		}
	}
	return false
}

func reverseVowels(s string) string {
	new_s := []rune(s)
	vowels := []rune{'a','i', 'u', 'e', 'o','A','I', 'U', 'E', 'O'}
	left := 0
	right := len(s) - 1
	for left < right {
		for left < right && !isRuneIn(vowels, new_s[left]){
            left += 1
        }
        for left < right && !isRuneIn(vowels, new_s[right]){
            right -= 1
        }
        if left < right{
            new_s[left], new_s[right] = new_s[right], new_s[left]
            left += 1
            right -= 1
        }
	}
	return string(new_s)
}
