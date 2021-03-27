import java.util.Scanner;

public class Length extends Letter {
    

    public static StringBuffer pwd = new StringBuffer(); // store all char and make password

    // get password length 
    public static void passwordLen() {

        Scanner in = new Scanner(System.in);
        System.out.print("pwd length >> ");
        int loop = in.nextInt();
        int len = addRandomLetter();

        for (int start = 0; start < loop; start++) {
            int randomChar = (int) (Math.random() * len);
            pwd.append(letters.charAt(randomChar));
        }

        System.out.println("|");
        System.out.println("|");
        // System.out.println("|");
        System.out.println("----> " + pwd);

    }
}
