import java.util.*;
import java.awt.*;

public abstract class Animal extends LivingThing {
    protected int maxFood = 5;

    protected int currentFood = maxFood;

    protected Pasture pasture;

    protected int ticks;

    protected int ticksPerMove;

    public Animal(Pasture pasture, int ticksPerMove) {
        this.pasture = pasture;
        this.ticksPerMove = ticksPerMove;
    }

    public Animal(Pasture pasture, Point position, int ticksPerMove) {
        this.pasture = pasture;
        this.position = position;
        this.ticksPerMove = ticksPerMove;
    }

    public void move() {
        ticks += 1;
        if (ticks % ticksPerMove == 0) {
            Random rand = new Random();
            int randInt = rand.nextInt(4);
            int newX;
            int newY;
            if (randInt == 0) {
                newX = (int) getPosition().getX() + 1;
                newY = (int) getPosition().getY();
            } else if (randInt == 1) {
                newX = (int) getPosition().getX() - 1;
                newY = (int) getPosition().getY();
            } else if (randInt == 2) {
                newX = (int) getPosition().getX();
                newY = (int) getPosition().getY() + 1;
            } else {
                newX = (int) getPosition().getX();
                newY = (int) getPosition().getY() - 1;
            }

            if (newX < pasture.getWidth() && newX >= 0 && newY < pasture.getHeight() && newY >= 0) {
                setPosition(new Point(newX, newY));
            }

            if (currentFood == 0) {
                pasture.removeEntity(this);
            }

            currentFood -= 1;
        }
    }
}
