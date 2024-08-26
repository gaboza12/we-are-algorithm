package zxzxvcdd.greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Q_8980 {

    static class Delivery implements Comparable<Delivery> {
        int from, to, box;
        public Delivery(int from, int to, int box) {
            this.from = from;
            this.to = to;
            this.box = box;
        }
        @Override
        public int compareTo(Delivery o) {
            if (this.to == o.to) return this.from-o.from;
            else return this.to-o.to;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer inputToken = new StringTokenizer(br.readLine());
        
        int town = Integer.parseInt(inputToken.nextToken());
        int maxBoxCount = Integer.parseInt(inputToken.nextToken());
        int deliveryCount = Integer.parseInt(br.readLine());
       
        Delivery info[] = new Delivery[deliveryCount];
        for (int i = 0; i < deliveryCount; i++) {
            inputToken = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(inputToken.nextToken());
            int to = Integer.parseInt(inputToken.nextToken());
            int cnt = Integer.parseInt(inputToken.nextToken());
            info[i] = new Delivery(from, to, cnt);
        }
        Arrays.sort(info);

        int[] truck = new int[town+1];
        int max, possible, total = 0;

        for(int i = 0; i < town; i++){

            int from = info[i].from;
            int to = info[i].to;
            int box = info[i].box;

            max =0;
       
            for (int j = from; j < to; j++) {
                max = Math.max(max, truck[j]);
            }

            possible  = Math.min(maxBoxCount-max, box);
            total  += possible;
            for (int j = from; j < to; j++) {
                truck[j] += possible;
            }

        }
        System.out.println(total +truck[town]);

    }
    
}
