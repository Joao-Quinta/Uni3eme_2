package ch.unige.cui.rpg;

public class Armor implements Item{
	private String name;
	private int weight;
	private int minLvl;
	private int protection;
	
	public Armor(String name,int protection, int weight, int minLvl) {
		this.name = name;
		this.weight = weight;
		this.minLvl = minLvl;
		this.protection = protection;
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
	
	public int getProtection() {
		return this.protection;
	}

}
