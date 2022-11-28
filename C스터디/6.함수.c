포인터 반환시 잘하는 실수

#include <stdio.h>

int *ten()    // int 포인터를 반환하는 ten 함수 정의
{
    int num1 = 10;   // num1은 함수 ten이 끝나면 사라짐

    return &num1;    // 함수에서 지역 변수의 주소를 반환하는 것은 잘못된 방법
} //        ↑ warning C4172: 지역 변수 또는 임시 변수의 주소를 반환하고 있습니다.

int main()
{
    int *numPtr;

    numPtr = ten();    // 함수를 호출하고 반환값을 numPtr에 저장

    printf("%d\n", *numPtr);    // 10: 값이 나오긴 하지만 이미 사라진 변수를 출력하고 있음

    return 0;
}

그렇다면 어떻게? 포인터를 반환하려면 다음과 같이 malloc 함수로 메모리를 할당한 뒤 반환해야 합니다.

#include <stdio.h>
#include <stdlib.h>    // malloc, free 함수가 선언된 헤더 파일

int *ten()    // int 포인터를 반환하는 ten 함수 정의
{
    int *numPtr = malloc(sizeof(int));    // int 크기만큼 동적 메모리 할당

    *numPtr = 10;    // 역참조로 10 저장

    return numPtr;   // 포인터 반환. malloc으로 메모리를 할당하면 함수가 끝나도 사라지지 않음
}

int main()
{
    int* numPtr;

    numPtr = ten();    // 함수를 호출하고 반환값을 numPtr에 저장

    printf("%d\n", *numPtr);    // 10: 메모리를 해제하기 전까지 안전함

    free(numPtr);    // 다른 함수에서 할당한 메모리라도 반드시 해제해야 함

    return 0;
}

중단점 삽입/삭제: F9
디버깅 시작 및 계속: F5
디버깅 중지: Shift+F5
프로시저 단위 실행: F10
한 단계씩 코드 실행: F11
프로시저 나가기: Shift+F11


// 함수는 return을 만나면 죽는다!
// 나누기0 같은 예외처리를 if-return을 이용하여 할 수 있다.