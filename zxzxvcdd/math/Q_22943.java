package zxzxvcdd.math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Q_22943 {

    static boolean[] isUnDecimals;
    static List<Integer> decimals;
    static Set<Integer> decimalSum;
    static Set<Integer> decimalMult;
    static int numIndex;
    static int maxNum;
    static int validCnt;
    static int target;
    static boolean[] used = new boolean[10];

    

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer inputToken = new StringTokenizer(br.readLine());
        numIndex = Integer.parseInt(inputToken.nextToken());
        setMaxNum();
        target = Integer.parseInt(inputToken.nextToken());

        checkDecimal();
        setSumAndMult();
        validCnt = 0;        
        calcCnt(0, 0);

        System.out.println(validCnt);

    }

    static void calcCnt(int index, int value) {
        if (index == numIndex) {
            if (isValid(value))
                validCnt++;
            return;
        }
        for (int i = 0; i <= 9; i++) {
            if (i==0 && index==0 || used[i]) continue;
            used[i] = true;
            calcCnt(index+1, value*10+i);
            used[i] = false;
        }
    }


    static boolean isValid(int value) {
       
        if(decimalSum.contains(value)){
            while (value%target==0) value/=target;
            return decimalMult.contains(value);
        }
        return false;
    }

    static void setMaxNum() {

        int cnt = 9;

        for(int i=0; i < numIndex; i++){
            maxNum *= 10;
            maxNum += cnt;
            cnt--;
        }

    }

    static void checkDecimal() {

        decimals= new ArrayList<>();
        isUnDecimals = new boolean[maxNum + 1];
        isUnDecimals[0] = isUnDecimals[1] = true;
 
        for (int i = 2; i <= maxNum; i++) {
            if (!isUnDecimals[i]) {
                for (int j = 2; i * j <= maxNum; j++) {
                    isUnDecimals[i * j] = true;
                }
                decimals.add(i);
            }
        }
    }

    static void setSumAndMult(){
        decimalMult = new HashSet<>();
        decimalSum = new HashSet<>();
        for (int i = 0; i < decimals.size(); i++) {
            for (int j = i; j < decimals.size(); j++) {
                int a = decimals.get(i);
                int b = decimals.get(j);
                long mult = (long)(a) * (long)(b);
                if (mult <= maxNum)
                    decimalMult.add((int)mult);
                if (a!=b) {
                    int sum = a+b;
                    if (sum <= maxNum)
                        decimalSum.add(sum);
                }
            }
        }
    }

}
