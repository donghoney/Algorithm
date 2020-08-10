import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    public static int N;
    public static long ans = 0;
    public static long[][] arr;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        arr = new long[N+1][10];

        for(int i=1; i<=N; i++){

            for(int j=1; j<=9; j++){

                if(i == 1) arr[i][j] = 1;

                else if(i == 2){
                    if(j == 9) arr[i][j] = 1;
                    else arr[i][j] = 2;
                }

                else{
                    if(j == 1) arr[i][j] = (arr[i-2][j]+arr[i-1][j+1])%1000000000;
                    else if(j == 9) arr[i][j] = (arr[i-1][j-1])%1000000000;
                    else arr[i][j] = (arr[i-1][j-1]+arr[i-1][j+1])%1000000000;
                }

            }
        }

        for(int i=1; i<=9;i++) ans += arr[N][i];
        System.out.println(ans%1000000000);
    }
}