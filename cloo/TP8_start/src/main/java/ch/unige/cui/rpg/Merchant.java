package ch.unige.cui.rpg;
import java.util.*;

//interface "vide" mais qui etdent buyer et seller en meme temps
//pour ne pas avoir a reecire extends Buyer<T>, Seller<T> pour chaque classe implementant un marchand ?
public interface Merchant<T extends Item> extends Buyer<T>, Seller<T> {}

