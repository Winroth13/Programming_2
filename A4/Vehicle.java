public abstract class Vehicle {
    int price;
    int weight;
    String colour;

    public void printInfo() {
        System.out.printf("Price: %d\nWeight: %d\nColour: %s\n", price, weight, colour);
    }
}
