package ch.unige.cui.rpg;

import java.util.ArrayList;

public class Warrior extends GameChar{
	private Ressource rage;
	private ArrayList<Spell> spellBook;
	
	public Warrior(String name, int maxHp, int maxRage) {
		super(name, maxHp);
		this.rage = new Ressource(0, maxRage, RessourceType.RAGE);
	}
	
	@Override
	public boolean hasRage() {
		return true;
	}

	@Override
	protected Ressource getRage() {
		return rage;
	}
	
	public void addToSpellBook(Spell newSpell) {
		spellBook.add(newSpell);
	}
	
	public String toString() {
		return "I am " + super.name + "! I have " + String.valueOf(health.getVal()) + " hp, and " + String.valueOf(rage.getVal()) + " rage";
	}
	

}