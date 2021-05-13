package ch.unige.cui.rpg;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.io.*;
import java.lang.Math; 
import java.lang.reflect.*;


public class LootGenerator implements RandomGenerator<Item> {

    private final String filename;
    private ArrayList<String> lines = new ArrayList<>();

    public LootGenerator(String filename){
        this.filename=filename;
        //read lfile in lines private var
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

    public Item single(Random rng){
        int line = rng.nextInt(6 - 1);
        //System.out.println(">>>>>>>>>>>> rnd line="+lines.get(line)+"<<<<<<<<<<<<<<<<");
        List<String> parsedLine = Arrays.asList(lines.get(line).split(","));

        String classVal = parsedLine.get(0);
        String nameVal = parsedLine.get(1);
        int minVal = Integer.parseInt(parsedLine.get(2));
        int maxVal = Integer.parseInt(parsedLine.get(3));
        int minLvlVal = Integer.parseInt(parsedLine.get(4));
        
        int propertyVal = rng.nextInt(maxVal - minVal) + minVal;
        int weightVal = (int) Math.ceil((double) propertyVal/5.0);
        
        try{
            Class cl = Class.forName("ch.unige.cui.rpg."+classVal);
            Constructor cons = cl.getConstructor(String.class, int.class, int.class, int.class );
            return  (Item) cons.newInstance(nameVal, propertyVal, weightVal, minLvlVal);
        }
        catch(Exception e){
            System.out.println("Exception occured.");
            return new NullObject();
        }
        
        
    }

}