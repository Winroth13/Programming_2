import javax.swing.*;
import java.awt.*;

public abstract class LivingThing implements Entity {
    protected Point position;

    public Point getPosition() {
        return position;
    }

    public void setPosition(Point newPosition) {
        position = newPosition;
    }

    public abstract void tick();

    public abstract ImageIcon getImage();

    public abstract String type();
}
