package ch.unige.cui.rpg;

public class MageRobes implements Protection {
	private final Damage protectionValues;
	private final int weight;


    public int getWeight() {
        return weight;
    }

    public MageRobes(int magicalProt, int weight){
    	protectionValues = new Damage(0,magicalProt,0,0);
    	this.weight = weight;
    	
    }

    public Damage absorb(Damage dmg) {
        //chain mail only absorbs magical damage
        return new Damage(dmg.getPhysical(), 
                    dmg.getMagical()-protectionValues.getMagical(), 
                    dmg.getElectrical(),
                    dmg.getFire());
    }

    public Damage getMageRobesProt() {
        return protectionValues;
    }

}
