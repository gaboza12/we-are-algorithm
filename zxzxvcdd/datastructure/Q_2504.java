package zxzxvcdd.datastructure;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Q_2504 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        Stack<Character> bracketStack = new Stack<>();
        int result = 0;
        int value = 1;

        for(int i= 0; i < input.length(); i++){
        
            char currentChar = input.charAt(i);
            int bracketValue = getBracketValue(currentChar);
            if(isCurrentStart(currentChar)){
                bracketStack.push(currentChar);
                value *= bracketValue;
            }else if(isCurrentEnd(currentChar)){
                if(bracketStack.isEmpty() || !matchBracket(bracketStack.peek(),currentChar)){
                    result=0;
                    break;
                }else if (matchBracket(input.charAt(i-1),currentChar)){
                    result += value;
                }
                bracketStack.pop();
                value /= bracketValue;
            }
        }

        if(!bracketStack.isEmpty()) result = 0;
        System.out.println(result);
    }

    static boolean isCurrentStart(char target){
        return target=='(' || target == '[';
    }

    static boolean isCurrentEnd(char target){
        return target==')' || target == ']';
    }

    static boolean matchBracket(char start, char end){
        boolean matched = false;
        
        if(isCurrentStart(start) && isCurrentEnd(end)){
            matched = (end - start) == 1 || (end - start) ==2; 
        }
        return matched;
    }

    static int getBracketValue(char bracket){
        
        boolean square = (bracket=='[' || bracket==']');
        return square ? 3 : 2;
    }



}
