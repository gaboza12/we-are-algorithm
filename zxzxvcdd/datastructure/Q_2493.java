package zxzxvcdd.datastructure;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Q_2493 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        class Tower{
            int index;
            int height;
            public Tower(int index, int height) {
                this.index = index;
                this.height = height;
            }
        }
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int towerCount =  Integer.parseInt(br.readLine());
        StringTokenizer inputToken = new StringTokenizer(br.readLine());
        
        Stack<Tower> towerStack = new Stack<>();


        for (int i = 0; i < towerCount; i++) {
            int height = Integer.parseInt(inputToken.nextToken());
            
            while(!towerStack.isEmpty() && height > towerStack.peek().height){
                towerStack.pop();
            }
            
            int result = towerStack.isEmpty()? 0 : towerStack.peek().index+1;

            System.out.print(result+" ");

            towerStack.push(new Tower(i,height));
        }

        br.close();

    }
}
