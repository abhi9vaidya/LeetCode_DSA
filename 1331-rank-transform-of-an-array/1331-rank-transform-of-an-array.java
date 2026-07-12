import java.util.Arrays;

class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int[] temp = Arrays.copyOf(arr, arr.length);
        Arrays.sort(temp);
        
        HashMap<Integer,Integer> rank = new HashMap<>();
        int r = 1;

        for(int num : temp){
            if(!rank.containsKey(num)){ // only assigning a rank if havent seen this num
                rank.put(num,r);
                r++;
            }
        }

        int[] result = new int[arr.length];
        for(int i = 0; i < arr.length; i++){
            result[i] = rank.get(arr[i]);
        }
        
        return result;
    }
}