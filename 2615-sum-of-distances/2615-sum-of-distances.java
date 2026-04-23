class Solution {
    public long[] distance(int[] nums) {
        int n=nums.length;
        long[] arr=new long[n];
        HashMap<Integer, ArrayList<Integer>> map=new HashMap<>();
        for (int i=0;i<n;i++) {
            if (!map.containsKey(nums[i])) map.put(nums[i], new ArrayList<>());
            map.get(nums[i]).add(i);
        }
        for (int key:map.keySet()) {
            ArrayList<Integer> pos=map.get(key);
            int k = pos.size();
            long[] prefix=new long[k+1];
            for (int i=0;i<k;i++) {
                prefix[i+1]=prefix[i]+pos.get(i);
            }
            for (int i=0;i<k;i++) {
                long left=(long)i*pos.get(i)-prefix[i];
                long right=(prefix[k]-prefix[i+1])-(long)(k-i-1)*pos.get(i);
                arr[pos.get(i)]=left+right;
            }
        }
        return arr;
    }
}