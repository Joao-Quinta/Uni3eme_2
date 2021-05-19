package ch.unige.cui.rpg;
import java.util.*;

public interface Buyer<T>  { 
    //retourne la valeur d'achat
    int buy( Inventory<? extends Item> goods );
  }
  