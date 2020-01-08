//ry

class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<Integer> list = new ArrayList<>();
        for(int i : arr1) map.put(i, map.getOrDefault(i, 0) + 1);
        int j = 0;
        for(int i = 0; i < arr2.length; i++) {
            int len = map.get(arr2[i]);
            map.put(arr2[i], 0);
            for(int x = 0; x < len; x++) arr1[j++] = arr2[i];
        }
        for(int i : map.keySet()) {
            if(map.get(i) != 0) list.add(i);
        }
        Collections.sort(list);
        for(int i : list) {
            int len = map.get(i);
            for(int x = 0; x < len; x++) arr1[j++] = i;
        }
        return arr1;
    }
}
