package ch.unige.cui.rpg;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class Trader {
	private List<Item> tradeGoods = new ArrayList<>();
	private int gold;
	
	public Trader(int nbPotions, String fn) {
		Random rng = new Random(System.currentTimeMillis());
		LootGenerator lg = new LootGenerator(fn);
		for(int i=0;i<nbPotions;i++){
			tradeGoods.add(lg.single(rng));
        }
		gold = 0;
	}
	
	public List<Item> getTradeGoods(){
		return tradeGoods;
	}
	
	public Item sellPotion(List<? extends Item> stock, int idx, int offeredAmount) {
		this.gold += offeredAmount;
		Item obj = tradeGoods.remove(idx);
		return obj;
	}

}
