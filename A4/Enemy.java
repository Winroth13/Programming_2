public class Enemy {
    int hp;

    public Enemy(int health) {
        hp = health;
    }

    public void takeDamage(int damage) {
        hp -= damage;
    }

    public void printHp() {
        System.err.println(hp);
    }
}
