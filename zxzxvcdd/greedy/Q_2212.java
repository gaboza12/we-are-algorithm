package zxzxvcdd.greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q_2212 {
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int sensorCount = Integer.parseInt(br.readLine());
        int baseCount = Integer.parseInt(br.readLine());

        StringTokenizer inputToken = new StringTokenizer(br.readLine());
        
        int[] sensors = new int[sensorCount];
        for(int i=0; i < sensorCount; i++){
            sensors[i] = Integer.parseInt(inputToken.nextToken());
        }
        Arrays.sort(sensors);

        int[] distances = new int[sensorCount-1];
        for(int i=0; i < sensorCount-1; i++){
            distances[i] = sensors[i+1] - sensors[i];
        }
        Arrays.sort(distances);

        int result = 0;
        for(int i=0; i <  sensorCount - baseCount; i++){
            if(i > distances.length-1) break;
            result += distances[i];
        }
        System.out.println(result);
        

    }
}
