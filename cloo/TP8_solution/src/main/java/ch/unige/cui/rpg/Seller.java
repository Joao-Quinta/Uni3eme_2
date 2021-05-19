package ch.unige.cui.rpg;
import java.util.*;

public interface Seller<T> { 
    //retourne vrai si la vente se conclu
    boolean sell( Inventory<? extends Item> goods, int offeredAmount  );
    //Retourne les objets dispos
    Inventory<? extends Item> showInventory();
  }
  