package zxzxvcdd.math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_1188 {
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer inputToken = new StringTokenizer(br.readLine());

        int sausages = Integer.parseInt(inputToken.nextToken());
        int critics = Integer.parseInt(inputToken.nextToken());

        int result = critics - slicing(sausages,critics);
        

        System.out.println(result);

    }

    private static int slicing(int sausages, int critics) {
        return sausages%critics==0? critics : slicing(critics, sausages%critics);
    }
}
