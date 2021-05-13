package ch.unige.cui.rpg;

public class HealingPotion implements Item {

    private final String name;
    private final int HP;
    private final int weight;
    private final int minLvl;

    public HealingPotion(String name, int HP, int weight, int minLvl){
        this.name=name;
        this.HP=HP;
        this.weight=weight;
        this.minLvl=minLvl;
    }

    public int getWeight(){
        return weight;
    }

    public String getName(){
        return name;
    }

    public int getHP(){
        return HP;
    }

    public int getMinLvl() {
        return minLvl;
    }

    
    @Override
    public String toString() {
        return "HealingPotion [HP=" + HP + ", minLvl=" + minLvl + ", name=" + name + ", weight=" + weight + "]";
    }
    
}