import ch.unige.cui.rpg.Character;
import ch.unige.cui.rpg.Quest;

public class Game{
	public static void main(String[] args){
		Character c1 = new Character("Lancelot",100,0);
		Quest q1 = new Quest("Holy grail quest",1000000);
		c1.startQuest(q1);
		
		System.out.println(c1.toString());
		System.out.println(q1.toString());
	}
}