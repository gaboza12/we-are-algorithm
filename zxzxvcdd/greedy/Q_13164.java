package zxzxvcdd.greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q_13164 {

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer inputToken = new StringTokenizer(br.readLine());
        int childCount = Integer.parseInt(inputToken.nextToken());
        int groupCount = Integer.parseInt(inputToken.nextToken());
        int[] heights = new int[childCount];

        inputToken = new StringTokenizer(br.readLine());
        for(int i=0; i < childCount; i++){
            heights[i] = Integer.parseInt(inputToken.nextToken());
        }
        Arrays.sort(heights);

        int[] diff = new int[childCount-1];
        for(int i=0; i < childCount-1; i++){
            diff[i] = heights[i+1] - heights[i];
        }
        Arrays.sort(diff);

        int result = 0;
        for(int i=0; i <  childCount - groupCount; i++){
            result += diff[i];
        }
        System.out.println(result);

    }
}
