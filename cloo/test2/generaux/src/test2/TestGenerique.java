package test2;

import java.util.ArrayList;
import java.util.List;

public class TestGenerique<T extends Personne> {
	public static <T> void twice(ArrayList<T> data){
		data.addAll(data);
	}

}
