// https://www.acmicpc.net/problem/
package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Q1300 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        int start = 0, end = k;
        int ans=-1;
        while (start <= end) {
            int mid = end + (start-end) /2;
            int count = 0;

            for (int i=1; i<=n; i++){
                count += Math.min(mid/i, n);
            }

            if (count>=k){
                ans = mid;
                end = mid -1;
            } else {
                start = mid +1;
            }
        }
        System.out.println(ans);
    }
}
