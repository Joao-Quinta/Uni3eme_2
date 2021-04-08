import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

import ch.unige.cui.rpg.*;


public class Game{
	public static void main(String[] args){

		Quest q1 = new Quest("Holy grail quest",1000000);
		
		/**/
		Map<String, String> lines = new HashMap<String, String>();
		try {
		      File myObj = new File("C:\\Users\\qjoao\\Documents\\GitHub\\Uni3eme_2\\cloo\\tp4_withGradle\\src\\main\\java\\doc.txt");
		      Scanner myReader = new Scanner(myObj);
		      while (myReader.hasNextLine()) {
		        String data = myReader.nextLine();
		        String[] parts = data.split(":");
		        lines.put(parts[0], parts[1]);
		      }
		      myReader.close();
		    } catch (FileNotFoundException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }
		
		System.out.println(lines);
		Set<String> keyLines = lines.keySet();
		ProtectionStack knightProtectionSt = null;
		if (keyLines.contains("knightProtectionSt")) {	
			//on vient la 
			ChainMail layerAbove = null;
			FireProofLeatherVest layerBelow = null;
			
			
			if (keyLines.contains("layerAbove")) {
				//on vient la
				String typeLayerAbove = lines.get("layerAboveT");
				System.out.println(typeLayerAbove);
				
				String valueLayerAbove = lines.get("layerAbove");
				if (typeLayerAbove == typeLayerAbove) {
					String[] valuesParts = valueLayerAbove.split(",");
					System.out.println("\n asd");
					layerAbove  = new ChainMail(Integer.parseInt(valuesParts[0]),Integer.parseInt(valuesParts[1]));
					

				}
			}	
			if (keyLines.contains("layerBelow")) {
				String typeLayerBelow = lines.get("layerBelowT");
				String valueLayerBelow = lines.get("layerBelow");
				if (typeLayerBelow == typeLayerBelow) {
					String[] valuesParts = valueLayerBelow.split(",");
					System.out.println("\n asd111111");
					layerBelow  = new FireProofLeatherVest(Integer.parseInt(valuesParts[0]),Integer.parseInt(valuesParts[1]),Integer.parseInt(valuesParts[2]));		

				}
			}
			
				
			knightProtectionSt = new ProtectionStack(layerAbove, layerBelow);
			
			
			
		}
		String valueChar = lines.get("character");
		String[] valuesParts = valueChar.split(",");
		GameCharacter c1 = new GameCharacter(valuesParts[0],Integer.parseInt(valuesParts[1]),Integer.parseInt(valuesParts[2]),knightProtectionSt);
		
		
		
		/*
		//armorVal=75,weight=27 [kg?]
		ChainMail scarletChestpieceOfTheBoar = new ChainMail(55,27);
		//fire prot=100, phys prot=26, weight=6
		FireProofLeatherVest scarletLeatherVestOfFireResistance = new FireProofLeatherVest(100, 15, 6);
		//above, below
		ProtectionStack knightProtectionSt = new ProtectionStack(scarletChestpieceOfTheBoar,scarletLeatherVestOfFireResistance);
		//100 HP
		GameCharacter c1 = new GameCharacter("Lancelot",100,10,knightProtectionSt);
		*/
		
		
		c1.startQuest(q1);

		System.out.println("\nCharacter state BEFORE damage:");
		System.out.println(c1.toString());

		//phy=50,mag=5,elec=0,fire=100
		Damage dragonDmg = new Damage(75,33,0,99);
		c1.wound(dragonDmg);

		System.out.println("\nCharacter state AFTER damage:");
		System.out.println(c1.toString());

		Damage longswordDmg = new Damage(200,0,0,0);
		c1.wound(longswordDmg);

		System.out.println("\nCharacter state after FATAL damage:");
		//HP will bet at 0 //you could add a test to display that character is dead
		System.out.println(c1.toString());
		

	}
}