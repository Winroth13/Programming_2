// UsesTimeStampedVariable.java

import java.util.Scanner;

public class UsesTimeStampedVariable {

    public static void main(String[] args) {
        TimeStampedVariable<String> minVariabel1 = new TimeStampedVariable<String>("AB");
        TimeStampedVariable<Integer> minVariabel2 = new TimeStampedVariable<Integer>(5);
        TimeStampedVariable<Double> minVariabel3 = new TimeStampedVariable<Double>(3.14);

        Scanner input = new Scanner(System.in);

        System.out.println("Vilket värde ska minVariabel1 ha?");
        String nyaVardet = input.nextLine();

        minVariabel1.updateVariable(nyaVardet);

        input.close();

        System.out.println("minVariabel1 ändrades: " + minVariabel1.getTimeStamp());
        System.out.println("minVariabel2 ändrades: " + minVariabel2.getTimeStamp());
        System.out.println("minVariabel3 ändrades: " + minVariabel3.getTimeStamp());

        minVariabel1.printVariable();
        minVariabel2.printVariable();
        minVariabel3.printVariable();
    }
}
