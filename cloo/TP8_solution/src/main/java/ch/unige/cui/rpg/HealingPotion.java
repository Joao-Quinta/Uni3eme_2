package ch.unige.cui.rpg;

public class HealingPotion implements Potion {

    private final String name;
    private final int HP;
    private final int weight;
    private final int price;

    public HealingPotion(String name, int HP, int weight, int price){
        this.name=name;
        this.HP=HP;
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
        return HP;
    }

    public int getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return "HealingPotion [  HP=" + HP + ", name=" + name + ", price=" + price + ", weight=" + weight
                + "]";
    }
    
}