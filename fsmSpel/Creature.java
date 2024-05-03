import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;

public abstract class Creature {
    protected Point coordinate;
    protected int rotation;
    protected int radius;
    protected Color colour;
    protected int speed;

    protected Creature(Point startCoordinate, int rotation, int radius, Color colour, int speed) {
        if (radius <= 0) {
            throw new IllegalArgumentException("Radius must be a positive number");
        }
        if (rotation < 0 || rotation > 360) {
            throw new IllegalArgumentException("Rotation must be between 0 and 360");
        }
        if (colour == null) {
            throw new IllegalArgumentException("Colour must not be null");
        }
        if (speed <= 0) {
            throw new IllegalArgumentException("Speed must be a positive number");
        }
        if (startCoordinate == null) {
            throw new IllegalArgumentException("StartCoordinate must not be null");
        }
        this.coordinate = startCoordinate;
        this.rotation = rotation;
        this.radius = radius;
        this.colour = colour;
        this.speed = speed;
    }

    public void draw(Graphics g) {
        g.setColor(this.colour);
        g.fillOval(coordinate.x - radius / 2, coordinate.y - radius, radius, radius);
    }

    public abstract void update();

    protected boolean move(Point target) {
        double dx = target.x - coordinate.x;
        double dy = target.y - coordinate.y;
        double distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < speed) {
            return true;
        } else {
            double angle = Math.atan2(dy, dx);

            coordinate.x += Math.cos(angle) * speed;
            coordinate.y += Math.sin(angle) * speed;

            return false;
        }
    }
}