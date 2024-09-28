// https://www.acmicpc.net/problem/
package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Q2110 {

    static boolean check(int[] houses, int c, int n, int distance) {
        int prev = houses[0];
        c--;
        for (int i = 1; i < n; i++) {
            if (houses[i] - prev >= distance) {
                c--;
                prev = houses[i];
                if (c == 0) return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int c = Integer.parseInt(inputs[1]);

        int[] houses = new int[n];
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            houses[i] = Integer.parseInt(input);
        }
        Arrays.sort(houses);

        int left = 1, right = houses[n - 1] - houses[0], ans = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(houses, c, n, mid)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        System.out.println(ans);
    }
}
