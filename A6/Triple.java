public class Triple<T, U, V> {
    protected T variable1;
    protected U variable2;
    protected V variable3;

    public Triple(T varable1, U variable2, V variable3) {
        this.variable1 = varable1;
        this.variable2 = variable2;
        this.variable3 = variable3;
    }

    public void printVariables() {
        System.err.printf("variable1: %s\n", variable1);
        System.err.printf("variable2: %s\n", variable2);
        System.err.printf("variable3: %s\n", variable3);
    }
}
