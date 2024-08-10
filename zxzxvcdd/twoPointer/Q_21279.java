package zxzxvcdd.twoPointer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Q_21279 {

    static class Mineral{

        int x;
        int y;
        long v;

        public Mineral(int x, int y, long v) {
            this.x = x;
            this.y = y;
            this.v = v;
        }

    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer input = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(input.nextToken());
        int c = Integer.parseInt(input.nextToken());

        List<Mineral> minerals = new ArrayList<>();

        for(int i = 0; i < n; i++){
            input = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(input.nextToken());
            int y = Integer.parseInt(input.nextToken());
            long v = Long.parseLong(input.nextToken());
            minerals.add(new Mineral(x, y, v));
            
        }

        long result = getMaxBeauty(minerals, c);
        System.out.println(result);

    }
    static long getMaxBeauty(List<Mineral> minerals, int c) {

        minerals.sort(Comparator.comparingInt(g -> g.x));

        long maxBeauty = 0;
        int start = 0;
        long currentBeauty = 0;
        PriorityQueue<Integer> yValues = new PriorityQueue<>();

        for (int end = 0; end < minerals.size(); end++) {

            Mineral mineral = minerals.get(end);
            yValues.add(mineral.y);
            currentBeauty += mineral.v;

            int cnt = yValues.size();

            
            int i = end + 1;
            while(i <= minerals.size() - 1 && minerals.get(i).x == mineral.x){
                cnt++;
                i++;
            }

            while (cnt > c) {
                currentBeauty -= minerals.get(start).v;
                yValues.remove(minerals.get(start).y);
                start++;
            }

            maxBeauty = Math.max(maxBeauty, currentBeauty);
        }

        return maxBeauty;
    }
}
