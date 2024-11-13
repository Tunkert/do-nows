package javaPrograms.worksheets;

import java.util.Random;
import java.io.FileWriter;
import java.io.IOException;

public class QuadraticNonPerfectSquares {

    public static void appendToFile(String filename, String textToAppend) {
        try {
            FileWriter fw = new FileWriter(filename, true); // the true will append the new data
            fw.write("add a line\n");// appends the string to the file
            fw.close();
        } catch (IOException ioe) {
            System.err.println("IOException: " + ioe.getMessage());
        }
    }

    // create a random number
    public static int getRandomNumber() {
        Random random = new Random();
        return random.nextInt(101) + 50;
    }

    public static int notAPerfectSquare(int baseNumber) {
        int number = baseNumber;
        while (true) {
            if (!isPerfectSquare(number)) {
                return number;
            }
            number++;
        }
    }

    private static boolean isPerfectSquare(int num) {
        if (num < 0) {
            return false;
        }
        int sqrt = (int) Math.sqrt(num);
        return sqrt * sqrt == num;
    }

    public static void main(String[] args) {
        String filename = "simplifySquareRoots.html";
        for (int i = 0; i < 8; i++) {
            int aRandomNumber = getRandomNumber();
            int notPerfect = notAPerfectSquare(aRandomNumber);
            String notPerfectStr = String.valueOf(notPerfect);
            System.out.println(notPerfectStr);
            appendToFile(filename, notPerfectStr);
        }
    }
}