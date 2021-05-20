import java.util.ArrayList;
import java.util.Iterator;

import test2.*;

public class App {
    @SuppressWarnings("static-access")
	public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        Personne t = new Personne("not", 23);
        Codeur t1 = new Codeur("joao", 23, 3);
        Personne2 t2 = new Personne2("joaaaaaao", 22);
        //System.out.println(t.toString());
        //System.out.println(t1.toString());
        
        // personne
        ArrayList<Personne> listePersonne = new ArrayList<Personne>();
        listePersonne.add(t);
        //listePersonne.add(t1);
        TestGenerique<Personne> instanceTwice = new TestGenerique<Personne>();
        instanceTwice.twice(listePersonne);
         
        System.out.println("\npersonne ");
        Iterator<Personne> it = listePersonne.iterator();
        while(it.hasNext()) {
        	System.out.println(it.next().toString());
        }
        
        
        //codeur
        ArrayList<Codeur> listePersonne1 = new ArrayList<Codeur>();
        listePersonne1.add(t1);
        //listePersonne.add(t1);
        TestGenerique<Codeur> instanceTwice1 = new TestGenerique<Codeur>();
        instanceTwice1.twice(listePersonne1);
        
        System.out.println("\n codeur ");
        Iterator<Codeur> it1 = listePersonne1.iterator();
        while(it1.hasNext()) {
        	System.out.println(it1.next().toString());
        }
        
        //personne 2
        /*
        ArrayList<Personne2> listePersonne2 = new ArrayList<Personne2>();
        listePersonne2.add(t2);
        //listePersonne.add(t1);
        TestGenerique<Personne2> instanceTwice2 = new TestGenerique<Personne2>();
        instanceTwice2.twice(listePersonne2);
        
        System.out.println("\n personne 2 ");
        Iterator<Personne2> it2 = listePersonne2.iterator();
        while(it2.hasNext()) {
        	System.out.println(it2.next().toString());
        }*/
        
        
    }
}
