import entities.Historico;
import tools.Operacoes;

import java.util.Scanner;
import java.util.Optional;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Historico historico = new Historico();

        while (true) {

            System.out.println("Operações disponíveis:");
            for (Operacoes op : Operacoes.values()) {
                System.out.println(op + ": " + op.getSimbolo());
            }

            System.out.println("Digite a operação (nome ou símbolo) ou 'hist' para histórico, 'sair' para encerrar: ");
            String entradaOp = sc.next();

            if (entradaOp.equalsIgnoreCase("sair")) {
                System.out.println("Encerrando");
                break;
            }

            if (entradaOp.equalsIgnoreCase("hist")) {
                historico.exibir();
                continue;
            }

            Optional<Operacoes> operacaoOpt = Operacoes.buscarPorSimbolo(entradaOp);

            if (operacaoOpt.isEmpty()) {
                System.out.println("Erro: Operação inválida.");
                continue;
            }

            Operacoes operacao = operacaoOpt.get();

            System.out.print("Digite o primeiro número: ");
            double num1 = sc.nextDouble();

            System.out.print("Digite o segundo número: ");
            double num2 = sc.nextDouble();

            try {

                double resultado = operacao.calcular(num1, num2);
                System.out.printf("Resultado: %.2f\n", resultado);

                historico.adicionar(num1, operacao.getSimbolo(), num2, resultado);

            } catch (ArithmeticException e) {
                System.out.println(e.getMessage());
            }
        }
        sc.close();
    }
}
