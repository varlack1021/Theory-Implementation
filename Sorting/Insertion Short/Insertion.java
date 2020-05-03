/**
 * Implementation of the Insertion Sort Alogorithm
 *
 * @author Pharez
 */
public class Insertion {

public static void main(String args[]) {

 //Input samples to be sorted

 int [] scores = {6,0,89,5,41,2,1,6,7};

 //Prints the unsorted array

 for (int i = 0; i<scores.length;i++) {

 System.out.print(scores[i]+"\t");

 }

 //Sorts the arrray using Insertion Sorting Sort

 InsertionSort(scores);
 System.out.println("");

 //Prints the array after being sorted

 for (int i = 0; i<scores.length;i++) {

 System.out.print(scores[i]+"\t");

 }

}
//---------------------------------------------------------------------------
/*
 *@ param scores array
 *Searches the array sequentially and sorts up to a search size within the arrray
 *Search size begins at zero (index zero)
 *When the search size is increasd by one, the rest of the array will already sorted
 *@return Pointer to sorted array
 */
public static void InsertionSort(int [] scores) {

  for(int i =1; i < scores.length; i++) {

    for(int j = 0; j < i; j++) {

      if (scores[j] > scores[i]) {
           int temp = scores[i];
           scores[i] = scores[j];
           scores[j] = temp;
        }
      }
    }
  }
}
