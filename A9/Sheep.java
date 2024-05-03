import javax.swing.*;
import java.awt.*;
import java.util.*;

public class Sheep extends Animal {
    private final ImageIcon image = new ImageIcon("sheep.gif");

    public Sheep(Pasture pasture) {
        super(pasture, 1);
    }

    public Sheep(Pasture pasture, Point position) {
        super(pasture, position, 1);
    }

    public void tick() {
        move();

        Collection world = pasture.getEntities();
        Iterator it = world.iterator();

        while (it.hasNext()) {
            Entity e = (Entity) it.next();
            Point pos = e.getPosition();
            String type = e.type();
            if (pos.equals(position) && type.equals("Plant")) {
                pasture.removeEntity(e);
                this.currentFood = this.maxFood;
                if (this.ticks > 10) {
                    this.ticks = this.ticks % this.ticksPerMove;
                    Entity sheep = new Sheep(pasture, this.position);
                    pasture.addEntity(sheep);
                }
            }
        }
    }

    public String type() {
        return "Sheep";
    }

    public ImageIcon getImage() {
        return image;
    }
}
