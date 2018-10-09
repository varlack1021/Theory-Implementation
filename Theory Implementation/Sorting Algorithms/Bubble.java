/**
 * Implementation of the Bubble Sort Algorithm
 *Bubble Sort compares each index and swaps them if one is bigger than the other
 *Program stops when the each index has been compared
 * @Pharez
 */

public class Bubble
{
   public static void main (String args[])
   {
     //Sample data
     
     int [] numbers = {6,9,2,0,4,15,74,12,9,24,1};

     bubbleSort(numbers);

    for(int i = 0; i<numbers.length;i++)
      {
        System.out.print(numbers[i] + "\t");
      }
}

//------------------------------------------------------------------------

public static void bubbleSort(int [] scores) {

for(int i = 0; i<scores.length;i++) {

    for(int j = 0; j<scores.length-1;j++) {

//If the current index is greater than the next index then they will swap

          if (scores[j] > scores[j+1]) {

             int temp = scores[j];
             scores[j] = scores[j+1];
             scores[j+1] = temp;
    }
   }
  }
 }
}
