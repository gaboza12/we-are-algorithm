package zxzxvcdd.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Q_4347 {


    public static void main(String[] args) throws NumberFormatException, IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCount = Integer.parseInt(br.readLine());
        StringBuilder result = new StringBuilder();
        for(int i=0; i< testCount; i++){

            int xCount= 0;
            int oCount = 0;

            char[][] grid = new char[3][3];
            for(int j=0; j < 3; j++){
                String inputToken = br.readLine();
                for(int k = 0; k < 3; k++){
                    char flag = inputToken.charAt(k);
                    grid[j][k] = flag;
                    if(flag=='O') oCount++;
                    if(flag=='X') xCount++;
                }
            }
            result.append(getResult(grid,xCount,oCount)+"\n");
            if (i < testCount - 1) {
                br.readLine();
            }
        }
        System.out.println(result.toString());
    }


    static String getResult(char[][] grid, int xCount, int oCount){

        boolean x =  checkResult(grid, 'X');
        boolean o = checkResult(grid, 'O');


        if ((x && o) || xCount < oCount) {
            return "no";
        } else if (x && xCount == oCount+1) {
            return "yes";
        } else if (o && xCount == oCount) {
            return "yes";
        } else if (!x && !o && (xCount == oCount || xCount == oCount + 1)) {
            return "yes";
        } else {
            return "no";
        }

    }

    static boolean checkResult(char[][] grid, char flag){

        for (int i = 0; i < 3; i++) {
            if ((grid[i][0] == flag && grid[i][1] == flag && grid[i][2] == flag) ||
                (grid[0][i] == flag && grid[1][i] == flag && grid[2][i] == flag)) {
                    return true;
            }
        }

        if ((grid[0][0] == flag && grid[1][1] == flag && grid[2][2] == flag) ||
            (grid[0][2] == flag && grid[1][1] == flag && grid[2][0] == flag)) {
                return true;
        }
        return false;
    }
    
}
