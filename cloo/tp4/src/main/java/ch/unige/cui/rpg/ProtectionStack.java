package main.java.ch.unige.cui.rpg;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;


@SuppressWarnings("unused")
public class ProtectionStack implements Protection{
	
	// ProtectionStack est une entité, car avec le temps elle peut évoluer, on peut équiper des pièces (eventuellement en déséquiper), ces attributs ne sont donc pas définissants
	
	private boolean belowLayer;
	private boolean aboveLayer;
	private int totalArmorWeight;
	private Damage damageDeffence;
	
	public ProtectionStack() {
		this.belowLayer = false;
		this.aboveLayer = false;
		this.totalArmorWeight = 0;
		this.damageDeffence = new Damage();
	}
	
	public boolean addPiece(Damage deffence, int weight, String layer) {
	
		if (layer == "below") {
			if (this.belowLayer) {
				return false;
			} else {
				this.belowLayer = true;		
			}
		}
		
		if (layer == "above") {
			if (this.aboveLayer) {
				return false;
			} else {
				this.aboveLayer = true;		
			}
		}
		
		this.totalArmorWeight += weight;
		
		ArrayList<String> armorType = new ArrayList<String>();
		ArrayList<Integer> armorAmount = new ArrayList<Integer>();
		
		// la vieille qu on avait deja
		Map<String, String> currentArmor = damageDeffence.getTypesDmge();
		if (currentArmor != null) {
			Set<String> armorTypes = currentArmor.keySet();
			
			for (Iterator<String> it = armorTypes.iterator(); it.hasNext();) {
				String type = it.next();
				int val = Integer.valueOf(currentArmor.get(type));
				armorType.add(type);
				armorAmount.add(val);			
		    }
		}
		
		// celle qu on ajoute
		Map<String, String> armorToAdd = deffence.getTypesDmge();
		Set<String> armorTypesToAdd = armorToAdd.keySet();
		
		for (Iterator<String> it = armorTypesToAdd.iterator(); it.hasNext();) {
			String type = it.next();
			int val = Integer.valueOf(armorToAdd.get(type));
			if(armorType.contains(type)) {
				int index = armorType.indexOf(type);
				armorAmount.set(index, armorAmount.get(index) + val);
			}else {
				armorType.add(type);
				armorAmount.add(val);
			}		
	    }
		
		this.damageDeffence = new Damage(armorType, armorAmount);
		return true;
	}

	@Override
	public int weight() {
		return this.totalArmorWeight;
	}

	@Override
	public Damage absorb(Damage dmg) {
		int totalDamage = 0;
		Map<String, String> incomingDmg = dmg.getTypesDmge();
		Map<String, String> currentArmor = this.damageDeffence.getTypesDmge();
		Set<String> atackTypes = incomingDmg.keySet();
		
		for (Iterator<String> it = atackTypes.iterator(); it.hasNext();) {
			String type = it.next();
			int val = Integer.valueOf(incomingDmg.get(type));
			if (currentArmor.containsKey(type)) {
				val = val - Integer.valueOf(currentArmor.get(type));
			}
			totalDamage += val;		    
		}
		ArrayList<String> damageType = new ArrayList<String>();
		damageType.add("damage");
		ArrayList<Integer> damageAmount = new ArrayList<Integer>();
		damageAmount.add(totalDamage);
		return new Damage(damageType, damageAmount);
	}
	
	public Damage getDamage() {
		
		return damageDeffence;
	}
	
}