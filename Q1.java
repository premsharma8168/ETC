package CONTENT.Z_scraped;
import java.util.Arrays;

public class Q1 {
    public static void mergeAndRearrange(int[] A, int[] B) {
        int N = A.length;
        int L = B.length;

        
        int[] merged = new int[N + L];
        System.arraycopy(A, 0, merged, 0, N);
        System.arraycopy(B, 0, merged, N, L);

        
        Arrays.sort(merged);

        
        for (int i = 0; i < N; i++) {
            A[i] = merged[i];
        }

        
        for (int i = 0; i < L; i++) {
            B[i] = merged[N + i];
        }

        
        System.out.println("Merged & Sorted Array: " + Arrays.toString(merged));
    }

    public static void main(String[] args) {
        int[] A = {1, 5, 9};
        int[] B = {2, 3, 10, 14};

        mergeAndRearrange(A, B);

        System.out.println("Array A: " + Arrays.toString(A));
        System.out.println("Array B: " + Arrays.toString(B));
    }
}