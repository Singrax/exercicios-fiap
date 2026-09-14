import entities.Moeda;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        //Cria uma lista pra abrigar as moedas
        List<Moeda> moedas = new ArrayList<>();

        // Instanciona as moedas na lista
        Moeda dolarAm = new Moeda("Dolar Americano", "$",1);
        moedas.add(dolarAm);
        Moeda euro = new Moeda("Euro", "€",1.15);
        moedas.add(euro);
        Moeda real = new Moeda("Real", "R$", 5.15);
        moedas.add(real);

        //Imprime a lista de todas as moedas
        System.out.println("Moedas:");
        for (Moeda moeda : moedas) {
            System.out.println(moeda);
        }

        //Coleta a primeira moeda e valor
        System.out.println("Escreva o primeiro valor (exemplo: 'R$ 10.00)' ");
        String valor[] = sc.nextLine().split(" ");
        String m1cifra =  valor[0];
        double m1valor = Double.parseDouble(valor[1]);

        //Coleta a segunda moeda
        System.out.println("Escreva a moeda a ser convertida (exemplo: 'Dolar Americano') ");
        String valor2= sc.nextLine();
        double valorConvertido = 0;
        String m2cifra = " ";

        //Checa e calcula baseado exatamente nos valores das moedas escolhidas
        for (Moeda moeda1 : moedas) {
            //acha a moeda certa baseado no nome e recolhe a cifra
            if (moeda1.getNome().equals(valor2)) {
                m2cifra = moeda1.getCifra();

                if(m2cifra.equals(m1cifra)) {
                    valorConvertido = m1valor;
                }

                else {
                    for (Moeda moeda2 : moedas) {
                        if (moeda2.getCifra().equals(m1cifra)) {}
                        valorConvertido = (m1valor * moeda1.getValor()) * moeda2.getValor();
                    }
                }
            }
        }
        System.out.println("Valor convertido: " + m2cifra + String.format("%.2f", valorConvertido));

        sc.close();

    }
}
