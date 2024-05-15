import java.awt.Color;
import java.awt.Point;

public class Guard extends FSM {
    private static final Patrol patrol = new Patrol();
    private static final Engage engage = new Engage();
    private static final ReturnToPatrol returnToPatrol = new ReturnToPatrol();

    private final static int radius = 50;
    private final static Color colour = Color.red;
    private final static int speed = 5;

    private final Point[] patrolPath;
    private int currentPointIndex = 0;
    private Point target;
    private Point returnLocation;

    public Guard(Point startCoordinate, int rotation, Point[] patrolPath) {
        super(startCoordinate, rotation, radius, colour, speed, patrol);
        
        if (patrolPath == null || patrolPath.length == 0) {
            throw new IllegalArgumentException("Patrolpath cannot be null or empty");
        }

        this.patrolPath = patrolPath;
        this.target = patrolPath[currentPointIndex];
    }

    private static class Patrol implements State {
        public void update(FSM guard) {
            Guard g = (Guard) guard;

            if (g.move(g.target)) {
                g.currentPointIndex = (g.currentPointIndex + 1) % g.patrolPath.length;
                g.target = g.patrolPath[g.currentPointIndex];
            }
        }
    }

    private static class Engage implements State {
        public void update(FSM guard) {
            Guard g = (Guard) guard;

            if (g.move(g.target)) {
                g.changeState(returnToPatrol);
            }
        }
    }

    private static class ReturnToPatrol implements State {
        public void update(FSM guard) {
            Guard g = (Guard) guard;

            if (g.move(g.returnLocation)) {
                g.changeState(patrol);
            }
        }
    }

    public void targetFound(Point location) {
        if (location == null) {
            throw new IllegalArgumentException("Target location cannot be null");
        }

        this.target = location;

        if (this.state == patrol) {
            this.returnLocation = this.coordinate;
        }

        this.changeState(engage);
    }
}