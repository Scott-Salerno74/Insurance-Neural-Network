public class test {
    public static void main(String[] args) {
        String s = ",,,";

        String[] a = s.split(",", -1);

        for(String s1: a){
            System.out.println(s1);
        }

        System.out.println(a.length);
    }
}
