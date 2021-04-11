package ch.unige.cui.rpg;

public class GameCharacter {
	private final String nom;
	private final int hpMax;
	private int hpCurrent;
	private int armor;
	private int gold;
	private Quest currentQuest;
	private ProtectionStack myArmorPieces;
	private boolean below = false;
	private boolean above = false;
	
	public GameCharacter(String nom, int hpMax, int armor) {
		this.nom = nom;
		this.hpMax = hpMax;
		this.hpCurrent = hpMax;
		this.armor = armor;
		this.setGold(0);
	}
	
	public void wound(int damage) {
		hpCurrent = hpCurrent - (damage - armor);
		if (!(hpCurrent > 0)) {
			hpCurrent = 0;
			System.out.println("Vous etes mort");	
		}
	}
	
	public void heal(int hp) {
		hpCurrent = Math.min(hpMax, hpCurrent + hp);
	}
	
	public void startQuest(Quest q) {
		currentQuest = q;
	}
	
	public String toString() {
		String questInfo = "Je n'ai pas de quete";
		if (!(currentQuest == null)) {
			questInfo = "Ma quete est de " + currentQuest.getDescription();	
		}
		return "Je suis " + nom + " j'ai " + String.valueOf(hpCurrent) + " points de vie, " + String.valueOf(armor) + " d'armure, " + String.valueOf(gold) + " or. " + questInfo + ".";
	}
	
	public void equipProtection(Protection prot) {
		if (!(this.above) && !(this.below)) {
			this.myArmorPieces = new ProtectionStack(prot, new Protection(0,0,0,0,0));
			this.below = true;
		}
		if (!(this.above)) {
			this.myArmorPieces = new ProtectionStack(prot, this.myArmorPieces);
			this.above = true;
		}
		if (this.above && this.below) {
			System.out.println("above and below equiped");
		}
		
	}
	
	public boolean getBelow() {
		return below;
	}
	
	public boolean getAbove() {
		return above;
	}
	
	public void setAbove(boolean above) {
		this.above = above;
	}
	
	public void setBelow(boolean below) {
		this.below = below;
	}
	
	public String getNom() {
		return nom;
	}

	public int getGold() {
		return gold;
	}

	public void setGold(int gold) {
		this.gold = gold;
	}

	public int getHpMax() {
		return hpMax;
	}
	
	public ProtectionStack getMyArmorPieces() {
		return myArmorPieces;
	}
	
	public void setMyArmorPieces(ProtectionStack prot) {
		this.myArmorPieces = prot;
	}

}
