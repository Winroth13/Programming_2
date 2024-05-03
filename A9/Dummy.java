import javax.swing.*;
import java.util.*;
import java.awt.*;

public class Dummy implements Entity {

  private final ImageIcon image = new ImageIcon("unknown.gif");

  protected Point position;

  protected Pasture pasture;

  public Dummy(Pasture pasture) {
    this.pasture = pasture;
  }

  public Dummy(Pasture pasture, Point position) {
    this.pasture = pasture;
    this.position = position;
  }

  public Point getPosition() {
    return position;
  }

  public void setPosition(Point newPosition) {
    position = newPosition;
  }

  public void tick() {
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
  }

  public String type() {
    return "Dummy";
  }

  public ImageIcon getImage() {
    return image;
  }
}
