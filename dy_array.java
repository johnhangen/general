// ADT Circular Queue
// 
// Jack Hangen 
// April 19, 2021
//
// Create a circular ADT

public class dy_array
{
    // data
    char[] list;
    int size;

    public dy_array(char[] list)
    {
        this.list = list;
        this.size = 0;
    }

    public int getSize()
    {
        return(size);
    }

    public boolean isFull()
    {
        if(list.length - 1 == size)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public void append(char item)
    {
        if(list.length - 1 < size)
        {
            int newLength = (list.length)*2;
            char[] oldList = list;
            char[] list = new char[newLength];
            System.out.println(oldList.length);
            System.out.println(list.length);
            for (int i  = 0; oldList.length - 1 >= i; i++)
            {
                char j = oldList[i];
                System.out.println(j);
                list[i] = j;
            }
            list[size] = item;
            size++;
            this.list = list;
        }
        else
        {
            list[size] = item;
            size++;
        }
    }

    public char returnIndex(int index)
    {
        System.out.println(list.length);
        char place = list[index];
        return place;
    }
}