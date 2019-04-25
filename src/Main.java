import java.io.*;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(new File("QHP_PY2018_Medi-_Indi-_Land.csv")));

        String[] OGHeaders = br.readLine().split(",");
        ArrayList<String> OGHeaderList = new ArrayList<>();

        for(int i = 0; i < OGHeaders.length; i++) {
            OGHeaderList.add(OGHeaders[i]);
        }

        String[] headers = "State Code,County Name,Metal Level,Issuer Name,Plan Marketing Name,Plan Type,Plan Brochure URL,EHB Percent of Total Premium,Premium Child Age 0-14,Premium Child Age 18,Premium Adult Individual Age 21,Premium Adult Individual Age 27,Premium Adult Individual Age 30 ,Premium Adult Individual Age 40 ,Premium Adult Individual Age 50 ,Premium Adult Individual Age 60 ,Premium Couple 21  ,Premium Couple 30 ,Premium Couple 40 ,Premium Couple 50 ,Premium Couple 60 ,\"Couple+1 child, Age 21\",\"Couple+1 child, Age 30 \",\"Couple+1 child, Age 40 \",\"Couple+1 child, Age 50 \",\"Couple+2 children, Age 21\",\"Couple+2 children, Age 30 \",\"Couple+2 children, Age 40 \",\"Couple+2 children, Age 50\",\"Couple+3 or more Children, Age 21\",\"Couple+3 or more Children, Age 30\",\"Couple+3 or more Children, Age 40\",\"Couple+3 or more Children, Age 50\",\"Individual+1 child, Age 21\",\"Individual+1 child, Age 30\",\"Individual+1 child, Age 40\",\"Individual+1 child, Age 50\",\"Individual+2 children, Age 21\",\"Individual+2 children, Age 30\",\"Individual+2 children, Age 40\",\"Individual+2 children, Age 50\",\"Individual+3 or more children, Age 21\",\"Individual+3 or more children, Age 30\",\"Individual+3 or more children, Age 40\",\"Individual+3 or more children, Age 50\",Medical Deductible - Individual - Standard,Drug Deductible - Individual - Standard,Medical Deductible - Family - Standard,Drug Deductible - Family - Standard,Primary Care Physician - Standard,Specialist - Standard,Emergency Room - Standard,Inpatient Facility - Standard,Inpatient Physician - Standard,Generic Drugs - Standard,Preferred Brand Drugs - Standard,Non-preferred Brand Drugs - Standard,Specialty Drugs - Standard".split(",");

        int[] indices = new int[headers.length];

        for(int i = 0; i < indices.length; i++) {
            indices[i] = OGHeaderList.indexOf(headers[i]);
            if(indices[i] == -1) {
                System.out.println("Cannot find header:  " + headers[i]);
            }
        }

        BufferedWriter writer = new BufferedWriter(new FileWriter("dataset.csv"));
        for(int i = 0; i < headers.length - 1; i++) {
            writer.write(headers[i]+ ",");
        }

        writer.write(headers[headers.length - 1] + "\n");

        String line = "";
        while((line = br.readLine()) != null) {
            String[] data = line.split(",", -1);
            for(int i = 0; i < indices.length - 1; i++){
                writer.write(data[indices[i]] + ",");
            }

            writer.write(data[indices[indices.length - 1]] + "\n");
        }

        writer.flush();
        writer.close();
    }
}
