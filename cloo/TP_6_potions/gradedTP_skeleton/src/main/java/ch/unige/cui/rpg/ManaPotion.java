package ch.unige.cui.rpg;

public class ManaPotion implements Item{
	private String name;
	private int weight;
	private int minLvl;
	private int mana;
	
	public ManaPotion(String name, int mana, int weight, int minLvl) {
		this.name = name;
		this.weight = weight;
		this.minLvl = minLvl;
		this.mana = mana;
	}
	
	@Override
	public String getName() {
		return this.name;
	}
	
	@Override
	public int getWeight() {
		return this.weight;
	}

	@Override
	public int getMinLvl() {
		return this.minLvl;
	}
	
	public int getMana() {
		return this.mana;
	}

}
