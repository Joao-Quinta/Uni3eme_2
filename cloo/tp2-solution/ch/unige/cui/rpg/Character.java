package ch.unige.cui.rpg;

public class Character{
  private final String name;
  private final int maxHP;
  private int gold;
  private int currentHP;
  private int armor;
  private Quest currentQuest;
  
  public Character(String name,int maxHP, int gold){
	  this.name=name;
	  this.maxHP=maxHP;
	  this.currentHP=maxHP;
	  this.gold=gold;
  }
  
  public void wound(int damage){
    final int actual = damage - armor;
    if( actual < 0 ) return;
	final int nextHP = currentHP - damage;
	if( nextHP > 0 ) currentHP = nextHP;
    else currentHP = 0;
  }
  
  public void heal(int hp){
    if( hp <= 0) return;
    final int nextHP = currentHP + hp;
	if( nextHP < maxHP ) currentHP = nextHP;
	else currentHP = maxHP;
  }
  
  public void startQuest(Quest q){
	  this.currentQuest = q;
  }
  
  public String toString(){
	  return "Name="+name+"gold="+gold+"currentHP="+currentHP+"armor="+armor+currentQuest.toString();
  }
  
}