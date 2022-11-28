
!! 자주 실수하는 것?
배열로 문자열을 사용할 때 한 가지 주의할 점은 배열을 선언한 즉시 문자열로 초기화해야 한다는 점입니다. 
배열을 미리 선언해놓고 문자열을 나중에 할당할 수는 없습니다.
즉 다음 코드는 오류가 뜬다.
string_array_assign_error.c
#include <stdio.h>

int main()
{
    char s1[10];     // 크기가 10인 char형 배열 선언
    
    s1 = "Hello";    // 이미 선언된 배열에 문자열을 할당하면 컴파일 에러 발생

    printf("%s\n", s1);    // Hello: %s로 문자열 출력

    return 0;
}



#include <stdio.h>

int main()
{
    char *s1 = "Hello";       // 포인터에 문자열 Hello의 주소 저장

    printf("%c\n", s1[1]);    // e: 인덱스 1(두 번째)의 문자 출력
    printf("%c\n", s1[4]);    // o: 인덱스 4(다섯 번째)의 문자 출력
    printf("%c\n", s1[5]);    // 문자열 맨 뒤의 NULL(\0) 출력. NULL은 화면에 표시되지 않음

    return 0;
}

일단 문자열은 포인터로도 사용할 수 있고, 배열로도 사용할 수 있다는 점만 기억하면 됩니다.
%s 을 %c대신 쓴다!!




입력 값을 배열에 할당하는 경우 or 포인터에 할당하는 경우 하는짓이 약간 다르다.

입력 값을 문자열 포인터에 저장하려면 문자열이 들어갈 공간을 따로 마련해야 됩니다. 따라서 다음과 같이 malloc 함수로 메모리를 할당한 뒤 문자열을 저장합니다.

// 배열의 경우
#define _CRT_SECURE_NO_WARNINGS // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main()
{
    char s1[10];    // 크기가 10인 char형 배열을 선언

    printf("문자열을 입력하세요: ");
    scanf("%s", s1);     // 표준 입력을 받아서 배열 형태의 문자열에 저장

    printf("%s\n", s1);  // 문자열의 내용을 출력

    return 0;
}



// 포인터의 경우
#define _CRT_SECURE_NO_WARNINGS     // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
#include <stdlib.h>    // malloc, free 함수가 선언된 헤더 파일

int main()
{
    char *s1 = malloc(sizeof(char) * 10);    // char 10개 크기만큼 동적 메모리 할당

    printf("문자열을 입력하세요: ");
    scanf("%s", s1);      // 표준 입력을 받아서 메모리가 할당된 문자열 포인터에 저장

    printf("%s\n", s1);   // 문자열의 내용을 출력

    free(s1);    // 동적 메모리 해제

    return 0;
}

// 참고
char s1[30];

printf("문자열을 입력하세요: ");
scanf("%[^\n]s", s1);    // 공백까지 포함하여 문자열 입력받기

printf("%s\n", s1);

//차이점
char *s1 = "Hello";       // 문자열 포인터에 문자열 리터럴 할당(읽기 전용 메모리를 가리킴)
s1[0] = 'A';              // 실행 에러: 문자를 변경할 수 없음 ★메모리는 읽기 전용이란다! 포인터에 뭘 쓸려면 malloc으로 꼭 할당해줘야댐

char s2[10] = "Hello";    // 문자 배열에 문자열 리터럴 할당(배열에 문자열이 복사됨)
s1[0] = 'A';              // 문자를 변경할 수 있음 