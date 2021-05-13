package ch.unige.cui.rpg;

public class ManaPotion implements Item {


    private final String name;
    private final int mana;
    private final int weight;
    private final int minLvl;

    public ManaPotion(String name, int mana, int weight, int minLvl){
        this.name=name;
        this.mana=mana;
        this.weight=weight;
        this.minLvl=minLvl;
    }

    public int getWeight(){
        return weight;
    }

    public String getName(){
        return name;
    }

    public int getMana(){
        return mana;
    }

    public int getMinLvl() {
        return minLvl;
    }

    
    @Override
    public String toString() {
        return "ManaPotion [mana=" + mana + ", minLvl=" + minLvl + ", name=" + name + ", weight=" + weight + "]";
    }
    
}