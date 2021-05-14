package ch.unige.cui.rpg;

import java.util.*;
import java.util.Random;
import java.io.File;

public class Game {

    public static void main(String[] args){
        Random rng = new Random(System.currentTimeMillis());
        String fn = "src/main/resources/potions.txt";
        File file = new File(fn);
        String absolutePath = file.getAbsolutePath();
        
        //Player(String name, int maxHP, int maxMana, int armor, int gold) 
        Player Lancelot = new Player("Lancelot", 100, 50, 75, 25);

        Merchant potionVendor = new Merchant(10, absolutePath);

        List<Item> viewedGoods = potionVendor.viewGoods();


        System.out.println("\n\n *** START OF SCENARIO *** \n\n");

        //Voir etat des variables du joueur et marchand avant la transaction
        System.out.println("\n\n Player bag BEFORE transaction: "+ Lancelot.getBag());
        System.out.println("\n\n Player gold BEFORE transaction: "+ Lancelot.getGold());

        System.out.println("\n\n Merchant s goods BEFORE transaction: "+ potionVendor.viewGoods());
        System.out.println("\n\n Merchant s gold BEFORE transaction: "+ potionVendor.getGold());


        System.out.println("\n\n Viewing merchant's goods: "+viewedGoods.toString());

        //scenario: player veut acheter item a un index choisi dans la liste de produits du marchand qu'il a pu voir (viewdGoods)
        int chosenItemIdx = 3;
        
        //le moteur de jeu verif si le joueur a assez d'argent pour effectuer la transaction achat/vente
        if( Lancelot.getGold() >= viewedGoods.get(chosenItemIdx).getPrice() ){

            Item chosenItem = potionVendor.sell(viewedGoods, chosenItemIdx, viewedGoods.get(chosenItemIdx).getPrice());

            System.out.println("\n\n Chosen item: "+chosenItem);

            //le moteur de jeu se charge d'appeler la methode buy
            Lancelot.buy( Lancelot.getBag(), chosenItem); 
        }

        
        //constater que l'objet a ete enleve du stock du marchand et mis dans le sac du jouer
        //et aussi que les sommes d'or on bien ete transferees
        System.out.println("\n\n Player bag AFTER transaction: "+ Lancelot.getBag());
        System.out.println("\n\n Player gold AFTER transaction: "+ Lancelot.getGold());

        System.out.println("\n\n Merchant s goods AFTER transaction: "+ potionVendor.viewGoods());
        System.out.println("\n\n Merchant s gold AFTER transaction: "+ potionVendor.getGold());

    }
}