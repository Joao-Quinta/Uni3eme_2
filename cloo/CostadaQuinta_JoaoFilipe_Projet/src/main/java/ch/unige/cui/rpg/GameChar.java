package ch.unige.cui.rpg;

public abstract class GameChar {
	protected String name;
	protected Ressource health;
	private GameChar target = null;
	
	
	public GameChar(String name, int max) {
		this.name = name;
		this.health = new Ressource(max, max, RessourceType.HEALTH);
	}
	
	public <T extends Modifier> boolean cast(T m) {
		if(canCast(m.requiresTarget()) && m.preCondition(this)) {
			m.applyModification(this, this.target);
			return true;
		}
		return false;		
	}

	
	public boolean canCast(boolean require) {
		if (require && this.hasTarget()) {
			return true;
		}
		else if(! require) {
			return true;
		}else {
			return false;
		}
	}
	
	public boolean hasTarget() {
		if(target == null) {
			return false;
		}else {
			return true;
		}
	}
	
	public void setTarget(GameChar tar) {
		this.target = tar;
	}
	
	public void loseTarget() {
		this.target = null;
	}
	
	public boolean hasHealth() {
		return true;
	}
	public boolean hasMana() {
		return false;
	}
	public boolean hasRage() {
		return false;
	}
	
	protected Ressource getMana() {
		return null;
	}
	
	protected Ressource getRage() {
		return null;
	}
}
