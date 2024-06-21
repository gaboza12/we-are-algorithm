package zxzxvcdd.datastructure2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Q_11286{

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int maxCount = Integer.parseInt(br.readLine());
        StringBuffer resultBuffer = new StringBuffer();
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b){
                if(Math.abs(a) == Math.abs(b)){
                    return a < b ? -1 : 1;
                } 
                return Math.abs(a) < Math.abs(b)? -1 : 1;
            }
        });

        for(int i=0; i < maxCount; i++){

            int value = Integer.parseInt(br.readLine());

            if(value==0){
                if(minHeap.isEmpty()){
                    resultBuffer.append("0\n");
                }else{
                    resultBuffer.append(minHeap.poll());
                    resultBuffer.append("\n");
                }

            }else {
                minHeap.add(value);
            }
        }
        System.out.println(resultBuffer.toString());
        br.close();
    }
}