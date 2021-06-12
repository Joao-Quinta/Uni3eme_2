package ch.unige.cui.rpg;

public class Spell implements Modifier{
	private int pre;
	private int pos;
	private PossibleTarget target;
	private RessourceType typePre;
	private RessourceType typePost;
	private boolean requiresTarget;

	public Spell(int pre, int pos, PossibleTarget target, RessourceType typePre, RessourceType typePost, boolean requiresTarget) {
		this.pre = pre;
		this.pos = pos;
		this.target = target;
		this.typePre = typePre;
		this.typePost = typePost;
		this.requiresTarget = requiresTarget;
	}
	
	public int getPre() {
		return pre;
	}
	
	//vérifie que le jouer respecte les préconditions, et effectue les changements s'il les respect
	@Override
	public boolean preCondition(GameChar player) {
		
		switch(this.typePre) {
		
		// je vais expliquer le cas de figure pour HEALTH, les 2 autres cas marchent de la même façon 
		case HEALTH:
			if(player.hasHealth()) {// si le personnage dispose de la ressource HEALTH
				Ressource health = player.health;
				if(health.getVal() >= pre) { // alors on vérifie qu'il ait assez de HEALTH pour 'payer' le sort
					// s'il a assez de ressource, alors on calcule la nouvelle valeur pour la ressource HEALTH
					health.setVal(health.getVal() + pre); 
					return true;
				}
				return false;
			}
			return false;
			
		case MANA:// see HEALTH
			if(player.hasMana()) {
				Ressource mana = player.getMana();
				if(mana.getVal() >= pre) {
					mana.setVal(mana.getVal() + pre);
					return true;
				}
				return false;
			}
			return false;
			
		case RAGE:// see HEALTH
			if(player.hasRage()) {
				Ressource rage = player.getRage();
				if(rage.getVal() >= pre) {
					rage.setVal(rage.getVal() + pre);
					return true;
				}
				return false;
			}
			return false;
			
		default:
			return false;
		}
	}
	
	@Override
	public PossibleTarget target() {
		return target;
	}

	@Override
	public void applyModification(GameChar player, GameChar target) {
		GameChar toChange; 
		if(this.target == PossibleTarget.PLAYER) {
			toChange = player;
		}else {
			toChange = target;
		}
		switch(this.typePost) {
		case HEALTH:
			if(toChange.hasHealth()) {
				Ressource health = toChange.health;
				int newVal = health.getVal() + pos;
				if(newVal <= health.getMaxVal()) {
					if(newVal > 0) {
						health.setVal(newVal);
					}else {
						health.setVal(0);
					}
				}else {
					health.setVal(health.getMaxVal());
				}
			}
			
		case MANA:
			if(toChange.hasMana()) {
				Ressource mana = toChange.getMana();
				int newVal = mana.getVal() + pos;
				if(newVal <= mana.getMaxVal()) {
					if(newVal > 0) {
						mana.setVal(newVal);
					}else {
						mana.setVal(0);
					}
				}else {
					mana.setVal(mana.getMaxVal());
				}
			}
			
		case RAGE:
			if(toChange.hasRage()) {
				Ressource rage = toChange.getRage();
				int newVal = rage.getVal() + pos;
				if(newVal <= rage.getMaxVal()) {
					if(newVal > 0) {
						rage.setVal(newVal);
					}else {
						rage.setVal(0);
					}
				}else {
					rage.setVal(rage.getMaxVal());
				}				
			}
		default:
		}
	}

	@Override
	public RessourceType getTypePre() {
		return typePre;
	}

	@Override
	public RessourceType getTypePost() {
		return typePost;
	}

	@Override
	public boolean requiresTarget() {
		return this.requiresTarget;
	}


}
