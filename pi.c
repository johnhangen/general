# include <stdio.h>

int main(int argc, char const *argv[])
{
    int dig;
    int diOfPi[12] = {3,1,4,1,5,9,2,6,5,3,5,9};
    
    printf("how many digits of pi do you want to see: \n");
    scanf("%i", &dig);

    if (dig >= 1)
    {
        printf("3.");
        for (int i = 1; i < dig; i++)
        {
            printf("%i", diOfPi[i]);
        }
    }

    return 0;
}
