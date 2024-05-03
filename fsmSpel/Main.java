import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("FSM Guard");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1000, 500);

        final Creature[] creatures = {
                new Guard(new Point(100, 100), 0,
                        new Point[] {
                                new Point(100, 100),
                                new Point(200, 100),
                                new Point(100, 200)
                        }),
                new Guard(new Point(200, 200), 0,
                        new Point[] {
                                new Point(200, 200),
                                new Point(300, 200)
                        }),
        };

        final JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                for (Creature creature : creatures) {
                    creature.draw(g);
                }
            }
        };
        panel.setBackground(Color.BLACK);

        frame.add(panel);

        frame.addMouseListener(new MouseListener() {

            @Override
            public void mouseClicked(MouseEvent e) {
                for (Creature creature : creatures) {
                    if (creature instanceof Guard) {
                        ((Guard) creature).targetFound(e.getPoint());
                    }
                }
            }

            @Override
            public void mouseEntered(MouseEvent e) {
            }

            @Override
            public void mouseExited(MouseEvent e) {
            }

            @Override
            public void mousePressed(MouseEvent e) {
            }

            @Override
            public void mouseReleased(MouseEvent e) {
            }
        });

        new Timer(16, e -> {
            for (Creature creature : creatures) {
                creature.update();
            }
            panel.repaint();
        }).start();

        frame.setVisible(true);
    }
}