class Solution {
    
    int reverse(int num) {
        int current = 0;
        
        while (num > 0) {
            current = current * 10 + (num % 10);
            num = num / 10;
        }
        
        return current;
    }
    
    public boolean sumOfNumberAndReverse(int num) {
        
        for (int i = 0; i <= num; i++) {
            if (i + reverse(i) == num) {
                return true;
            }
        }
        return false;
    }
}