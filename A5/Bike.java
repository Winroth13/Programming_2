public class Bike extends Vehicle {
    int gears;

    public Bike(int price, int weight, String colour, int gears) {
        this.price = price;
        this.weight = weight;
        this.colour = colour;
        this.gears = gears;
    };

    public void printInfo() {
        System.out.printf("Price: %d\nWeight: %d\nColour: %s\nGears: %d\n", price, weight, colour, gears);
    }
}
