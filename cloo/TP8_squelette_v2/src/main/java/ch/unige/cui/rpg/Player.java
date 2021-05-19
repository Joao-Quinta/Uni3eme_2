package ch.unige.cui.rpg;
import java.util.*;

public class Player {

    private final String name;
    private final int maxHP;
    private final int maxMana;
    private int HP;
    private int mana;
    private int armor;
    private int gold;
    private Inventory bag = new Inventory();

    public Player(String name, int maxHP, int maxMana, int armor, int gold, Inventory bag) {
        this.name = name;
        this.maxHP=maxHP;
        this.maxMana=maxMana;
        this.HP = maxHP;
        this.mana = maxMana;
        this.armor = armor;
        this.gold = gold;
        this.bag=bag;//on pourrait passer un inventaire au joueur a l instanciation, sinon un inv vide
    }

    public Player(String name, int maxHP, int maxMana, int armor, int gold) {
        this.name = name;
        this.maxHP=maxHP;
        this.maxMana=maxMana;
        this.HP = maxHP;
        this.mana = maxMana;
        this.armor = armor;
        this.gold = gold;
        //pas d inv = inv vide par defaut
    }

    public int getGold() {
        return gold;
    }

    public void pay(int gold){
        this.gold -= gold;
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

    public void receivePayment(int gold){
        this.gold += gold;
    }

    public Inventory<? extends Item> showBagContents(){
        return bag;
    }

    public void addToBag(Inventory<? extends Item> items){
        //inv de potion -> on a le droit de les mettre dans un sac d items
        //une potion -> droit de la mettre dans un sac de  potions ou soit dans un sac de tous les supertypes de potions
        //MAIS un item ->  est ce qu on a le droit de le mettre dans un sac de potions? ->Non car on ne sait  encore que ss-type c est
        bag.addAllToInv(items.showItems());
    }

    public void removeFromBag(Inventory<? extends Item> items){
        bag.removeAllFromInv(items.showItems());
    }

}
