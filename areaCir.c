# include <stdio.h>

int main(void)
{
    int radius;
    printf("What is the radius");
    scanf("%i", &radius);
    double area = 3.14*(radius*radius);
    printf("The area of a circle with a radius %i is: %f\n", radius, area);
    return 0;
}