package zxzxvcdd.Dynamic;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_15486 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int dDay = Integer.parseInt(br.readLine());
        

        int[] time = new int[dDay + 2];
        int[] pay = new int[dDay + 2];
        for (int i = 1; i <= dDay; i++) {

            StringTokenizer input = new StringTokenizer(br.readLine());

            time[i] = Integer.parseInt(input.nextToken());
            pay[i] = Integer.parseInt(input.nextToken());
        }

        int[] costs = new int[dDay + 2];
        int max = 0; 
        for (int i = 1; i <= dDay + 1; i++) {

            if (max < costs[i]) {
                max = costs[i];
            }

            int day = i + time[i];

            if (day <= dDay + 1) {
                costs[day] = Math.max(costs[day], max + pay[i]);
            }
        }

        System.out.println(max);
    }

    
}
