package ch.unige.cui.rpg;

public class Game{
	public static void main(String[] args){
		System.out.println("Successfully entered in main.");
		CharProfile mageProfile = new CharProfile(1,0,0,0,0);
		MageClass mage = new MageClass("mage", 10, 10, new ProtectionStack(null, null),mageProfile);
		mage.levelUp(mageProfile);
	}
}