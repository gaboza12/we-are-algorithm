package zxzxvcdd.math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Q_3343 {

    static class RoseInfo{

        long size;
        long cost;
    
        public RoseInfo(StringTokenizer inputToken) {
            this.size = Long.parseLong(inputToken.nextToken());
            this.cost = Long.parseLong(inputToken.nextToken());
        }
    
        boolean isMoreExpensive(RoseInfo storeB){
            return ((double)this.cost / this.size > (double)storeB.cost / storeB.size);
        }
        
        long getCostBySize(long target){
            long totalcost = (target/this.size) * this.cost;
            return totalcost;
        }
    
        long getUnitCost(){
            return this.size/this.cost;
        }
    
    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer inputToken = new StringTokenizer(br.readLine());

        long target = Long.parseLong(inputToken.nextToken());
        RoseInfo storeA = new RoseInfo(inputToken);
        RoseInfo storeB = new RoseInfo(inputToken);
        
        long totalCost = 0;
        if(storeA.isMoreExpensive(storeB)){
            totalCost = getRsult(storeB, storeA, target);
        }else{
            totalCost = getRsult(storeA, storeB, target);
        }

        System.out.println(totalCost);

    }

    static long getRsult(RoseInfo storeA, RoseInfo storeB, long target){

        long result= Long.MAX_VALUE;
        for(int i=0; i <= storeA.size; i++) {
			long sizeA = (long) Math.ceil((double)(target - i*storeB.size)/storeA.size) ;
            if(sizeA < 0){
                sizeA=0;
            }
            long costB = i * storeB.cost;
			result = Math.min(result, sizeA * storeA.cost + costB);
            if(sizeA==0) break;
		}
        return result;
    }
}
