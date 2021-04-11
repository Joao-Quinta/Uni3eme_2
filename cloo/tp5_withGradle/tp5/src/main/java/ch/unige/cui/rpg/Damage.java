package ch.unige.cui.rpg;

public class Damage {
	private int physicalDmg;
	private int magicalDmg;
	private int electricalDmg;
	private int fireDmg;

	public Damage(int physicalDmg, int magicalDmg, int electricalDmg, int fireDmg) {
		this.physicalDmg = physicalDmg;
		this.magicalDmg = magicalDmg;
		this.electricalDmg = electricalDmg;
		this.fireDmg = fireDmg;
	}

	public int getPhysicalDmg() {
		return physicalDmg;
	}

	public int getMagicalDmg() {
		return magicalDmg;
	}

	public int getElectricalDmg() {
		return electricalDmg;
	}

	public int getFireDmg() {
		return fireDmg;
	}
}
