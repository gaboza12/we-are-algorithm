package zxzxvcdd.disjointSet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
  
/*
문제
성규는 로봇을 조립해야 한다. 상자 안에는 여러 로봇의 부품들이 섞여 있다. 그런데 어떤 부품이 어느 로봇의 부품인지 표시가 되어있지 않다. 호재는 전자과라서 두 부품을 보면 같은 로봇의 부품인지 알 수 있다. 그래서 성규는 호재의 지시에 따라 부품들을 정리하기로 하였다.

부품들은 1부터 106까지의 정수로 표현된다. 그리고 부품 i가 속한 로봇은 robot(i)라고도 표현한다. 예를 들어, 부품 11과 부품 22가 로봇 A의 부품이라고 알고 있는 경우, robot(11)은 로봇 A를 의미하고, robot(22)도 로봇 A를 의미한다.

서로 다른 로봇은 공통 부품을 가지지 않는다. 즉 어떤 부품이 로봇 A의 부품이라면, 로봇 B의 부품은 될 수 없다.

호재는 2가지 지시를 한다.

서로 다른 부품 2개를 말해주며, 두 부품은 같은 로봇의 부품이라는 정보를 알려준다.
부품 i에 대해서, 지금까지 알아낸 robot(i)의 부품이 몇 개냐고 물어본다.
초기에는 부품에 대한 정보가 존재하지 않는다.

입력
첫 번째 줄에 호재의 지시 횟수 N이 들어온다. (1 ≤ N ≤ 106)

다음 줄부터 N개의 지시가 들어온다.

부품 2개가 같은 로봇의 부품인지 알려줄 때에는 
\(I\)  a b 의 형태로 들어온다. 부품 a와 부품 b는 같은 로봇의 부품이라는 의미이다. (1 ≤ a, b ≤ 106, a ≠ b, a, b는 정수)

어떤 로봇의 부품이 몇 개인지 물어볼 때에는 Q c 의 형태로 들어온다. 지금까지 알아낸 robot(c)의 부품이 몇 개냐는 의미이다. (1 ≤ c ≤ 106, c는 정수)

입력으로 Q c의 형태가 적어도 한 번 들어온다.

출력
Q로 시작하는 입력에 대해서 한 줄에 하나씩, 지금까지 알아낸 해당 로봇의 부품 개수를 출력한다.
*/
public class Q_18116 {
  
    public static void main(String[] args) throws IOException {

        class Union{

            int[] parent;
            int[] count;

            public Union(int size) {
                parent = new int[size];
                count = new int[size];
                for(int i = 0; i < size; i++){
                    parent[i] = i;
                    count[i] = 1;
                }
            }

            int getParent(int i){
                if(parent[i]==i) return i;

                return parent[i] = getParent(parent[i]);
            }

            void union(int a, int b){
                a = getParent(a);
                b = getParent(b);
                if(a!=b){
                    boolean flag = a > b;
                    int min = flag ? b : a;
                    int max = flag ? a : b;
                    count[min] += count[max];
                    parent[max] = min;
                }
            }

            int getCount(int a){
                return count[getParent(a)];
            }

        }
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int inputCount = Integer.parseInt(br.readLine());

        Union union = new Union(1000001);
        
        StringBuilder result = new StringBuilder();

        for(int i = 0; i < inputCount; i++){

            StringTokenizer inputToken = new StringTokenizer(br.readLine());
            
            String command = inputToken.nextToken();

            if(command.equals("I")){

                int partA = Integer.parseInt(inputToken.nextToken()) -1;
                int partB = Integer.parseInt(inputToken.nextToken()) -1;
                
                union.union(partA, partB);

            }else{

                int part = Integer.parseInt(inputToken.nextToken()) -1;
                result.append(union.getCount(part)+"\n");

            }
        }

        System.out.println(result.toString());
        
    }

}
