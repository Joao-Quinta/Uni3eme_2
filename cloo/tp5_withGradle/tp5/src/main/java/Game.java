import ch.unige.cui.rpg.*;


public class Game {
	public static void main(String[] args){
		GameCharacter c1 = new GameCharacter("moonSlave", 100, 100);
	    Quest q1 = new Quest("faire la paix", 100000);
	    String toStringPreQuest = c1.toString();
	    
	    System.out.println(toStringPreQuest);
	    
	    c1.startQuest(q1);
	    
	    String toStringPostQuest = c1.toString();
	    
	    System.out.println(toStringPostQuest);
	    
	}
	
    

}
