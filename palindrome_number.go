func isPalindrome(x int) bool {
    if x < 0 || (x % 10 == 0 && x != 0){
        return false
    }
    revert_num := 0
    temp_x := x
    for x != 0{
        revert_num =  revert_num * 10 + (x%10)
        x = x / 10
    }
    return revert_num == temp_x
}
