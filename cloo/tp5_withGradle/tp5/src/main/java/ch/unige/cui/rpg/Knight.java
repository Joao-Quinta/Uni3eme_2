package ch.unige.cui.rpg;


public class Knight extends GameCharacter{

	public Knight(String nom, int hpMax, int armor) {
		super(nom, hpMax, armor);
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
	
	public void equipProtection(ChainMail piece) {
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
	
	public void equipProtection(LeatherVest piece) {
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