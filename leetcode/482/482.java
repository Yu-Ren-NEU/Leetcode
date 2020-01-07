class Solution {
    public String licenseKeyFormatting(String S, int K) {
        if(S.length() == 0) return S;
        char[] s_arr = S.replaceAll("-", "").toCharArray();
        int rem = s_arr.length % K;
        StringBuilder sb = new StringBuilder();
        if(rem != 0) {
            for(int i = 0; i < rem; i++) {
                sb.append(s_arr[i]);
            }
            if(rem < s_arr.length) sb.append("-");
        } 
        int num = 0;
        for(int i = rem; i < s_arr.length; i++) {
            if(num == K) {
                sb.append("-");
                num = 0;
            }
            sb.append(s_arr[i]);
            num++;
        }
        return sb.toString().toUpperCase();
    }
}
