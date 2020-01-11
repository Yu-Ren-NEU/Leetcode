//ry

class Solution {
    public String getHint(String secret, String guess) {
        int A = 0;
        int B = 0;
        int[] num = new int[10];
        char[] arr_secret = secret.toCharArray();
        char[] arr_guess = guess.toCharArray();
        for(int i = 0; i < arr_secret.length; i++) {
            if(arr_secret[i] == arr_guess[i]) {
                A++;
                arr_secret[i] = '-';
            }
            else {
                num[arr_guess[i] - '0'] ++;
            }
        }
        for(int i = 0; i < arr_secret.length; i++) {
            if(arr_secret[i] != '-' && num[arr_secret[i] - '0'] != 0) {
                B++;
                num[arr_secret[i] - '0'] --;;
            }
        }
        return A + "A" + B + "B";
    }
}
