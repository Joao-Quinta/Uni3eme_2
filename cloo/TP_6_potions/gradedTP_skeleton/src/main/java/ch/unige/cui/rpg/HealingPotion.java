package ch.unige.cui.rpg;

public class HealingPotion implements Item{
	private String name;
	private int weight;
	private int minLvl;
	private int hp;
	
	public HealingPotion(String name, int health, int weight, int minLvl) {
		this.name = name;
		this.weight = weight;
		this.minLvl = minLvl;
		this.hp = health;
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
	
	public int getHp() {
		return this.hp;
	}

}
