package ch.unige.cui.rpg;

public class Weapon implements Item{
	private String name;
	private int weight;
	private int minLvl;
	private int damage;
	
	public Weapon(String name, int damage, int weight, int minLvl) {
		this.name = name;
		this.weight = weight;
		this.minLvl = minLvl;
		this.damage = damage;
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
	
	public int getDamage() {
		return this.damage;
	}
}
