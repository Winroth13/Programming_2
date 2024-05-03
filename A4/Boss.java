public class Boss extends Enemy {

    public Boss(int health) {
        super(health);
    }

    public void takeDamage(int damage) {
        hp -= damage / 2;
    }
}
