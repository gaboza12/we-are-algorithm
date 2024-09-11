// https://www.acmicpc.net/problem/
package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Q2470 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String[] inputs = br.readLine().split(" ");
        long[] nums = new long[n];
        for (int i=0; i<n; i++){
            nums[i] = Integer.parseInt(inputs[i]);
        }
        Arrays.sort(nums);
        int left = 0, right = n-1;
        long cmin = Long.MAX_VALUE;
        long[] ans = new long[2];

        while (left < right) {
            long lnum = nums[left], rnum = nums[right];
            long total = lnum + rnum;

            if (Math.abs(total) < Math.abs(cmin)) {
                cmin = total;
                ans[0] = lnum;
                ans[1] = rnum;
            }
            if (total == 0) {
                System.out.println(ans[0] + " " + ans[1]);
                return;
            } else if (total > 0) {
                right--;
            } else {
                left ++;
            }
        }
        System.out.println(ans[0] + " " + ans[1]);
    }
}
