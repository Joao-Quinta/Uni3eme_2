package ch.unige.cui.rpg;

public class Protection extends Equipment{
	private int physicalProt;
	private int magicalProt;
	private int electricalProt;
	private int fireProt;

	public Protection(int weight, int physicalProt, int magicalProt, int electricalProt, int fireProt) {
		super(weight);
		this.physicalProt = physicalProt;
		this.magicalProt = magicalProt;
		this.electricalProt = electricalProt;
		this.fireProt = fireProt;
	}
	
	public Damage absorb(Damage dmg) {
		int resPhysicalDmg = Math.max(0, this.physicalProt - dmg.getPhysicalDmg());
		int resMagicalDmg = Math.max(0, this.magicalProt - dmg.getMagicalDmg());
		int resElectricalDmg = Math.max(0, this.electricalProt - dmg.getElectricalDmg());
		int resFireDmg = Math.max(0, this.fireProt - dmg.getFireDmg());
		return new Damage(resPhysicalDmg, resMagicalDmg, resElectricalDmg, resFireDmg);
	}
	
	public int getPhysicalProt(){
		return this.physicalProt;
	}
	
	public int getMagicalProt(){
		return this.magicalProt;
	}
	
	public int getElectricalProt(){
		return this.electricalProt;
	}
	
	public int getFireProt(){
		return this.fireProt;
	}
	
	

}
