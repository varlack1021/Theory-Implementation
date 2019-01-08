/*
*@author Phaerz
*Sorts the array by dividing the array into smaller arrays
*Combines and sorts the smaller arrays
*Divide and conquer technique
*/

public class mergeSort {

public static int comparison = 0;

public static int [] mergeSort(int [] data, int middle, int last) {

/*
*splits the array into sub arrays
*@param data, middle, last
*@return merge, the sorted array
*/

  int [] left  = new int[middle];
  int [] right = new int[data.length-middle];

  for (int i = 0; i < middle; i ++) {
    left[i] = data[i];
  }

  for (int j = middle; j < data.length; j++) {

    right[j - middle] = data[j];

  }


  if(left.length != 1)
  left = mergeSort(left,  left.length/2, left.length);

  if (right.length != 1)
  right = mergeSort(right,  right.length/2, right.length);

  int [] merge = new int[data.length];

  sort(merge, left, right);

  //prints the visual representation of the arrays merging
  /*System.out.println("The length of the two arrays merged is:" + merge.length);
  print("\nThe merged array:");
  printArray(merge);
  print("\n--------------------------------------------");
  print("\n");*/

  return merge;
}

//-----------------------------------------------------------------------------
public static void sort(int [] data, int[] left, int[] right) {

/*
*Sorts the left and right array
*@param data represents the size of both arrays combind
*@param left, right
*/

 int rPointer = 0;
 int lPointer = 0;
 int copied   = 0;

 //prints the visual representation of the sub arrays
 /*print("\n\nLeft Array:");
 printArray(left);

 print("\n\nRight array:");
 printArray(right);*/


 while(copied < data.length) {

   if(lPointer >= left.length) {

     data[copied] = right[rPointer];
     //System.out.println("The value of copy is: " + copied);
     copied++;
     rPointer++;
   }

   else if(rPointer >= right.length) {
     //  print("\nWent 2");
     data[copied] = left[lPointer];
     copied++;
     lPointer++;
   }

   else if(left[lPointer] < right[rPointer]) {
     //print("\nWent 3");
     comparison++;
     data[copied] = left[lPointer];
     copied++;
     lPointer++;
   }

   else {
   //  print("\nWent 4");

   data[copied]  = right[rPointer];
   copied++;
   rPointer++;
   }
  }
 }
}
