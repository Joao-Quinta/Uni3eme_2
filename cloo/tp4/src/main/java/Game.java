package main.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;

import main.java.ch.unige.cui.rpg.*;
import main.java.ch.unige.cui.rpg.Character;


public class Game{
	public static void main(String[] args){
		
		// je definis une premiere armure -> 10 de déffence nature, 20 déffence feu
		ArrayList<String> armorTypeP1 = new ArrayList<String>( Arrays.asList("nature", "feu"));
		ArrayList<Integer> armorAmountP1 = new ArrayList<Integer>( Arrays.asList(10, 20));
		Damage piece1 = new Damage(armorTypeP1, armorAmountP1);
		
		// je definis une deuxieme armure -> 10 de déffence nature, 20 déffence electrique
		ArrayList<String> armorTypeP2 = new ArrayList<String>( Arrays.asList("nature", "electrique"));
		ArrayList<Integer> armorAmountP2 = new ArrayList<Integer>( Arrays.asList(10, 20));
		Damage piece2 = new Damage(armorTypeP2, armorAmountP2);
		
		//une piece sera la -below- et l autre la -above-
		
		/*
		//si je tente de equiper une 3eme piece, ca ne sera pas possible, et y aura aucun changement
		
		ArrayList<String> armorTypeP2 = new ArrayList<String>( Arrays.asList("nature", "ombre"));
		ArrayList<Integer> armorAmountP2 = new ArrayList<Integer>( Arrays.asList(10, 20));
		Damage piece2 = new Damage(armorTypeP2, armorAmountP2);
		*/
		
		//je cree un druid, qui a un nom, une vie, et des points d'armure
		Character druidEqui = new Character("druid Equi", 50, 10);
		// j equipe la premiere piece d armure
		druidEqui.equipProtection(piece1, 10, "below");
		// j equipe la deuxieme piece d armure
		druidEqui.equipProtection(piece2, 10, "above");
		
		Map<String, String> defence = druidEqui.getMyArmorPieces().getDamage().getTypesDmge();
		System.out.println(defence);
		
		// je definis l arme qui va attaquer mon personnage
		ArrayList<String> damageType = new ArrayList<String>( Arrays.asList("nature", "electrique"));
		ArrayList<Integer> damageAmount = new ArrayList<Integer>( Arrays.asList(40, 20));
		Damage arme = new Damage(damageType, damageAmount);
		//cette arme fait 40 de degats nature -> mon personnage peut "enlever" 20, et peut enlever 20 de lectrique aussi
		//du coup je prends au total 20 degats, je dois donc finir à 40 de vie (j avais 50 + 10 armure)
		
		
		System.out.println(druidEqui.toString());
		// mon personnage prends du degats
		Damage actualDamage = druidEqui.getMyArmorPieces().absorb(arme);
		druidEqui.wound(Integer.valueOf(actualDamage.getTypesDmge().get("damage")));
		System.out.println(druidEqui.toString());
		
		// protectionStack -> entité
		// damage -> value
		
		// ProtectionStack est une entité, car avec le temps elle peut évoluer, on peut équiper des pièces (eventuellement en déséquiper), ces attributs ne sont donc pas définissants
		// damage est un value objetct, car 2 pieces qui ont le meme type de déffence sont égales,et les protections ne peuvent pas évoluer avec le temps
		

		Damage piece3 = new Damage(armorTypeP2, armorAmountP2);
		System.out.println(piece2.equals(piece3));
		System.out.println(piece2.hashCode() == piece3.hashCode());
	}
}