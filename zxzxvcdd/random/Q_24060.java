package zxzxvcdd.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_24060 {

    static int size;
    static int targetIndex;
    static int[] tmp;
    static int cnt = 0;
    static int result = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer input = new StringTokenizer(br.readLine());

        size = Integer.parseInt(input.nextToken());
        targetIndex = Integer.parseInt(input.nextToken());

        int[] arr = new int[size];

        input = new StringTokenizer(br.readLine());
        for (int i = 0; i < size; i++) {
            arr[i] = Integer.parseInt(input.nextToken());
        }
        
        tmp = new int[size];
        mergeSort(arr, 0, size - 1);

        System.out.println(result);
    }

    static void mergeSort(int[] arr, int left, int right) {
        if(cnt > targetIndex) return;
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    static void merge(int[] arr, int left, int mid, int right) {

        int i = left;
        int j = mid + 1;
        int t = 0;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                tmp[t++] = arr[i++];
            } else {
                tmp[t++] = arr[j++];
            }
        }

        while (i <= mid) {
            tmp[t++] = arr[i++];
        }
        while (j <= right) {
            tmp[t++] = arr[j++];
        }

        i=left;
        t=0;

        while(i <= right){
            cnt++;

            if(cnt == targetIndex){
                result = tmp[t];

            }
        }

    }
}