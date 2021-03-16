package ch.unige.cui.rpg;

import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;



public class Damage {
	private Map<String, String> typesDmg;
	
	public Damage(ArrayList<String> typesDmg, ArrayList<Integer> values) {
		this.typesDmg = new HashMap<String, String>();
		for(int i = 0; i < typesDmg.size(); i++) {
			this.typesDmg.put(typesDmg.get(i), String.valueOf(values.get(i)));
		}
	}

	public Damage() {
		
	}

	public Map<String, String> getTypesDmge() {
		return typesDmg;
	}
}
