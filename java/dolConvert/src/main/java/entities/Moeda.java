package entities;

import java.util.Scanner;

public class Moeda {
    private double valor;
    private String cifra;
    private String nome;

    public Moeda(String nome, String cifra,  double valor) {
        this.valor = valor;
        this.cifra = cifra;
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public String getCifra() {
        return cifra;
    }

    public void setCifra(String cifra) {
        this.cifra = cifra;
    }

    public double Convesao(Moeda m1, Moeda m2){
        return m1.getValor() * m2.getValor();
    }

    @Override
    public String toString() {
        return nome + ": " + cifra + String.format("%.2f", valor);
    }
}
