import java.util.Scanner;

public class BMI {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Much do you weigh? (kg)");
        float weight = input.nextFloat();

        System.out.println("How tall are you? (m)");
        float height = input.nextFloat();

        input.close();

        double value = weight / Math.pow(height, 2);

        System.out.println("Your BMI is " + value);
    }
}
