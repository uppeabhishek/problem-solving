class Solution {
   public void helper(char[] s, int front, int last) {
        if (front >= last) {
            return;
        }

        helper(s, front + 1, last - 1);
        
        char temp = s[front];
        s[front] = s[last];
        s[last] = temp;
    }
    
    public void reverseString(char[] s) {
        helper(s, 0, s.length - 1);
    }
}