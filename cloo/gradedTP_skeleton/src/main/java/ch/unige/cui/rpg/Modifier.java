package ch.unige.cui.rpg;

public interface Modifier {
	public boolean preCondition(GameChar player);
	public PossibleTarget target();
	public void applyModification(GameChar player, GameChar target);
	public RessourceType getTypePre();
	public RessourceType getTypePost();
	public boolean requiresTarget();
}
