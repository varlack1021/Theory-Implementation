import java.util.Scanner;
import java.math.*;


class hashEntry {

    String key;
    int value;

    //Constructor
   
   public hashEntry(String key, int value){

       this.key = key;
       this.value = value;

    }
}

//Hash Table Class

class hashTable {
    
    private int TABLE_SIZE;
    private int size;
    private hashEntry[] table;
    private int primeSize;

    public hashTable(int ts) {
        size = 0;
        TABLE_SIZE = ts;
        table = new hashEntry[TABLE_SIZE];

        for (int i = 0; i < TABLE_SIZE; i++) {
            table[i] = null;
            primeSize = getPrime();
        }

    }
//Function to get a primer number less than table size for myhash2 function
    public int getPrime() {

        for (int i = TABLE_SIZE - 1; i >= 1; i--){
            
            int fact = 0;
            for(int j = 2; j <= (int)Math.sqrt(i); j++) 
            
              if (i % j ==0)
                    fact++;

            if (fact == 0)
               return i;    
            
        }
        //Return a prime number
        return 3;

    }

    //Function to get number key-value pairs
    public int getSize(){
        
        return size;

    }


    //Checks to see if table is empty
    public boolean isEmpty(){

        return size == 0;

    }
    //Clears hashTable
    public void makeEmpty() {
        size = 0;
        for(int i = 0; i < TABLE_SIZE; i++) {

            table[i] =null;

        }
    }

    public int get(String key) {
   
        int hash1 = myhash1(key);
        int hash2 = myhash2(key);

        while (table[hash1] != null && !table[hash1].key.equals(key)) { 

            hash1 += hash2;
            hash1 %= TABLE_SIZE;
        }

    return table[hash1].value;
    
    }

    //Function to get value of a key

    public void insert(String key, int value) {
        
        if(size == TABLE_SIZE) {
            
            System.out.println("Table is Full");
            return;

        }

        int hash1 = myhash1(key);
        int hash2 = myhash2(key);

        while(table[hash1] != null) {

            hash1 += hash2;
            hash1 %= TABLE_SIZE;
        }

        table[hash1] = new hashEntry(key, value);
        size++;
    }

    //Function to remove a key
    public void remove(String key) 
    {
        int hash1 = myhash1( key );
        int hash2 = myhash2( key );        
        
        while (table[hash1] != null && !table[hash1].key.equals(key)) {
 
            hash1 += hash2;
            hash1 %= TABLE_SIZE;
 
        }
        table[hash1] = null;
 
        size--;
    }

    //Function myhash which gives a specific hash value for a given String 

    private int myhash1(String x) {

        int hashVal = x.hashCode();
        hashVal %= TABLE_SIZE;

        if (hashVal < 0) {
            
            hashVal += TABLE_SIZE;
         
  
        }
        return hashVal;
    }

       /* Function myhash function for double hashing */
    private int myhash2(String x ) {
        
        int hashVal = x.hashCode( );
        
        hashVal %= TABLE_SIZE;
        
        if (hashVal < 0)
            hashVal += TABLE_SIZE;
        
        return primeSize - hashVal % primeSize;
    }

    /* Function to print hash table */
    public void printHashTable() {
        
        System.out.println("\nHash Table");
        
        for (int i = 0; i < TABLE_SIZE; i++)
            if (table[i] != null)
                System.out.println(table[i].key +" "+table[i].value);
    }
}

/* Class DoubleHashingHashTableTest */
    public class hash_map {
    
        public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.println("Hash Table Test\n\n");
        System.out.println("Enter size");
        
        /* Make object of HashTable */
        hashTable ht = new hashTable(scan.nextInt() );
 
        char ch;
        /*  Perform HashTable operations  */
        do    
        {
            System.out.println("\nHash Table Operations\n");
            System.out.println("1. insert ");
            System.out.println("2. remove");
            System.out.println("3. get");       
            System.out.println("4. check empty");     
            System.out.println("5. clear");
            System.out.println("6. size");
 
            int choice = scan.nextInt();            
            switch (choice)
            {
            case 1 : 
                System.out.println("Enter key and value");
                ht.insert(scan.next(), scan.nextInt() ); 
                break;                          
            case 2 :                 
                System.out.println("Enter key");
                ht.remove( scan.next() ); 
                break;                        
            case 3 : 
                System.out.println("Enter key");
                System.out.println("Value = "+ ht.get( scan.next() )); 
                break;                                   
            case 4 : 
                System.out.println("Empty Status " +ht.isEmpty());
                break;
            case 5 : 
                ht.makeEmpty();
                System.out.println("Hash Table Cleared\n");
                break;
            case 6 : 
                System.out.println("Size = "+ ht.getSize() );
                break;         
            default : 
                System.out.println("Wrong Entry \n ");
                break;   
            }
            /* Display hash table */
            ht.printHashTable();  
 
            System.out.println("\nDo you want to continue (Type y or n) \n");
            ch = scan.next().charAt(0);                        
        } while (ch == 'Y'|| ch == 'y');  
    }
}


