package ch.unige.cui.rpg;

public class ManaPotion implements Potion {

    private final String name;
    private final int mana;
    private final int weight;
    private final int price;

    public ManaPotion(String name, int mana, int weight, int price){
        this.name=name;
        this.mana=mana;
        this.weight=weight;
        this.price=price;
    }

    public int getWeight(){
        return weight;
    }

    public String getName(){
        return name;
    }

    public int getPotionValue(){
        return mana;
    }

    public int getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return "ManaPotion [ mana=" + mana + ", price=" + price + ", name=" + name + ", weight=" + weight + "]";
    }
    
}