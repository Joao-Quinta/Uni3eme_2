package ch.unige.cui.rpg;
import java.util.ArrayList;
import ch.unige.cui.rpg.DmgType;

public class Game{
	public static void main(String[] args){
		System.out.println("Successfully entered in main.");
		
		Armor t = new Armor(50, DmgType.PHYSICAL);
		Damage dmg = new Damage(100, 100);
		Damage test = t.absorb(dmg);
		//System.out.println(test.getMagical()+test.getPhysical());
		
		Player p1 = new Player("Smeagol",50,  new Armor(11, DmgType.PHYSICAL), new CharProfile(1,5,5),PlayerClass.WARRIOR);
        Player p2 = new Player("Gandalf",100, new Armor(55,DmgType.MAGICAL), new CharProfile(10, 2, 3), PlayerClass.MAGE);
        Player p3 = new Player("Sauron",5000,  new Armor(99, DmgType.PHYSICAL), new CharProfile(105,25,10),PlayerClass.MAGE);
		
        
	}
}