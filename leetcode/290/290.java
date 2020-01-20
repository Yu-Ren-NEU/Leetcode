//ry

class Solution {
    public boolean wordPattern(String pattern, String str) {
        char[] pattern_arr = pattern.toCharArray();
        String[] str_arr = str.split(" ");
        if(pattern_arr.length != str_arr.length) return false;
        HashMap<Character, String> map1 = new HashMap<>();
        HashMap<String, Character> map2 = new HashMap<>();
        for(int i = 0; i < pattern_arr.length; i ++) {
            if(map2.get(str_arr[i]) == null) map2.put(str_arr[i], pattern_arr[i]);
            else {
                if(map2.get(str_arr[i]) != pattern_arr[i]) return false;
            }
            String tmp = map1.get(pattern_arr[i]);
            if(tmp == null) map1.put(pattern_arr[i], str_arr[i]);
            else {
                if(tmp.compareTo(str_arr[i]) != 0) return false;
            }
        }
        return true;
    }
}
