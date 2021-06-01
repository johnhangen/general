# include <stdio.h>

void swap(int *x,int  *y);

int main(void)
{
	/* variables */
	int x = 0;
	int y = 1;

	printf("Start: x = %i and y = %i\n",x, y);

	swap(&x, &y);

	printf("End: x = %i and y = %i\n",x, y);

	return 0;
}

void swap(int *x,int *y)
{
	int temp; 
	temp = *x;
	*x = *y;
	*y = temp;
}
