import java.util.Scanner;

public class PasswordManager {
    


    // add [a-z A-Z 0-9] and special symbol
    public static void addLetters() {
        
        StringBuffer letters = new StringBuffer();
        for (int i = 33; i <= 123; i++) {
            char word = (char) i;
            letters.append(word);
        }

        setPasswordLength(letters);
    }


    // set password length
    public static void setPasswordLength(StringBuffer letters) {
        
        Scanner in = new Scanner(System.in);
        
        try {
            System.out.println("pwd length : ");
            int length = in.nextInt();
            System.out.println(makePassword(letters, length));
        } 
        catch (Exception e) {
            System.out.println(e);
        }

    }


    // cook password following length
    public static String makePassword(StringBuffer letters, int length) {
        
        StringBuffer randomPwd = new StringBuffer();

        for (int i = 1; i <= length; i++) {
            int random = (int) (Math.random() * letters.length());
            randomPwd.append(letters.charAt(random));
        }

        return randomPwd.toString();
    }


    
    

}   
