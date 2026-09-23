package tools;
import java.util.Optional;

public enum Operacoes {
    SOMA("+") {
        @Override
        public double calcular(double a, double b) { return a + b; }
    },
    SUBTRACAO("-") {
        @Override
        public double calcular(double a, double b) { return a - b; }
    },
    MULTIPLICACAO("*") {
        @Override
        public double calcular(double a, double b) { return a * b; }
    },
    DIVISAO("/") {
        @Override
        public double calcular(double a, double b) {
            if (b == 0) {
                throw new ArithmeticException("Erro: Divisão por zero não é permitida.");
            }
            return a / b;
        }
    },
    POTENCIACAO("pow") {
        @Override
        public double calcular(double a, double b) { return Math.pow(a, b); }
    },

    MODULO("%") {
        @Override
        public double calcular(double a, double b) { return a % b; }
    },
    MAX("max") {
        @Override
        public double calcular(double a, double b) { return Math.max(a, b); }
    },
    MIN("min") {
        @Override
        public double calcular(double a, double b) { return Math.min(a, b); }
    };



    private final String simbolo;

    Operacoes(String simbolo) {
        this.simbolo = simbolo;
    }

    public String getSimbolo() {
        return simbolo;
    }

    public abstract double calcular(double a, double b);



    public static Optional<Operacoes> buscarPorSimbolo(String entrada) {
        for (Operacoes op : values()) {
            if (op.getSimbolo().equalsIgnoreCase(entrada) || op.name().equalsIgnoreCase(entrada)) {
                return Optional.of(op);
            }
        }
        return Optional.empty();
    }
}
