# include <stdio.h>

int main(int argc, char const *argv[])
{
    int dig;
    int diOfE[20] = {2,7,1,8,2,8,1,8,2,8,4,5,9,0,4,5,2,3,5,3};
    
    printf("how many digits of E do you want to see: \n");
    scanf("%i", &dig);

    if (dig >= 1)
    {
        printf("3.");
        for (int i = 1; i < dig; i++)
        {
            printf("%i", diOfE[i]);
        }
    }

    return 0;
}