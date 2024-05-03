import javax.swing.*;
import java.awt.*;
import java.util.*;

public class Wolf extends Animal {
    private final ImageIcon image = new ImageIcon("wolf.gif");

    public Wolf(Pasture pasture) {
        super(pasture, 2);
    }

    public Wolf(Pasture pasture, Point position) {
        super(pasture, position, 2);
    }

    public void tick() {
        move();

        Collection world = pasture.getEntities();
        Iterator it = world.iterator();

        while (it.hasNext()) {
            Entity e = (Entity) it.next();
            Point pos = e.getPosition();
            String type = e.type();
            if (pos.equals(position) && type.equals("Sheep")) {
                pasture.removeEntity(e);
                this.currentFood = this.maxFood;
                if (this.ticks > 10) {
                    this.ticks = this.ticks % this.ticksPerMove;
                    Entity wolf = new Wolf(pasture, this.position);
                    pasture.addEntity(wolf);
                }
            }
        }
    }

    public String type() {
        return "Wolf";
    }

    public ImageIcon getImage() {
        return image;
    }
}
