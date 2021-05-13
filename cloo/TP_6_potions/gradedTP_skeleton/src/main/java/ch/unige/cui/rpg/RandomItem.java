package ch.unige.cui.rpg;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Constructor;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class RandomItem implements RandomGenerator<Item>{
	private final String filename;
    private ArrayList<String> lines = new ArrayList<>();
	
	public RandomItem(String filename) throws FileNotFoundException, IOException {
		this.filename = filename;
		
		try( var in = new BufferedReader(new FileReader(filename))) {
            String ln = "";
            //int i = 1;
            while ((ln = in.readLine()) != null) {
                lines.add(ln);
                //System.out.println(i + ": " + ln );
                //i++;
        }
        } catch( IOException e ) {
            System.err.println("Couldn't read, because:");
            System.err.println(e.getMessage());
        }
	}

	@Override
	public Item single(Random rng) {
		int line = rng.nextInt(6 - 1);
		List<String> parsedLine = Arrays.asList(lines.get(line).split(","));
		String typeItem = parsedLine.get(0);
		String nameItem = parsedLine.get(1);
		int minVal = Integer.parseInt(parsedLine.get(2));
		int maxVal = Integer.parseInt(parsedLine.get(3));
		int niveauMin = Integer.parseInt(parsedLine.get(4));
		
		int val = rng.nextInt(maxVal - minVal) + minVal;
		int poids = (int) Math.ceil((double) val/5);
		
		try{
            Class cl = Class.forName("ch.unige.cui.rpg."+typeItem);
            Constructor cons = cl.getConstructor(String.class, int.class, int.class, int.class);
            return  (Item) cons.newInstance(nameItem, val, poids, niveauMin);
        }
        catch(Exception e){
            System.out.println("Exception occured.");
            return null;
        }
	}

}
