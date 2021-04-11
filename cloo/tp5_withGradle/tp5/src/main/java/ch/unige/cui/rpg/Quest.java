package ch.unige.cui.rpg;

public class Quest{
	private String description;
	private int reward;
	
	public Quest(String description, int reward) {
		this.description = description;
		this.reward = reward;
	}
	
	public String getDescription() {
		return description;
	}
	
	public int getReward() {
		return reward;
	}
}
