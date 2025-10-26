package CONTENT.Z_scraped;

import java.util.*;

public class Main {
    public static int minSwaps(int[] arr) {
        int n = arr.length;
        int[][] arrPos = new int[n][2];

        for (int i = 0; i < n; i++) {
            arrPos[i][0] = arr[i];
            arrPos[i][1] = i;
        }

        Arrays.sort(arrPos, Comparator.comparingInt(o -> o[0]));
        boolean[] visited = new boolean[n];
        int swaps = 0;

        for (int i = 0; i < n; i++) {
            if (visited[i] || arrPos[i][1] == i) continue;

            int cycleSize = 0;
            int j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = arrPos[j][1];
                cycleSize++;
            }
            if (cycleSize > 1) swaps += (cycleSize - 1);
        }

        return swaps;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter array size:");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int ans = minSwaps(arr);
        System.out.println("Minimum swaps: " + ans);
    }
}