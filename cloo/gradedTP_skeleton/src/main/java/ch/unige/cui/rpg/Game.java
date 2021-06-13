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
		
		System.out.println("mage tente de cast Frostbolt sur warrior :");
		System.out.println(mageChar.cast(frostbolt));
		
		System.out.println();
		System.out.println(mageChar.toString());
		System.out.println(warriorChar.toString());
		System.out.println();
		
		System.out.println("warrior tente de boir une potion de vie :");
		System.out.println(warriorChar.cast(healthPot));
		
		System.out.println();
		System.out.println(mageChar.toString());
		System.out.println(warriorChar.toString());
		System.out.println();
		
		System.out.println("warrior tente de cast Charge sur le mage");
		System.out.println(warriorChar.cast(charge));
		
		System.out.println();
		System.out.println(mageChar.toString());
		System.out.println(warriorChar.toString());
		System.out.println();
		

	}
}