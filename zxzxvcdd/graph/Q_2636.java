package zxzxvcdd.graph;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q_2636 {
    
    public static class Pos{
        int r, c;
        Pos(int r, int c){
            this.r = r;
            this.c = c;
        }
    }

    static int n, m;
    static int[][] cheese;
    static boolean[][] visited;
    static int[] dr = {0, 0, -1, 1};
    static int[] dc = {-1, 1, 0, 0};
    static int time, count;

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer input = new StringTokenizer(br.readLine());
        n = Integer.parseInt(input.nextToken());
        m = Integer.parseInt(input.nextToken());

        cheese = new int[n][m];
        for(int i=0; i<n; i++){
            input = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++){
                cheese[i][j] = Integer.parseInt(input.nextToken());
                if(cheese[i][j]==1) count++;
            }
        }

        visited = new boolean[n][m];
        visited[0][0] = true;
        
        bfs();
    }

    public static void bfs(){

        Queue<Pos> q = new LinkedList<>();
        q.offer(new Pos(0, 0));
        visited = new boolean[n][m];
        visited[0][0] = true;

        int melted = 0;
        time++;
        
        while(!q.isEmpty()){
            Pos p = q.poll();
            for(int i=0; i<4; i++){
                int nr = p.r + dr[i];
                int nc = p.c + dc[i];

                if(nr<0 || nc<0 || nr>=n || nc>=m || visited[nr][nc]) continue;

                visited[nr][nc] = true;

                if(cheese[nr][nc]==0){
                    q.offer(new Pos(nr, nc));
                }
                else{
                   
                    cheese[nr][nc] = 0;
                    melted++;
                }
            }
        }

        count -= melted;

        if(count==0){
            System.out.println(time);
            System.out.println(melted);
            return;
        }
        else{
            bfs();
        }
    }


}
