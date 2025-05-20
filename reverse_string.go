func reverseString(s []byte)  {
    left := 0
    right := len(s) - 1
    for right > left {
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    }
}
