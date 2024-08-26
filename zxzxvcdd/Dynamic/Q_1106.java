package zxzxvcdd.Dynamic;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q_1106 {


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer input = new StringTokenizer(br.readLine());

        int customers  = Integer.parseInt(input.nextToken());
        int cityCnt = Integer.parseInt(input.nextToken());
        
  	    int[] costs = new int[customers+100]; 
    	Arrays.fill(costs,  Integer.MAX_VALUE);
    	costs[0] = 0;

        for(int i=0; i<cityCnt; i++){
            
            input = new StringTokenizer(br.readLine());

            int cost = Integer.parseInt(input.nextToken());
            int effect = Integer.parseInt(input.nextToken());
            for(int j=effect; j<customers + 100; j++) {
    			if (costs[j-effect] != Integer.MAX_VALUE)
    				costs[j] = Math.min(costs[j], cost + costs[j-effect]);
				
    		}
            
        }

        int result = Integer.MAX_VALUE;
        for(int i=customers;i<customers+100;i++) {
    		result = Math.min(result, costs[i]);
    	}
 
    	System.out.println(result);
        

    }
}
