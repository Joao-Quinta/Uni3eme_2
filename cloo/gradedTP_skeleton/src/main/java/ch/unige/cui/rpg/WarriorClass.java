package ch.unige.cui.rpg;

public class WarriorClass extends GameCharacter implements CharClass {

    public WarriorClass(String name,
                int maxHP, 
                int gold, 
                ProtectionStack protectionSt,
                CharProfile pr
                ){
                super(name,maxHP,gold,protectionSt,pr);
    }

    public CharProfile levelUp(CharProfile pr){
    	LevelClass levelRules = new LevelClass();
    	int lvl = pr.getLvl();
    	int stamToAdd = 2;
    	int strengthToAdd = 1;
    	//(int intellect, int strength, int stamina, int xp, int lvl)
    	return new CharProfile(pr.getIntellect(), 
    			pr.getStrength()+strengthToAdd,
    			pr.getStamina()+stamToAdd,
    			0,
    			lvl+1);
    }


    @Override
    public int completeQuest(Quest q) {
        int questXp = super.completeQuest(q);
        LevelClass levelRules = new LevelClass();
        CharProfile currentPr = super.getPr();        
        if (currentPr.getLvl() < levelRules.getMaxLvl()) {
        	int currentXP = currentPr.getXp() + questXp;
        	int requiredXP = levelRules.getXPToNextLvl(currentPr.getLvl());
        	if (currentXP >= requiredXP) {
        		super.setPr(this.levelUp(currentPr));        		
        	}else {
        		super.setPr(new CharProfile(currentPr.getIntellect(),
        				currentPr.getStrength(),
        				currentPr.getStamina(),
        				currentXP,
        				currentPr.getLvl()));
        	}
        }
        return questXp;
    }


}
