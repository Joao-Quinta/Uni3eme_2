package main.java.ch.unige.cui.rpg;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.ArrayList;



public class Damage {
	// damage est un value objetct, car 2 pieces qui ont le meme type de déffence sont égales,et les protections ne peuvent pas évoluer avec le temps
	private Map<String, String> typesDmg;
	
	public Damage(ArrayList<String> typesDmg, ArrayList<Integer> values) {
		this.typesDmg = new HashMap<String, String>();
		for(int i = 0; i < typesDmg.size(); i++) {
			this.typesDmg.put(typesDmg.get(i), String.valueOf(values.get(i)));
		}
	}

	public Damage() {
		
	}
	
	public boolean equals(Object o) {
		if (o == this) return true;
		if (o == null) return false;
		if (! (o instanceof Damage)) return false;
		Damage dmg1 = (Damage) o;
		Map<String, String> dmg1That = dmg1.getTypesDmge();
		Map<String, String> dmgThis = this.getTypesDmge();
		
		Set<String> dmgKeysThat = dmg1That.keySet();
		Set<String> dmgKeysThis = dmgThis.keySet();
		
		if (dmgKeysThat.size() != dmgKeysThis.size()) return false;
		
		for (Iterator<String> it = dmgKeysThat.iterator(); it.hasNext();) {
			String type = it.next();
			if (dmgKeysThis.contains(type)) {
				if(Integer.valueOf(dmg1That.get(type)) != Integer.valueOf(dmgThis.get(type))) return false;
			} else return false;
			//int val = Integer.valueOf(currentArmor.get(type));	
	    }		
		return true;
	}
	
	public int hashCode() {
		int h = 0;
		Map<String, String> dmgThis = this.getTypesDmge();
		Set<String> dmgKeysThis = dmgThis.keySet();
		for (Iterator<String> it = dmgKeysThis.iterator(); it.hasNext();) {
			String type = it.next();
			h = h*31 + Double.hashCode(Integer.valueOf(dmgThis.get(type)));
		}
		return h;
	}

	public Map<String, String> getTypesDmge() {
		return typesDmg;
	}
}