package entities;

import java.util.ArrayList;
import java.util.List;

public class Historico {
    private final List<String> registros = new ArrayList<>();

    public void adicionar(double a, String simbolo, double b, double resultado) {
        String registro = String.format("%.2f %s %.2f = %.2f", a, simbolo, b, resultado);
        registros.add(registro);
    }

    public void exibir() {
        System.out.println("Histórico de Operações");
        if (registros.isEmpty()) {
            System.out.println("Nenhuma operação encontrada");
        } else {
            for (int i = 0; i < registros.size(); i++) {
                System.out.println((i + 1) + ". " + registros.get(i));
            }
        }
    }
}