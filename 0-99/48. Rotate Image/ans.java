import java.util.*;

class Solution {
    public void rotate(int[][] matrix) {
        transpose(matrix);
        reflect(matrix);
    }

    public void transpose(int[][] matrix) {
        for (int i = 1; i<matrix.length; i++) {
            for (int j = 0; j < i; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
    }

    public void reflect(int[][] matrix) {
        for (int i = 0; i<matrix.length; i++) {
            for (int j = 0; j < matrix.length / 2; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix.length-1-j];
                matrix[i][matrix.length-1-j] = tmp;
            }
        }
    }

    public static void main(String[] args) {
        double d = 10.0/-0;
        if (d==Double.POSITIVE_INFINITY)
            System.out.println("pos");
        else
            System.out.println("neg");
    }
}