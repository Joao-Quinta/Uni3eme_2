package ch.unige.cui.rpg;

public class NullObject implements Item {
    private final String name;
    private final int weight;
    private final int minLvl;

    public NullObject(){
        name="";
        weight=0;
        this.minLvl=0;
    }

    public int getWeight(){
        return weight;
    }

    public String getName(){
        return name;
    }

    public int getMinLvl() {
        return minLvl;
    }

}