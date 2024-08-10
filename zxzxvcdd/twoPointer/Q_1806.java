package zxzxvcdd.twoPointer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_1806 {
     public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer input = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(input.nextToken());
        int target = Integer.parseInt(input.nextToken());

        input = new StringTokenizer(br.readLine());
        
        int[] nums = new int[n + 1];
        for(int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(input.nextToken());
        }
        
        int min = Integer.MAX_VALUE;
        int start = 0;
        int end = 0;
        int total = 0;
        while(start <= n && end <= n) {
            if(total >= target && min > end - start) {
                min = end - start;
            }
            
            if(total < target){
                total += nums[end++];
            }else{
                total -= nums[start++];
            } 
        }
        
        if(min == Integer.MAX_VALUE) {
            System.out.println("0");
        }else{
            System.out.println(min);
        }
    }
}
