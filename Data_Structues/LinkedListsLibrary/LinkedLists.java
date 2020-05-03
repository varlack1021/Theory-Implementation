
/**
 * Creation of LinkedLists Data structire and its Methods
 *
 * @author Pharez
 */

//Creaes a Node with int data and a reference to another Node

 class Node {

  int data;
  Node next;
  Node (int d ) {
     data = d;
     next= null;
   }

}

//---------------------------------------------------------------------

//Initializes a Linked List with only one Node reference

class LinkedList {
Node head;

public LinkedList() {

    head = null;

}

//----------------------------------------------------------------

 public void add(int x) {

 if (head == null)
 head = new Node(x);

 else {
  Node n = new Node(x);
  Node temp = head;

  while(temp.next != null) {

    temp = temp.next;
   }

    temp.next = n;

  }
}

//--------------------------------------------------------------------

public void print() {
 Node temp = head;

 while(temp.next != null) {

 System.out.println(temp.data + " ");
 temp = temp.next;
 }

    System.out.println(temp.data);
}

//--------------------------------------------------------------------------

public void addStart(int x) {
 Node temp = head;
 head  = new Node(x);
 head.next = temp;
}

//---------------------------------------------------------------------------

public void removeFirst() {

  head = head.next;

}

//------------------------------------------------------------------------
public void removeLast()
{
  Node temp = head;
  while(temp.next != null) {

     if (temp.next.next == null) {
        temp.next = null;
        break;
    }

    temp = temp.next;
  }
}

//----------------------------------------------------------------------------

public void setPoint(int x, int place) throws NullPointerException {
  Node node = new Node(x);
  Node temp = head;

  if (x == 0)
  removeFirst();
  else {

    for(int i = 0; i<place-1; i++) {

    temp = temp.next;

    }

    node.next = temp.next;
    temp.next = node;
  }
}

//---------------------------------------------------------------------------

public void removePoint(int place) throws NullPointerException {
 Node temp = head;

 for(int i = 0; i< place-1; i++) {

    temp =  temp.next;
 }

    temp.next = temp.next.next;

}

//--------------------------------------------------------------------------

public int find(int find) throws NullPointerException {
  int place = 0;
  Node temp = head;
  while(temp.data != find) {
        temp = temp.next;
        place++;
     }

    return place;

    }

//-------------------------------------------------------------------------

public void addAfter(int value, int data) throws NullPointerException {
  Node node = new Node(data);
  Node temp = head;
  while (temp.data != value) {
    temp = temp.next;
    }

  node.next = temp.next.next;
  temp.next = node;

}

//--------------------------------------------------------------------------

public void removeValue(int value) {
  Node temp = head.next;
  Node temp2 = head;
  while(temp.data != value) {

    temp = temp.next;
    temp2 = temp2.next;

}

    temp2.next = temp2.next.next;
    temp = null;

  }
}

//------------------------------------------------------------------------------

public class LinkedLists{

public static void main (String ag[]) {

LinkedList links = new LinkedList();

try {
links.add(5);
links.add(7);
links.add(3);
links.add(8);
links.addStart(10);
links.addAfter(7,2);
links.print();
//links.removePoint(8);
//links.removeFirst();
//links.removeLast();
//System.out.println();
//links.print();
//System.out.println();
}
catch(NullPointerException ex) {
  System.out.println("The index you entered does not exists");}
 }
}
