public class Car extends Vehicle {
    String regNumber;
    int fuelConsumption;

    public Car(int price, int weight, String colour, String regNumber, int fuelConsumption) {
        this.price = price;
        this.weight = weight;
        this.colour = colour;
        this.regNumber = regNumber;
        this.fuelConsumption = fuelConsumption;
    }

    public void printInfo() {
        System.out.printf("Price: %d\nWeight: %d\nColour: %s\nRegister nummer: %s\nFuel consumption: %d\n", price, weight, colour, regNumber, fuelConsumption);
    }
}
