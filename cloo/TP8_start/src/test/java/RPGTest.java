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




}
