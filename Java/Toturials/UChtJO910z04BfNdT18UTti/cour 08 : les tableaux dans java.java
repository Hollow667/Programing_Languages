//cour 08 : les tableaux dans java
import java.util.*;
import java.lang.*;
import java.io.*;
class Main {
    public static void main(String[] args) {
        //declearation et initialization
        //le vecteur: type[] nom-tab;
        int[] tab = {1, 2, 3, 4, 5};
        System.out.println(tab[0]);
        
        int[] tab2 = new int[5];
        tab2[0] = 1;
        tab2[1] = 2;
        tab2[2] = 3;
        tab2[3] = 4;
        tab2[4] = 5;
        System.out.println(tab[0]);

        // la martice: type [][] nom-martice
        int[][] mat = {{1, 2, 3},{4, 5, 6},{7, 8, 9}};
        int mat2[][] = new int[3][3];
        int i = 0;
        for(;i < 3;i++)
        {
            for (int j = 0;j < 3;j++)
            {
                mat2[i][j] = i * 3 + j + 1;
            }
        }
        
        //mat2 same as mat
        System.out.print(mat[1][2] + "=" + mat2[1][2] + '\n');
        
        for(int[] row: mat2)
        {
            System.out.println(row[0]);
        }
        
    }
    
}
