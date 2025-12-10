import java.io.*;
import java.util.Arrays;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        HashMap<String, Integer> map = new HashMap<>();

        String[] inp = br.readLine().split(" ");
        int n = Integer.parseInt(inp[0]);
        int m = Integer.parseInt(inp[1]);

        String[] pokemons = new String[n+1];

        for (int i = 1; i < n+1; i++) {
            String pokemon = br.readLine();
            map.put(pokemon, i);
            pokemons[i] = pokemon;
        }

        for (int i = 0; i < m; i++) {
            String q = br.readLine();
            Integer pok = map.getOrDefault(q, -1);
            if (pok.equals(-1)) {
                int idx = Integer.parseInt(q);
                bw.write(String.valueOf(pokemons[idx]));
            } else {
                bw.write(pok + "");
            }
            bw.write("\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
