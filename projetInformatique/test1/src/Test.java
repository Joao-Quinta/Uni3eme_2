import org.json.*;
import java.io.*;  
import java.io.IOException;

public class Test {
	   public static void main(String[] args) {
		   
		   String nom = "testt.json";
		   JSONObject obj = new JSONObject();
		   
		   obj.put("name", "foo");
		   obj.put("num", "2");
		   obj.put("balance", "3");
		   obj.put("is_vip", "4");
			
		   System.out.print(obj);
		    try {
		        File myObj = new File(nom);
		        if (myObj.createNewFile()) {
		          System.out.println("File created: " + myObj.getName());
		        } else {
		          System.out.println("File already exists.");
		        }
		      } catch (IOException e) {
		        System.out.println("An error occurred.");
		        e.printStackTrace();
		      }
		    
		    try {
		        FileWriter myWriter = new FileWriter(nom);
		        myWriter.write(obj.toString());
		        myWriter.close();
		        System.out.println("Successfully wrote to the file.");
		      } catch (IOException e) {
		        System.out.println("An error occurred.");
		        e.printStackTrace();
		      }
		    
		   
	   }
}
