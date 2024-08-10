package zxzxvcdd.twoPointer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_15961 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer input = new StringTokenizer(br.readLine());

        int n=Integer.parseInt(input.nextToken());
        int d=Integer.parseInt(input.nextToken());
        int k=Integer.parseInt(input.nextToken());
        int c=Integer.parseInt(input.nextToken());

        int[] sushi = new int[n];
        int[] visit = new int[d+1];

        for(int i=0;i<n;i++) {
            sushi[i]=Integer.parseInt(br.readLine());
        }

        int result=1;
        visit[c]++;
        
        for(int i=0;i<k;i++) {
            if(visit[sushi[i]]==0) result++;
            visit[sushi[i]]++;
        }

        int cnt=result;
        for(int i=1;i<n;i++) {
            int pop = sushi[i-1];
            visit[pop]--;
            if(visit[pop]==0) cnt--;

            int add = sushi[(i+k-1)%n];
            if(visit[add]==0) cnt++;
            visit[add]++;

            result = Math.max(result,cnt);
        }

        System.out.println(result);
    }
}
