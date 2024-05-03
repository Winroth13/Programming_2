import java.awt.Color;
import java.awt.Point;

public abstract class FSM extends Creature {
    public interface State {
        void update(FSM fsm);
    }

    protected State state;

    public FSM(Point startCoordinate, int rotation, int radius, Color colour, int speed, State startState) {
        if (startState == null) {
            throw new IllegalArgumentException("StartState cannot be null");
        }
        super(startCoordinate, rotation, radius, colour, speed);
        this.state = startState;
    }

    public void update() {
        if (state != null) {
            state.update(this);
        }
    }

    public void changeState(State newState) {
        this.state = newState;
    }
}