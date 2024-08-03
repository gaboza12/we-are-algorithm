package zxzxvcdd.dp2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_2758 {
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testcase = Integer.parseInt(br.readLine());
 
        int n, m;
        long result=0;
        long [][] dp = new long [11][4001];
 
        for(int i=1; i<=4000; i++){
            dp[1][i] = 1;
        }
 
        for(int i=2; i<=10; i++){
            for(int j=1; j<=4000;j++){
                if(dp[i-1][j]!=0){
                    for(int k =j*2; k<=4000; k++){
                        dp[i][k] += dp[i-1][j];
                    }
                }
            }
        }
        for(int i=0; i<testcase; i++){
            StringTokenizer input = new StringTokenizer(br.readLine());
            n = Integer.parseInt(input.nextToken());
            m = Integer.parseInt(input.nextToken());
            result=0;
            for(int j=1; j<=m; j++){
                result+=dp[n][j];
            }
            System.out.println(result);
        }


    }
}
