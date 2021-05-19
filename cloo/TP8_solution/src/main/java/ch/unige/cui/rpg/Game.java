package ch.unige.cui.rpg;

import java.util.*;
import java.io.File;

public class Game {

    public static void main(String[] args){
        System.out.println("TP8 v3");
        /*
        //NOT used at the moment
        Random rng = new Random(System.currentTimeMillis());
        String fn = "src/main/resources/potions.txt";
        File file = new File(fn);
        String absolutePath = file.getAbsolutePath();
        LootGenerator lg = LootGenerator(absolutePath);
        */

        //chanque stack de potions a un ID unique car il s agit du meme type de potion (meme nom, valeur, poids, prix) seule la quantite
        //de cet item varie par exemple ici 100
        final int healingPotID = 0;
        final int manaPotID = 1;
        var healingPotions = new ItemInventory(healingPotID, new HealingPotion("Healing Potion", 25, 2, 5),100);
        var manaPotions = new ItemInventory(manaPotID, new ManaPotion("Mana Potion", 15, 3, 10),100);
        Inventory merchantInv = new Inventory();
        merchantInv.addItemInventoryToInv(healingPotions);
        merchantInv.addItemInventoryToInv(manaPotions);
        int initGoldAmount = 1000;

        var DrovnarStrongbrew = new PotionMerchant("Drovnar Strongbrew", merchantInv, initGoldAmount);
        var Boromir = new Player("Boromir", 100, 50, 75, 150);

        System.out.println("\n *** START OF SCENARIO v2 *** \n");


        System.out.println(DrovnarStrongbrew.getName()+"'s goods BEFORE 1st transaction: "+DrovnarStrongbrew.showInventory());
        System.out.println(DrovnarStrongbrew.getName()+"'s gold BEFORE 1st transaction: "+DrovnarStrongbrew.getGold());
        System.out.println();
        System.out.println(Boromir.getName()+"'s goods BEFORE 1st transaction: "+Boromir.showBagContents());
        System.out.println(Boromir.getName()+"'s gold BEFORE 1st transaction: "+Boromir.getGold());


        //client achete des potions: il passe un inventaire contenant ce qu il veut acheter

        //select goods from vendor s inv
        Inventory viewedInvFromVendor = DrovnarStrongbrew.showInventory();
        Inventory selectedGoods = new Inventory();
        // >>>>>>>>>> normalement on devrait cloner et renvoyer une copie profonde de l inventaire au lieu de faire cela
        int nbHealingPotions = 3;
        int nbManaPotions = 1;
        ItemInventory selectedHealingPotions = viewedInvFromVendor.getItemInventoryByID(healingPotID).setAmmount(nbHealingPotions);
        //client veut acheter 3 potions de vie
        ItemInventory selectedManaPotions = viewedInvFromVendor.getItemInventoryByID(manaPotID).setAmmount(nbManaPotions);
        //ajout a l inventaire de selection
        selectedGoods.addItemInventoryToInv(selectedHealingPotions);
        selectedGoods.addItemInventoryToInv(selectedManaPotions);



        //Transaction #1
        //le marchand vend (= le joueur achete)
        //c est le moteur du jeu qui se charge de realiser la transaction
        //$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        if(Boromir.getGold()>=selectedGoods.getTotal()){
            boolean b =  DrovnarStrongbrew.sell( selectedGoods, selectedGoods.getTotal() );
            Boromir.addToBag(selectedGoods);
            Boromir.pay(selectedGoods.getTotal());
        }
        else{
            System.out.println("\n\n !!!!!!!!! Player "+Boromir.getName()+" does not have enough gold. !!!!!!!!!");
            return;//pour ce scenario on s arrete
        }
        //$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        System.out.println("\n >>>>>>>>> Merchant sells to player (1st transaction): \n");
        System.out.println("\nSelected goods = "+selectedGoods );
        System.out.println("\nSelected goods : total amount to pay = "+selectedGoods.getTotal() );
        System.out.println("\nMerchant "+DrovnarStrongbrew.getName()+" 's inv AFTER 1st transaction: "+DrovnarStrongbrew.showInventory());
        System.out.println("\nMerchant "+DrovnarStrongbrew.getName()+" 's gold AFTER 1st transaction: "+DrovnarStrongbrew.getGold());
        System.out.println("\n"+Boromir.getName()+"'s goods AFTER 1st transaction: "+Boromir.showBagContents());
        System.out.println("\n"+Boromir.getName()+"'s gold AFTER 1st transaction: "+Boromir.getGold());




        //Transaction #2
        //le marchand achete (= le joueur vend)
        //Boromir vend au marchant 1 potion de mana et 2 potions de vie
        Inventory selectedGoods2 = new Inventory();
        //amount of potions of each type to selle to merchant i,e, fror merchant to buy from player
        int nbHealingPotions2 = 2;
        int nbManaPotions2 = 1;
        ItemInventory selectedHealingPotions2 = Boromir.showBagContents().getItemInventoryByID(healingPotID).setAmmount(nbHealingPotions2);
        ItemInventory selectedManaPotions2 = Boromir.showBagContents().getItemInventoryByID(manaPotID).setAmmount(nbManaPotions2);
        selectedGoods2.addItemInventoryToInv(selectedHealingPotions2);
        selectedGoods2.addItemInventoryToInv(selectedManaPotions2);

        //c est le moteur du jeu qui se charge de realiser la transaction
        //$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        if(DrovnarStrongbrew.getGold()>=selectedGoods2.getTotal()){
            DrovnarStrongbrew.buy(selectedGoods2);
            Boromir.receivePayment(selectedGoods2.getTotal());
            Boromir.removeFromBag(selectedGoods2);
        }
        else{
            System.out.println("\n\n !!!!!!!!! Merchant "+DrovnarStrongbrew.getName()+" does not have enough gold. !!!!!!!!!");
        }
         //$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

         System.out.println("\n >>>>>>>>> After Merchant bought from player (2nd transaction): \n");
         System.out.println("\nMerchant "+DrovnarStrongbrew.getName()+" 's inv AFTER 2st transaction: "+DrovnarStrongbrew.showInventory());
         System.out.println("\nMerchant "+DrovnarStrongbrew.getName()+" 's gold AFTER 2st transaction: "+DrovnarStrongbrew.getGold());

         System.out.println("\n"+Boromir.getName()+"'s goods AFTER 2st transaction: "+Boromir.showBagContents());
         System.out.println("\n"+Boromir.getName()+"'s gold AFTER 2st transaction: "+Boromir.getGold());

        
    }
}