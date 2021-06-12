package ch.unige.cui.rpg;

public class Ressource {
	private int maxVal;
	private int val;
	private RessourceType type;
	
	public Ressource(int start, int max, RessourceType type) {
		this.setMaxVal(max);
		this.setVal(start);
		this.type = type;
	}

	public int getVal() {
		return val;
	}

	public void setVal(int val) {
		this.val = val;
	}

	public int getMaxVal() {
		return maxVal;
	}

	public void setMaxVal(int maxVal) {
		this.maxVal = maxVal;
	}
	
}
