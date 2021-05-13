package ch.unige.cui.rpg;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Random;

public class Game{
	public static void main(String[] args) throws FileNotFoundException, IOException{
		System.out.println("Successfully entered in main.");
		Random rng = new Random(System.currentTimeMillis());
		String fn = "src/main/resources/potions.txt";
        File file = new File(fn);
        String absolutePath = file.getAbsolutePath();
        
        System.out.println(absolutePath);

        RandomItem lg = new RandomItem(absolutePath);
        
        var x = lg.single(rng);
        System.out.println(x.toString());
        var x1 = lg.single(rng);
        System.out.println(x1.toString());
        var x2 = lg.single(rng);
        System.out.println(x2.toString());
        var x3 = lg.single(rng);
        System.out.println(x3.toString());
        var x4 = lg.single(rng);
        System.out.println(x4.toString());
        var x5 = lg.single(rng);
        System.out.println(x5.toString());
        //var y = lg.single(rng);
	}
}