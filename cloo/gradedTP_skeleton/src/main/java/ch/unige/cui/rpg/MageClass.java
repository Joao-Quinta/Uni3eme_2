package ch.unige.cui.rpg;

public class MageClass extends GameCharacter implements CharClass{
    
    public MageClass(String name,
                int maxHP,
                int gold,
                ProtectionStack protectionSt,
                CharProfile pr
                ) {
        super(name,maxHP,gold,protectionSt,pr);
    }
    
    public CharProfile levelUp(CharProfile pr){
    	LevelClass levelRules = new LevelClass();
    	int lvl = pr.getLvl();
    	int stamToAdd = 0;
    	int intelToAdd = 3;
    	if (lvl%2 == 1 ) {// on va entrer en niveau impaire
    		stamToAdd = 1;
    	}
    	//(int intellect, int strength, int stamina, int xp, int lvl)
    	return new CharProfile(pr.getIntellect()+intelToAdd, 
    			pr.getStrength(),
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