package ch.unige.cui.rpg;

public class Potion implements Modifier{
	private int modify;
	private RessourceType typePre;
	private RessourceType typePost;
	
	
	public Potion(int val, RessourceType type) {
		this.modify = val;
		this.typePre = type;
		this.typePost = type;
	}
	
	public int getModify() {
		return this.modify;
	}

	@Override
	public boolean preCondition(GameChar player) {
		if (player.health.getVal() > 0) {// la precondition pour boire une potion, c'est qu on soit en vie
			return true;
		}
		return false;
	}

	@Override
	public void applyModification(GameChar player, GameChar target) {
		switch(this.typePost) {
		
		case HEALTH:
			if(player.hasHealth()) {
				Ressource health = player.health;
				health.setVal(Math.min(health.getVal() + modify, health.getMaxVal()));
			}
			
		case MANA:
			if(player.hasMana()) {
				Ressource mana = player.getMana();
				mana.setVal(Math.min(mana.getVal() + modify, mana.getMaxVal()));
			}
			
		default:
		}
	}

	@Override
	public RessourceType getTypePre() {
		return typePre;
	}


	@Override
	public PossibleTarget target() {
		return PossibleTarget.PLAYER;
	}

	@Override
	public RessourceType getTypePost() {
		return typePost;
	}

	@Override
	public boolean requiresTarget() {
		return false;
	}

}
