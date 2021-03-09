package ch.unige.cui.rpg;
import java.lang.Math;

@SuppressWarnings("unused")

public class Character{
	private String nom;
	private int hpMax;
	private int hpCurrent;
	private int armor;
	private int gold;
	private Quest currentQuest;
	
	public Character(String nom, int hpMax, int armor) {
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
		return "Je suis " + nom + " j'ai " + String.valueOf(hpCurrent) + " points de vie, " + String.valueOf(armor) + " d'armure, " + String.valueOf(gold) + " or. " + questInfo;
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
}
