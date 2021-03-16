public class MissingNumber {
    




public static void main(String[] args) {
    
    int[] arr = {1,3,4,5};
    int len = arr.length;
    int missingNumber = getMissingNumber(arr, len);
    System.out.println(missingNumber);

}


public static int getMissingNumber(int[] arr, int len) {
    int total = (len+1)*(len+2) / 2;
    for (int i = 0; i < len; i++)
        total -= arr[i];
    
    return total;
    
}












}
