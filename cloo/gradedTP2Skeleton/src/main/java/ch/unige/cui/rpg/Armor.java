package ch.unige.cui.rpg;

public class Armor{
    private final int MAX_ARMOR_VAL = 100;
    private int armorVal;
    private DmgType armorType;

    public Armor(int armorVal, DmgType armorType){
        if(armorVal<=MAX_ARMOR_VAL){
            this.armorVal=armorVal;
            this.armorType = armorType;
        }else {
        	throw new IllegalArgumentException("Illegal armorVal. Max possible armor value: 100.");
        }
    }

    public int getArmorVal(){
        return armorVal;
    }

    public DmgType getArmorType(){
        return armorType;
    }


    public Damage absorb(Damage dmg){
    	if(armorType == DmgType.MAGICAL) {
    		//cas magique
    		float pourCent = (float) getArmorVal()/100;
    		float pourCentM1 = (float) 1 - pourCent;
    		float newDmg = dmg.getMagical()*pourCentM1;
    		int newDmgInt = (int) newDmg;
    		return new Damage(dmg.getPhysical(), newDmgInt); 		
    	}else {
    		// cas phyisque 
    		//System.out.println("in physical case");
    		//System.out.println("armor val : " + getArmorVal());
    		//System.out.println("armor sur 100 : " + (float) getArmorVal()/100);
    		float pourCent = (float) getArmorVal()/100;
    		float pourCentM1 = (float) 1 - pourCent;
    		float newDmg = dmg.getPhysical()*pourCentM1;
    		int newDmgInt = (int) newDmg;
    		return new Damage(newDmgInt, dmg.getMagical()); 
    		
    	}
    }
}