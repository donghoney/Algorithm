import java.io.*;
import java.util.Arrays;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    public static int[] arr = new int[12];
    public static int[] op = new int[4];
    public static int N;
    public static int max = Integer.MIN_VALUE;
    public static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<4; i++){
            op[i] = Integer.parseInt(st.nextToken());
        }

        dfs(1, arr[0]);

        System.out.println(max);
        System.out.println(min);
    }

    public static void dfs(int index, int result){
        if(index==N){
            max = Math.max(result, max);
            min = Math.min(result, min);
            return;
        }

        for(int i=0; i<4; i++){

            if(op[i]>0){

                op[i]--;
                switch (i){
                    case 0: dfs(index+1, result+arr[index]); break;
                    case 1: dfs(index+1, result-arr[index]); break;
                    case 2: dfs(index+1, result*arr[index]); break;
                    case 3: dfs(index+1, result/arr[index]); break;
                }
                op[i]++;

            }

        }
    }
}