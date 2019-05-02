import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.*;
import java.util.List;

public class DataFormat {

    public static void main(String[] args) throws IOException {
        CSVParser parser = new CSVParser(new FileReader(new File("dataset.csv")), CSVFormat.DEFAULT.withQuote(null));

        List<CSVRecord> list = parser.getRecords();

        for (CSVRecord r : list) {
            System.out.println(r.toString());
        }



        //        BufferedReader br = new BufferedReader(new FileReader(new File("dataset.csv")));
//
//        String[] headers = br.readLine().split(",");
//
//        System.out.println(headers.length);
//
//        ArrayList[] ar = new ArrayList[headers.length];
//
//        for(int i = 0; i < ar.length; i++) {
//            ar[i] = new ArrayList();
//        }
//
//        String line = "";
//
//        while((line = br.readLine()) != null) {
//            String[] dataLine = line.split(",", -1);
//            System.out.println(dataLine.length);
//            for(int i = 0; i < dataLine.length; i++) {
//                ar[i].add(dataLine[i]);
//            }
//        }
//
//        Scanner pause = new Scanner(System.in);
//
//        for(int i = 0; i < ar.length; i++) {
//            System.out.print(headers[i]);
//            pause.nextLine();
//            for(Object o : ar[i]) {
//                System.out.println(o);
//            }
//        }
    }

}
