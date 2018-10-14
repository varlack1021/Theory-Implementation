/**
 * Implementation of the Selection Sort ALgorithm
 *
 * @author Pharez
 */
public class selectionSort
{
    public static void main(String args[])  {

     //Sample data

     int [] array ={5,2,0,1,4,63,7,8,2,5};

     selectionSort(array);

    // Print the sorted array

     for(int i = 0; i< array.length; i++) {

      System.out.print(array[i] + "\t");

     }

  }

//-----------------------------------------------------------------------------


/*
 *Sorts the array by finding the lowest value within the array and
 *moves it to the front of the unsorted array
 *Starts at index 0 and the increments, swapping values at the incrementating indexes
 *@param int array
 *@return Pointer to sorted array
*/
public static int [] selectionSort(int [] array) {

 for (int i = 0; i < array.length; i++) {

   //holds the index that will be swappped

   int swap = i;

  for(int j = i + 1; j < array.length; j++) {

    if(array[swap] < array[j]) {

        swap = j;
     }

   }

   int temp = array[i];
   array[i] = array[swap];
   array[swap] = temp ;

   }

   return array;

   }
}
