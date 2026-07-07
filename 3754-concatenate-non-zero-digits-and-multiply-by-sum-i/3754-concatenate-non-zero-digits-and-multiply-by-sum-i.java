class Solution {
    public long sumAndMultiply(int n) {
        StringBuilder xb = new StringBuilder();
        long sum = 0;
        while(n>0){
            long d;
            d = n%10;
            if(d!=0){
                xb.append(d);
                sum+=d;
            }
            n/=10;
        }
        xb.reverse();
        if(xb.length()==0) return 0;
        long x = Long.parseLong(xb.toString());
        return x*sum;
    }
}