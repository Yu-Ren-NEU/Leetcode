//ry

class Solution {
    public int addDigits(int num) {
        int digit = 0, sum = 0;
        while(num > 0)
        {
            digit = num % 10;
            num = digit + num / 10;
            if(num < 10)
            {
                break;
            }
        }         
        return num;    
    }
}
