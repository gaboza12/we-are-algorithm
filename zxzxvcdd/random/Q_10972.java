package zxzxvcdd.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_10972 {

    static int n;
    static int[] arr;

    public static void main(String[] args) throws NumberFormatException, IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        arr = new int[n];
        
        StringTokenizer input = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(input.nextToken());
        }

        if(getResult()) {
            for(int i=0; i<n; i++) System.out.print(arr[i] + " ");
        } else {
            System.out.println(-1);
        }

    }

    public static boolean getResult() {

        int i = arr.length - 1;
        while(i>0 && arr[i-1] > arr[i]) {
            i--;
        }

        if(i==0) return false;

        int j = arr.length-1;

        while (arr[j] < arr[i-1]) {
                    j--;
                }
        swap(i-1, j);
        j = arr.length-1;
        while (i < j) {
            swap(i, j);
            i++; j--;
        }

        return true;
    }

    public static void swap(int idx1, int idx2) {
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }

}
