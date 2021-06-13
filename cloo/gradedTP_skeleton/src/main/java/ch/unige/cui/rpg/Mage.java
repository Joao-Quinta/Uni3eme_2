package ch.unige.cui.rpg;


public class Mage extends GameChar{
	protected Ressource mana;
	
	public Mage(String name, int maxHp, int maxMana) {
		super(name, maxHp);
		this.mana = new Ressource(maxMana, maxMana, RessourceType.MANA);
	}
	
	@Override
	public boolean hasMana() {
		return true;
	}
	
	@Override
	public Ressource getMana() {
		return mana;
	}
	
	public String toString() {
		return "I am " + super.name + "! I have " + String.valueOf(health.getVal()) + " hp, and " + String.valueOf(mana.getVal()) + " mana";
	}


	
	

}
