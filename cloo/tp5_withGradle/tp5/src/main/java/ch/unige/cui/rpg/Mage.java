package ch.unige.cui.rpg;

public class Mage extends GameCharacter{
	
	private int manaPoints;

	public Mage(String nom, int hpMax, int armor, int mana) {
		super(nom, hpMax, armor);
		this.manaPoints = mana;
	}
	
	public void equipProtection(Cloth piece) {
		if (!(this.getAbove()) && !(this.getBelow())) {
			this.setMyArmorPieces(new ProtectionStack(piece, new Protection(0,0,0,0,0)));
			this.setBelow(true);
		}
		if (!(this.getAbove())) {
			this.setMyArmorPieces(new ProtectionStack(piece, this.getMyArmorPieces()));
			this.setAbove(true);
		}
		if (this.getAbove() && this.getBelow()) {
			System.out.println("above and below equiped");
		}
	}
	
	

}
