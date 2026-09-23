package tools;

import java.util.Optional;

public enum opTypes {
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

    opTypes(String simbolo) {
        this.simbolo = simbolo;
    }

    public String getSimbolo() {
        return simbolo;
    }

    //declaro que possui o metodo calcular vazio mesmo
    public abstract double calcular(double a, double b);

    public static Optional<opTypes> buscarPorSimbolo(String simbolo) {
        for (opTypes op : values()) {
            if (op.getSimbolo().equalsIgnoreCase(simbolo)) {
                return Optional.of(op);
            }
        }
        return Optional.empty();
    }
}
