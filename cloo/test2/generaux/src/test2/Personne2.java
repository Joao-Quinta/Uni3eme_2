package test2;

public class Personne2 {
	private String name;
	private int age;
	
	public Personne2(String name, int age) {
		this.age = age;
		this.name = name;
	}
	
	public String toString() {
		return "name : " + this.name + " age : " + String.valueOf(this.age);
	}

}
