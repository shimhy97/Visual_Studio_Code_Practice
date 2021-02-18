#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int numArr[5];
    int smallestNumber;

    scanf("%d %d %d %d %d", &numArr[0], &numArr[1], &numArr[2], &numArr[3], &numArr[4]);
    int(size) = sizeof(numArr)/sizeof(int) ;    
 

   for( i= 0;, i <= size-2;, i +=1;)
{
int temp=numArr[0];
 if( temp < numArr[i+1])
    temp = numArr[i];
 else
    temp = numArr[i+1];

}
smallestNumber = temp;



    printf("%d\n", smallestNumber);

    return 0;
}