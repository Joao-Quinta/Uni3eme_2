package ch.unige.cui.rpg;

import ch.unige.cui.rpg.Item;
import java.util.*;

public class Player {

    private final String name;
    private final  int maxHP;
    private final int maxMana;
    private int HP;
    private int mana;
    private int armor;
    private int gold;
    private List<Item> bag = new ArrayList<>();

    public Player(String name, int maxHP, int maxMana, int armor, int gold) {
        this.name = name;
        this.maxHP=maxHP;
        this.maxMana=maxMana;
        this.HP = maxHP;
        this.mana = maxMana;
        this.armor = armor;
        this.gold = gold;
    }

    public int getGold() {
        return gold;
    }

    public String getName() {
        return name;
    }

    public int getHP() {
        return HP;
    }

    public int getMana() {
        return mana;
    }

    public int getArmor() {
        return armor;
    }

    public List<Item> getBag() {
        return bag;
    }

    public void buy( List<? super Item> bag, Item obj) {
        //on considere que les verif si joueur a assez d or pour acheter etc
        //sont fait a l exterieur de la fonction, par le moteur du jeu.
            bag.add(obj);
            gold -= obj.getPrice();
    }


}
