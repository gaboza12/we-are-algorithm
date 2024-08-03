package zxzxvcdd.dp2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q_3687 {
    static long [] dp;
    static int [] min= {1,7,4,2,0,8};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
 
        dp = new long[101];
 
        Arrays.fill(dp,Long.MAX_VALUE);
 
        dp[2]=1;
        dp[3]=7;
        dp[4]=4;
        dp[5]=2;
        dp[6]=6;
        dp[7]=8;
        dp[8]=10;
 
        StringBuilder result;
 
        for(int i=9; i<=100; i++){
            for(int j=2; j<=7; j++){
                String temp = String.valueOf(dp[i-j])+String.valueOf(min[j-2]);
                dp[i] = Math.min(Long.parseLong(temp),dp[i]);
            }
        }
 
        for(int i=0; i<testCase; i++){
            int n = Integer.parseInt(br.readLine());
            result = new StringBuilder();
 
            result.append(dp[n]).append(" ");
            if(n%2==0){
                result.append(convertMax(n/2));
            }
            else{
                result.append("7").append(convertMax((n-3)/2));
            }
 
            System.out.println(result.toString());
        }
    }
 
    private static String convertMax(int n){
        StringBuilder result = new StringBuilder();
        for(int i=0; i<n; i++){
            result.append("1");
        }
        return result.toString();
    }
}
