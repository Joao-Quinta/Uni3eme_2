package test2;

public class Codeur extends Personne{
	private int exp;

	public Codeur(String name, int age, int xp) {
		super(name, age);
		this.exp = xp;
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public String toString() {
		return super.toString() + " exp : " + String.valueOf(this.exp);
	}
	
}
