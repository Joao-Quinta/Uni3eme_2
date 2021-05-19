package ch.unige.cui.rpg;
import java.util.*;

import ch.unige.cui.rpg.Item;
import ch.unige.cui.rpg.ItemInventory;
import ch.unige.cui.rpg.NullObject;

public class Inventory<T extends Item> {

    private final List<ItemInventory<? extends Item>> items = new ArrayList<>();
    
    /* // methode pour dfaire une copie profonde: on ne l utilise pas car ItemInventory est maintenant une classe immutable
    //elle est mise ici pour indication
    public List<ItemInventory<? extends Item>> showItems(){
        List<ItemInventory<? extends Item>> itemsCopy = new ArrayList<>();
        for(ItemInventory ii: items){
            ItemInventory iiCopy = new ItemInventory(ii.getID(),ii.getT(),ii.getAmmount());
            itemsCopy.add(iiCopy);
        }
        return itemsCopy;
    }
    */

    //une copie "au premier niveau" est suffisante car ItemsInv est immutable: la methode proposee pour ce TP
    public List<ItemInventory<? extends Item>> showItems(){
        List<ItemInventory<? extends Item>> itemsCopy = new ArrayList<>();
		itemsCopy.addAll(items);
        return itemsCopy;
    }

    /* //une methode avec les streams
    public List<ItemInventory<? extends Item>> showItems(){
        return items.stream()
			.map( ItemInventory::copy )
			.collect( Collectors.toList() );
    }
    */
    
    public int getTotal(){
        int total = 0;
        for(ItemInventory<? extends Item> item : items){
            total += item.getPrice()*item.getAmmount();
        }
        return total;
    }

    public ItemInventory getItemInventoryByID(int ID){        
        for(int i=0;i<items.size();i++){
            if(items.get(i).getID() == ID){
                //on peut maintenant se permettre de renvoyer directement l item puisque classe immutable
                return items.get(i);
            }
        }
        
        throw new IllegalArgumentException("ID does not exist.");
    }

    
    public void addItemInventoryToInv(ItemInventory<? extends Item> it ){
        for(int i=0;i<items.size();i++){
            if(items.get(i).equals(it)){
                items.set(i, items.get(i).incAmmount(it.getAmmount()));//= incremente le nb d item du nombre souhaite (argument)
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
    
    
    public void removeAllFromInv(List<ItemInventory<? extends Item>> that){ // List<ItemInventory<? extends Item>> that){
        for(ItemInventory e: that){
            this.removeItemInventoryFromInv(e);
        }
    }
    
    public void addAllToInv( List<ItemInventory<? extends Item>> that){//List<ItemInventory<? extends Item>> that){
        for(ItemInventory e: that){
            this.addItemInventoryToInv(e);
        }
    }

    @Override
    public String toString() {
        return "Inventory [items=" + items + "]";
    }
    
}
