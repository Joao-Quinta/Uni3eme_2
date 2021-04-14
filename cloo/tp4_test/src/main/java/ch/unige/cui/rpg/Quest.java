package ch.unige.cui.rpg;

public class Quest{
	private final String description;
	private final int reward;
	
	public Quest(String description, int reward){
		this.description=description;
		this.reward=reward;
	}
	
	public String toString(){
		return "Description="+description+"reward="+reward;
	}
	
}