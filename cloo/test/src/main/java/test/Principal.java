package test;

public class Principal {
	public static void main(String[] args){
		Called test = new Called(5);
		System.out.println("this is the number "+ test.getNumber());
	}

}