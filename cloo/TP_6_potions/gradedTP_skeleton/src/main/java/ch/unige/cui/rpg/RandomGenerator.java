package ch.unige.cui.rpg;
import java.util.Random;

public interface RandomGenerator<T> {
    public T single(Random rng);
}