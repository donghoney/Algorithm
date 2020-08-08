import java.io.*;
import java.util.Arrays;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    public static int N;
    public static int[][] arr;
    public static int max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = new int[N][2];

        for(int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<2; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i=0; i<N; i++) {
            dfs(i, arr[i][0], 0);
        }

        System.out.println(max);
    }

    public static void dfs(int index, int day, int money){
        if(index+day>N){
            max = Math.max(money, max);
            return;
        }
        else if(index+day == N){
            money += arr[index][1];
            max = Math.max(money, max);
            return;
        }
        else money += arr[index][1];

        for(int i = index+day; i<N; i++){
            dfs(i,arr[i][0],money);
        }
    }
}