package ch.unige.cui.rpg;

public class NullObject implements Item {
    
    private final String name;
    private final int weight;
    private final int price;
    
    public NullObject(){
        name="";
        weight=0;
        price=0;
    }

    public int getWeight(){
        return weight;
    }

    public String getName(){
        return name;
    }

    public int getPrice() {
        return price;
    }

}