package ch.unige.cui.rpg;

public class ProtectionStack extends Protection{
	
	public ProtectionStack(Protection layerAbove,Protection layerbelow) {
		super(layerAbove.getWeigth() + layerbelow.getWeigth(), 
				layerAbove.getPhysicalProt() + layerbelow.getPhysicalProt(), 
				layerAbove.getMagicalProt() + layerbelow.getMagicalProt(),
				layerAbove.getElectricalProt() + layerbelow.getElectricalProt(),
				layerAbove.getFireProt() + layerbelow.getFireProt());
	}


}
