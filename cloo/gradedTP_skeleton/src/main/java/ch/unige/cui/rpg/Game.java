package ch.unige.cui.rpg;

public class Game{
	public static void main(String[] args){
		System.out.println("Successfully entered in main.");
		System.out.println();
		
		Mage mageChar = new Mage("mage", 100, 100);
		Warrior warriorChar = new Warrior("warrior", 100, 100);
		
		Spell frostbolt = new Spell(-10, -20, PossibleTarget.TARGET, RessourceType.MANA, RessourceType.HEALTH, true);
		Spell charge = new Spell(0, 20, PossibleTarget.PLAYER, RessourceType.HEALTH, RessourceType.RAGE, true);
		Potion healthPot = new Potion(15, RessourceType.HEALTH);
		
		mageChar.setTarget(warriorChar);
		warriorChar.setTarget(mageChar);
		
		System.out.println("Voici les personnages :");	
		System.out.println(mageChar.toString());
		System.out.println(warriorChar.toString());
		System.out.println();		
		
		mageChar.cast(frostbolt);
		
		System.out.println("mage cast Frostbolt sur warrion");
		System.out.println(mageChar.toString());
		System.out.println(warriorChar.toString());
		System.out.println();
		
		warriorChar.cast(healthPot);
		
		System.out.println("warrior consomme une potion de vie");
		System.out.println(mageChar.toString());
		System.out.println(warriorChar.toString());
		System.out.println();
		
		warriorChar.cast(charge);
		
		System.out.println("warrior cast Charge sur le mage");
		System.out.println(mageChar.toString());
		System.out.println(warriorChar.toString());
		System.out.println();
		
		
		/*
		Mage mageChar = new Mage("mage", 100, 100);
		System.out.println(mageChar.toString());
		
		Spell frostbolt = new Spell(-10, 20, RessourceType.MANA);
		
		mageChar.cast(frostbolt);
		
		System.out.println(mageChar.toString());
		
		Potion manaPotion = new Potion(20, RessourceType.MANA);
		
		mageChar.cast(manaPotion);
		
		System.out.println(mageChar.toString());
		*/

	}
}