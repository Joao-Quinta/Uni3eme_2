package ch.unige.cui.rpg;

import java.util.ArrayList;
import java.util.List;

public class GameCharacter {
	private String name;
	private int healthPointsMax;
	private int healthPointsActu;
	private int mana;
	private int gold;
	private List<Item> bag;
	
	public GameCharacter(String name, int hpMax, int mana, int gold) {
		this.healthPointsMax = hpMax;
		this.healthPointsActu = hpMax;
		this.name = name;
		this.mana = mana;
		this.gold = gold;
		this.bag = new ArrayList<>();
	}
	
	public int getGold() {
		return this.gold;
	}
	
	public void setGold(int nGold) {
		gold = nGold;
	}
	
	public void addItem(Item obj) {
		bag.add(obj);
	}
	

}
