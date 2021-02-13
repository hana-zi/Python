import java.io.*;
import java.util.*;
public class CampApp{
	public static void main(String[] args)throws Exception{
		FileInputStream fis = new FileInputStream("dara.csv");
		inputStream fis = new FileInputStream("data.csv");
		InputStreamReader isr=new InputStreamReader(fis,"utf8");
		BufferedReader br=new BufferedReader(isr);
		Map<String,Integer>names=new HashMap<>();
		Map<String,Integer>names=new HashMap<>();

		int total=0;
		System.out.println("csvデータ");
		System.out.println("---------------");
		String line;
		while((line=br.readLine())!=null){
			System.out.println(line);
			String[] data=line.split(",");
			String name=data[0];
			String item=data[1];
			int price=Integer.parseInt(data[2]);
			total+=price;
			if(names.containsKey(name)){
				names.put(name,names.get(name)+price);
			}else{
				names.put(name,price);
			}
			if(items.containsKey(item)){
				items.put(item,items.get(item)+price);
			}else{
				items.put(item,price);
			}
		}
		System.out.println("\nキャンプ会計");
		System.out.println("------------------");
		for(String item:items.keySet()){
			System.out.println(item+":"+items.get(item));
		}
		int perYen=total/names.size();
		System.out.println("\n個人別会計(１人あたり:"+perYen+"円)");
		System.out.println("------------------");
		for(String name:names.keySet()){
			System.out.printf("%s:%s%d%n",name,names.get(name) < perYen ? "-":"+",Math.abs(names.get(name)-perYen) );
		}
	}
}

FileInputStream fis = new FileInputStream("data.csv");
inputStreamReader isr=new InputStreamReader(fis,"utf8");
BufferedReader br=new BufferedReader(isr);
String line;
while((line=br.readLine()) != null){
	System.out.println(line);
}
