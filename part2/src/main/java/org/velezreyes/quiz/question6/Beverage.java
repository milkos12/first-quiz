package org.velezreyes.quiz.question6;

public class Beverage implements Drink{
    private String name;
    private Boolean fizzy;
    private Double price;

    public Beverage (String name, Boolean fizzy, Double price) {
        this.name = name;
        this.fizzy = fizzy;
        this.price = price;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public boolean isFizzy() {
        return this.fizzy;
    }

    public Double getPrice() {
        return this.price;
    }
}
