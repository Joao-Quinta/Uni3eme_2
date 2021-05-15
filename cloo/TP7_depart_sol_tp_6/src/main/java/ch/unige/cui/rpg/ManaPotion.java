package ch.unige.cui.rpg;

public class ManaPotion implements Item {


    private final String name;
    private final int mana;
    private final int weight;
    private final int minLvl;
    private final int price;
    
    public ManaPotion(String name, int mana, int weight, int minLvl, int prix){
        this.name=name;
        this.mana=mana;
        this.weight=weight;
        this.minLvl=minLvl;
        this.price = prix;
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
        return "ManaPotion [mana=" + mana + ", minLvl=" + minLvl + ", name=" + name + ", weight=" + weight + ", price=" + price + "]";
    }

	public int getPrice() {
		return price;
	}
    
}