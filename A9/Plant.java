import javax.swing.*;
import java.util.*;
import java.awt.*;

public class Plant extends LivingThing {
    private final ImageIcon image = new ImageIcon("plant.gif");

    protected Pasture pasture;

    protected int ticks;

    protected int ticksToGrow = 2;

    public Plant(Pasture pasture) {
        this.pasture = pasture;
    }

    public Plant(Pasture pasture, Point position) {
        this.pasture = pasture;
        this.position = position;
    }

    public void tick() {
        ticks += 1;
        if (ticks == ticksToGrow) {
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
                Entity plant = new Plant(pasture, new Point(newX, newY));
                pasture.addEntity(plant);
            }

            ticks = 0;
        }
    }

    public String type() {
        return "Plant";
    }

    public ImageIcon getImage() {
        return image;
    }
}
