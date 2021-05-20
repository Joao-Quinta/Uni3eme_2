package ch.unige.cui.rpg;
import java.util.*;

import ch.unige.cui.rpg.Item;
import ch.unige.cui.rpg.ItemInventory;
import ch.unige.cui.rpg.NullObject;

public class Inventory<T extends Item> {

    private List<ItemInventory<? extends Item>> items = new ArrayList<>();

    public Inventory(){}
    
    public List<ItemInventory<? extends Item>> showItems(){
        //List<ItemInventory<...>> itemsClone = new ArrayList<>(items.size());
        //Collections.copy(itemsClone, items);
        List<ItemInventory<? extends Item>> itemsClone = List.copyOf(items);
        return itemsClone;
    }

    public int getTotal(){
        int total = 0;
        for(ItemInventory<? extends Item> item : items){
            total += item.getPrice()*item.getAmmount();
        }
        return total;
    }

    public ItemInventory getItemInventoryByID(int ID){
        for(ItemInventory it: items){
            if(it.getID() == ID){
                return it;
            }
        }
        throw new IllegalArgumentException("ID does not exist.");
    }

    
    public void addItemInventoryToInv(ItemInventory<? extends Item> it ){
        for(ItemInventory i: items){
            if(it.equals(i)){//i.getID() == it.getID()){
                //si ID trouve: incrementer amount
                i.incAmmount(it.getAmmount());
                return;
            }
        }
        //si pas d itemInv avec cet ID trouve: on en cree un
        items.add(it);
    }
    

    public void removeItemInventoryFromInv(ItemInventory<? extends Item> it ){
        for(int i=0;i<items.size();i++){
            if(items.get(i).equals(it)){
                items.set(i, items.get(i).decAmmount(it.getAmmount()));
                if(items.get(i).getAmmount() <= 0){
                    items.remove(i);
                }
            }
        }
    }
    
    
    public void removeAllFromInv(List<ItemInventory<? extends Item>> that){ 

        for(ItemInventory e: that){
            this.removeItemInventoryFromInv(e);
        }
    }
    
    public void addAllToInv( List<ItemInventory<? extends Item>> that){
        for(ItemInventory e: that){
            this.addItemInventoryToInv(e);
        }
    }

    @Override
    public String toString() {
        return "Inventory [items=" + items + "]";
    }
    
}
