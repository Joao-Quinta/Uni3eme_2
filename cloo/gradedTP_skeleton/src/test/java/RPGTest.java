import ch.unige.cui.rpg.*;
import jdk.jfr.Timestamp;

import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;
//@TestInstance(TestInstance.Lifecycle.PER_METHOD);

class RPGTest {


    @BeforeAll
    static void setUpAll(){
        System.out.println("BeforeAll test");
    }

    @BeforeEach
    void setUp(){
		//above, below
    	System.out.println("BeforeEach test");

    }

    @AfterEach
    void tearDown(){
        System.out.println("AfterEach test");
    }

    @AfterAll
    static void tearDownAll(){
        System.out.println("AfterAll test");
    }

}
