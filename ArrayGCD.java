

public class ArrayGCD {
    



    public static void main(String[] args) {
        
        int arr[] = {2, 3, 60, 90, 50};
        int index[] = {2, 4};
        // System.out.println("GCD is : " + gcd(arr));
        pushToGCD(arr, index);
    }


    public static void pushToGCD(int arr[], int index[]) {

        int firstIndex = index[0];
        int secondIndex = index[1];

        for (int i = firstIndex; i < secondIndex-1; i++) {
           
            System.out.println(gcd(arr[i],arr[i+1]));
        }
        
    }


    public static int gcd(int firstIndex, int secondIndex) {
        
        if (firstIndex == 0 || secondIndex == 0)
            return 0;
        if (firstIndex == secondIndex)
            return firstIndex;
        if (firstIndex > secondIndex)
            return gcd(firstIndex-secondIndex, secondIndex);
        else 
            return gcd(firstIndex, secondIndex-firstIndex);

    }


}
