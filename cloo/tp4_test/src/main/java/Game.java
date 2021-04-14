package ch.unige.cui.game;
import ch.unige.cui.rpg.*;


public class Game{
	public static void main(String[] args){

		Quest q1 = new Quest("Holy grail quest",1000000);

		//armorVal=75,weight=27 [kg?]
		ChainMail scarletChestpieceOfTheBoar = new ChainMail(55,27);
		//fire prot=100, phys prot=26, weight=6
		FireProofLeatherVest scarletLeatherVestOfFireResistance = new FireProofLeatherVest(100, 15, 6);
		//above, below
		ProtectionStack knightProtectionSt = new ProtectionStack(scarletChestpieceOfTheBoar,scarletLeatherVestOfFireResistance);
		//100 HP
		GameCharacter c1 = new GameCharacter("Lancelot",100,10,knightProtectionSt);
		c1.startQuest(q1);

		System.out.println("\nCharacter state BEFORE damage:");
		System.out.println(c1.toString());

		//phy=50,mag=5,elec=0,fire=100
		Damage dragonDmg = new Damage(75,33,0,99);
		c1.wound(dragonDmg);

		System.out.println("\nCharacter state AFTER damage:");
		System.out.println(c1.toString());

		Damage longswordDmg = new Damage(200,0,0,0);
		c1.wound(longswordDmg);

		System.out.println("\nCharacter state after FATAL damage:");
		//HP will bet at 0 //you could add a test to display that character is dead
		System.out.println(c1.toString());

	}
}