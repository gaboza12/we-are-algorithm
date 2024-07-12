package zxzxvcdd.divideAndConquer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_14601 {
    
    static int tileNo;
    static int[][] tileMap;
    public static void main(String[] args) throws NumberFormatException, IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int length = (int) Math.pow(2, Integer.parseInt(br.readLine()));
        StringTokenizer inputToken = new StringTokenizer(br.readLine());
        int holeX = Integer.parseInt(inputToken.nextToken());
        int holeY = Integer.parseInt(inputToken.nextToken());


        tileMap = new int[length][length];
        
        tileMap[holeY-1][holeX-1] = -1;

        placementTile(0,0,length);

        StringBuilder result = new StringBuilder();
        for(int i=length-1; i >= 0; i--){
            for(int j=0; j < length; j++){
                result.append(tileMap[i][j]+" ");
            }
            result.append("\n");
        }
        System.out.println(result.toString());
    }

    static void placementTile(int x, int y, int size){

        tileNo++;

        int resize = size/2 ;

        if(isValidPlace(x, y, resize)) tileMap[x + resize - 1][y + resize - 1] = tileNo;
        if(isValidPlace(x, y + resize, resize)) tileMap[x + resize-1][y + resize] = tileNo;
        if(isValidPlace(x + resize, y, resize)) tileMap[x + resize][y + resize-1] = tileNo;
        if(isValidPlace(x + resize, y + resize, resize)) tileMap[x + resize][y + resize] = tileNo;

        if(size==2) return;

        placementTile(x, y, resize);
        placementTile(x, y + resize, resize);
        placementTile(x + resize, y, resize);
        placementTile(x + resize, y + resize, resize);

    }

    static boolean isValidPlace(int x, int y, int size){
        for(int i = x; i< x+size; i++){
            for(int j = y; j < y+size; j++){
                if(tileMap[i][j] != 0) return false;
            }
        }
        return true;
    }

}
