// wanna make a GUI for this is python
package other;

public class caesarCipher
{
    public static void main(String[] args) {
        char[] list = {'f','d','c'};
        dycrptManual(list);
    }

    public static void encrpt(char[] list, int key)
    {
        for(int i = 0; i <= list.length-1; i++)
        {
            int tempChar = list[i];
            if (tempChar >= 65 || tempChar <= 90)
            {
                tempChar = tempChar + 32;
            }
            if(tempChar + key > 122)
            {
                tempChar = (tempChar - 26) + key;
            }
            else
            {
                tempChar = tempChar + key;
            }
            list[i] = (char)tempChar;
        }
        System.out.println(list);
    }

    public static void dycrptManual(char[] list)
    {
        for(int key = 1; key <= 26; key++)
        {
            char[] newlist = {'0', '0', '0'};
            for(int i = 0; i <= list.length-1; i++)
            {
                int tempChar = list[i];
                if (tempChar >= 65 || tempChar <= 90)
                {
                    tempChar = tempChar + 32;
                }
                if(tempChar - key < 97)
                {
                    tempChar = (tempChar + 26) - key;
                }
                else
                {
                    tempChar = tempChar - key;
                }
                newlist[i] = (char)tempChar;
            }
            System.out.println(newlist);
        }
    }

    public static void dycript(char[] list, int key)
    {
        for(int i = 0; i <= list.length-1; i++)
        {
            int tempChar = list[i];
            if (tempChar >= 65 || tempChar <= 90)
            {
                tempChar = tempChar + 32;
            }
            if(tempChar - key < 97)
            {
                tempChar = (tempChar + 26) - key;
            }
            else
            {
                tempChar = tempChar - key;
            }
            list[i] = (char)tempChar;
        }
        System.out.println(list);
    }
}