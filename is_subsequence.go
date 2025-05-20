func isSubsequence(s string, t string) bool {
    s_pointer := 0
    for i:=0; i < len(t); i++ {
        if len(s) == s_pointer{
            return true
        }
        if s[s_pointer] == t[i]{
            s_pointer +=1
        }
    }
    return s_pointer == len(s)
}
