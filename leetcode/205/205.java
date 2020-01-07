// ry

class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Integer> map_s = new HashMap<>();
        int len = s.length();
        char[] s_arr = s.toCharArray();
        int[] s_num = new int[len];
        int s_tag = 1;
        for(int i = 0; i < len; i++) {
            if(map_s.get(s_arr[i]) == null) {
                map_s.put(s_arr[i], s_tag);
                s_num[i] = s_tag;
                s_tag++;
            }
            else {
                s_num[i] = map_s.get(s_arr[i]);
            }
        }
        HashMap<Character, Integer> map_t = new HashMap<>();
        char[] t_arr = t.toCharArray();
        // int[] t_num = new int[len];
        int t_tag = 1;
        for(int i = 0; i < len; i++) {
            if(map_t.get(t_arr[i]) == null) {
                map_t.put(t_arr[i], t_tag);
                // t_num[i] = t_tag;
                
                if(t_tag != s_num[i]) return false;
                
                t_tag++;
            }
            else {
                // t_num[i] = map_t.get(t_arr[i]);
                
                if(map_t.get(t_arr[i]) != s_num[i]) return false;
            }
        }
        // for(int i = 0; i < len; i++) {
        //     if(s_num[i] != t_num[i]) return false;
        // }
        return true;
    }
}
