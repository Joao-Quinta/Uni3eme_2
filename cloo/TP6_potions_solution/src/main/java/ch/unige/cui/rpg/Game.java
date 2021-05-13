package ch.unige.cui.rpg;

import java.util.Random;
import java.io.File;

public class Game {

    public static void main(String[] args){
        
        System.out.println("Solution avec introspection");

        Random rng = new Random(System.currentTimeMillis());
        String fn = "src/main/resources/potions.txt";
        File file = new File(fn);
        String absolutePath = file.getAbsolutePath();
        
        System.out.println(absolutePath);

        LootGenerator lg = new LootGenerator(absolutePath);

        var x = lg.single(rng);
        var y = lg.single(rng);

        System.out.println(x.toString());
        System.out.println(y.toString());
    }
}