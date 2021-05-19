package ch.unige.cui.rpg;
import java.util.*;


public class ItemInventory<T extends Item > {

    private final int ID;//un item inv est unique: chaque item (e.g. une potion ) est "encapsule" dans un ItemInventory
    private T t;
    private int ammount;
    private int price;

    public ItemInventory(int ID, T t, int ammount){
      this.ID=ID;
      this.t = t;
      this.ammount = ammount;
      price = t.getPrice();//price of a single item
    }

    public void incAmmount(int val){
      ammount += val;
    }

    public void decAmmount(int val){
      ammount -= val;
    }

    public T getT() {
      return t;
    }
  
    public int getAmmount() {
      return ammount;
    }

    public void setAmmount(int ammount){
      this.ammount=ammount;
    }
  
    public int getPrice() {
      return price;
    }

    public int getID(){
      return ID;
    }
  
    @Override
    public String toString() {
      return "ItemInventory [ammount=" + ammount + ", price=" + price + ", t=" + t + "]";
    }

    // h code et eq: seuleement w.r.t. champ ID

    @Override
    public int hashCode() {
      final int prime = 31;
      int result = 1;
      result = prime * result + ID;
      return result;
    }
  
    @Override
    public boolean equals(Object obj) {
      if (this == obj)
        return true;
      if (obj == null)
        return false;
      if (getClass() != obj.getClass())
        return false;
      ItemInventory other = (ItemInventory) obj;
      if (ID != other.ID)
        return false;
      return true;
    }
 
  }
  