package ch.unige.cui.rpg;
//import java.util.Random;
import java.util.*;

import ch.unige.cui.rpg.Item;

public class Merchant {
    

    private List<Item> goods = new ArrayList<>();
    private int gold;

    //a constructor specific to a potion vendor
    public Merchant(int nbPotions, String fn){
        Random rng = new Random(System.currentTimeMillis());
        //String fn = "src/main/resources/potions.txt";
        //File file = new File(fn);
        //String absolutePath = file.getAbsolutePath();
        LootGenerator lg = new LootGenerator(fn);
        for(int i=0;i<nbPotions;i++){
            goods.add(lg.single(rng));
        }
        gold=0;
    }

    //a more general constructor
    public Merchant(List<Item> goods, int gold) {
        this.goods = goods;
        this.gold = gold;
    }

    //interet du wildcard ici: covaricance de la list qui aurait l avantage d assouplir les preconditions
    //i.e. type Item en arg peut etre généralisé mais pas spécialisé , et de plus sell() est une methode de producteur
    //donc PECS -> Producer Extends
    public Item sell(List<? extends Item> goods, int idx, int offeredAmount){
            this.gold += offeredAmount;
            Item obj = goods.remove(idx);
            return obj;
    }


    public List<Item> viewGoods() {
        return goods;
    }

    public int getGold() {
        return gold;
    }
    
}
