package ch.unige.cui.rpg;
import java.util.*;

public class PotionMerchant implements Merchant<Potion>{
        private final String name;//identifiant unique du marchand
        //inventaire du marchand
        private Inventory inv = new Inventory();
        private int gold;

        public String getName(){
            return name;
        }

        public int getGold() {
            return gold;
        }

        public PotionMerchant(String name, Inventory<? extends Item> inv, int initGoldAmount) {
            this.name = name;
            this.inv = inv;
            gold = initGoldAmount;
        }
        
        private boolean customContains(List<ItemInventory<? extends Item>> inv1, List<ItemInventory<? extends Item>> inv2){
            for(ItemInventory i1: inv1){
                for(ItemInventory i2: inv2){
                    if(i1.equals(i2)){
                        return true;
                    }
                }
            }
            return false;
        }

        //retourne vrai si la vente se conclu
        public boolean sell( Inventory<? extends Item> goods, int offeredAmount  ){ 
            if(offeredAmount < goods.getTotal()){
                return false;
            }
            if( customContains(inv.showItems(), goods.showItems()) ){
                gold += offeredAmount;
                inv.removeAllFromInv(goods.showItems());
                return true;
            }
            else{
                System.out.println("Merchant does not have some of the selected items.");
                return false;
            }
        }

        //Retourne les objets dispos
        public Inventory<? extends Item> showInventory() { 
            return inv;
        } 

        public int buy( Inventory<? extends Item> goods ) {
            int goldValue =  goods.getTotal();
            gold -= goldValue;//le marchand est debite de la somme
            inv.addAllToInv(goods.showItems());
            return goldValue;
        } 
}
