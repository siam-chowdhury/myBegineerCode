public class UnionAndIntersection {
    

    public static void main(String[] args) {
        
        int arr1[] = {1, 3, 4, 5, 7};
        int arr2[] = {2, 3, 5, 6};

        System.out.println("Union : ");
        getUnion(arr1, arr2);

        System.out.println("Intersection : ");
        getIntersection(arr1, arr2);


    }


    // this method is to get union
    public static void getUnion(int[] arr1, int[] arr2) {
        int i = 0, j = 0;
        int len1 = arr1.length;
        int len2 = arr2.length;

        while (i < len1 && j < len2) {
            if (arr1[i] < arr2[j])
                System.out.print(arr1[i++] + " ");
            else if (arr1[i] > arr2[j])
                System.out.print(arr2[j++] + " ");
            else {
                System.out.print(arr1[i++] + " ");
                j++;
            }
        }

        // printing remain elements from large array
        while (i < len1)
            System.err.print(arr1[i++] + " ");
        while (j < len2)
            System.err.print(arr2[j++] + " ");
        
        System.out.println();

    }
    
    // this method is to get intersection
    public static void getIntersection(int[] arr1, int[] arr2) {
        int i = 0, j = 0;
        int len1 = arr1.length;
        int len2 = arr2.length;

        while (i < len1 && j < len2) {
            if (arr1[i] < arr2[j])
                i++;
            else if (arr1[i] > arr2[j])
                j++;
            else {
                System.out.print(arr1[i++] + " ");
                j++;
                
            }
        }
    }
    
    
    
    
    
}

