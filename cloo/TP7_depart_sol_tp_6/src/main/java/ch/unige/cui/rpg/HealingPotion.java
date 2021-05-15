package ch.unige.cui.rpg;

public class HealingPotion implements Item {

    private final String name;
    private final int HP;
    private final int weight;
    private final int minLvl;
    private final int price;

    public HealingPotion(String name, int HP, int weight, int minLvl, int prix){
        this.name=name;
        this.HP=HP;
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

    public int getHP(){
        return HP;
    }

    public int getMinLvl() {
        return minLvl;
    }

    
    @Override
    public String toString() {
        return "HealingPotion [HP=" + HP + ", minLvl=" + minLvl + ", name=" + name + ", weight=" + weight + ", price=" + price + "]";
    }

	public int getPrice() {
		return price;
	}
    
}