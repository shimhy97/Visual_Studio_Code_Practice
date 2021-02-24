void로 선언된 포인터 내부의 값을 다른 변수에 할당하려면, 자료형을 써줘야 함.

int *numPtr =  malloc(sizeof(int));

numPtr[2] = *(numPtr+2)


매우매우 중요!
a[3] 에서 a는 읽기전용 포인터이다.
포인터를 배열처럼 쓰는게 가능했던 이유. 