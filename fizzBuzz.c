# include <stdio.h>
  
int main()
{
    int value;

    printf("Run fizz buzz to what number?");
    scanf("%i", &value);
    for(int i = 1; i <= value; i++)
    {
        if(i % 5 == 0 || i % 3 == 0)
        {
            if(i % 3 == 0)
            {
            printf("fizz");
            }
            if(i % 5 == 0)
            {
            printf("buzz");
            }
        printf("\n");
        }
        else
        {
            printf("%i \n", i);
        }
    }
    return 0;
}