public class Letter {
    
    
    public static StringBuffer letters = new StringBuffer(); // store [a-z A-Z 0-9 ] and symnol

    // Convert [int to char]
    public static int addRandomLetter() {

        for (int symbol = 33; symbol <= 123; symbol++) {
            char ch = (char) symbol;
            letters.append(ch);
        }
        return letters.length();

    }




}
