import ch.unige.cui.rpg.*;
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Random;
import java.io.File;
import java.util.concurrent.TimeUnit;

public class RPGTest {
    private Random rng = new Random(System.currentTimeMillis());
    
    @BeforeAll
    static void setUpAll(){
        System.out.println("BeforeAll test");
    }

    @BeforeEach
    void setUp(){
        System.out.println("BeforeEach test");
    }

    @AfterEach
    void tearDown(){
        System.out.println("AfterEach test");
    }

    @AfterAll
    static void tearDownAll(){
        System.out.println("AfterALl test");
    }

    

    @Test
    public void testPotion() {

        int nbIter = 100;

        String fn = "src/main/resources/potions.txt";
        File file = new File(fn);
        String absolutePath = file.getAbsolutePath();
        LootGenerator lg = new LootGenerator(absolutePath);

        var b = true;
        var x = lg.single(rng);
        for(int i=0;i<nbIter;i++){
            while( ! x.getName().equals("Lesser Healing Potion")){
                x = lg.single(rng);
                //System.out.println("inwhile:"+x.toString());
            }
            System.out.println(">>>>>>>>> debug test: "+((HealingPotion) x).getName()+" with HP="+((HealingPotion) x).getHP());
            
            b = b &&  (((HealingPotion) x).getHP() >=1 ) && (((HealingPotion) x).getHP() <= 10 );
            x = lg.single(rng);
        }
        
        assertEquals(b, true);
    }



}
