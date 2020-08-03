import java.io.*;
import java.util.Arrays;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    public static int[] arr;
    public static int N, M;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[M];
        rec(1,0);
        System.out.println(sb);

    }

    public static void rec(int at, int depth){

        if(depth == M){
            for(int val : arr){
                sb.append(val).append(' ');
            }
            sb.append('\n');
            return ;
        }

        for(int i = at; i <= N; i++){
            arr[depth] = i;
            rec(i+1, depth+1);
        }
    }
}