package zxzxvcdd.Dynamic;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q_2294 {
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer input = new StringTokenizer(br.readLine());

        int coins =  Integer.parseInt(input.nextToken());
        int targetCost =  Integer.parseInt(input.nextToken());

        int[] costs = new int[targetCost + 1];
        Arrays.fill(costs,  Integer.MAX_VALUE);

        costs[0] = 0;

        for(int i=0; i<coins; i++){
            
            int cost = Integer.parseInt(br.readLine());

            for(int j=cost; j<targetCost + 1; j++) {
    			if (costs[j-cost] != Integer.MAX_VALUE)
    				costs[j] = Math.min(costs[j], 1 + costs[j-cost]);
				
    		}
            
        }

        int result = 0;
        if(costs[targetCost] == Integer.MAX_VALUE){
            result = -1;
        }else{
            result = costs[targetCost];
        }
 
    	System.out.println(result);
        
    }

}
