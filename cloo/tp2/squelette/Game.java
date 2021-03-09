import ch.unige.cui.rpg.Character;
import ch.unige.cui.rpg.Quest;

public class Game{
	public static void main(String[] args){
		Character druidEqui = new Character("druid Equi", 100, 100);
		Character druidTank = new Character("druid Tank", 300, 1000);
		Character druidHeal = new Character("druid Heal", 90, 50);
		
		Quest gloireALaHorde = new Quest("Tuer Denathrius !", 1000);
		
		druidEqui.startQuest(gloireALaHorde);
		druidTank.startQuest(gloireALaHorde);
		druidHeal.startQuest(gloireALaHorde);
		
		String druidEquiP = druidEqui.toString();
		String druidTankP = druidTank.toString();
		String druidHealP = druidHeal.toString();
		
		System.out.println(druidEquiP);
		System.out.println(druidTankP);
		System.out.println(druidHealP);
		
		
	}
}