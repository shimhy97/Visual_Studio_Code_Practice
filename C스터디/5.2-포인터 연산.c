void로 선언된 포인터 내부의 값을 다른 변수에 할당하려면, 자료형을 써줘야 함.

int *numPtr =  malloc(sizeof(int));

numPtr[2] = *(numPtr+2)


매우매우 중요!
a[3] 에서 a는 읽기전용 포인터이다.
포인터를 배열처럼 쓰는게 가능했던 이유. 


/////

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Point3D {
    float x;
    float y;
    float z;
};

int main()
{
    void *ptr = malloc(sizeof(struct Point3D) * 3);
    struct Point3D p[3];
    float result1, result2;

    scanf("%f %f %f %f %f %f %f %f %f", 
        &p[0].x, &p[0].y, &p[0].z, 
        &p[1].x, &p[1].y, &p[1].z, 
        &p[2].x, &p[2].y, &p[2].z
    );

    memcpy(ptr, p, sizeof(struct Point3D) * 3);
    memset(p, 0, sizeof(struct Point3D) * 3);

    // 방법 1: 포인터 연산으로 취급
    result1 = ((struct Point3D*)ptr + 1)->x;
    result2 = ((struct Point3D*)ptr + 2)->z;
    // 방법 2: 배열로서 취급
    // result1 = ((struct Point3D*)ptr)[1].x;
    // result2 = ((struct Point3D*)ptr)[2].z;


    printf("%.1f %.1f\n", result1, result2);

    free(ptr);

    return 0;
}