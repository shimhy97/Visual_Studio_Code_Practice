#include <stdio.h>

int main()
{
    int numArr[10] = { 0, };      // 배열의 요소를 모두 0으로 초기화

    printf("%d\n", numArr[0]);    // 0: 배열의 첫 번째(인덱스 0) 요소 출력
    printf("%d\n", numArr[5]);    // 0: 배열의 여섯 번째(인덱스 5) 요소 출력
    printf("%d\n", numArr[9]);    // 0: 배열의 열 번째(인덱스 9) 요소 출력

    return 0;
}

// 배열의 크기를 알아서 구하려면?
#include <stdio.h>

int main()
{
    int numArr[10] = { 11, 22, 33, 44, 55, 66, 77, 88, 99, 110 };    // 크기가 10인 int형 배열

    printf("%d\n", sizeof(numArr));                  // 40: 4바이트 크기의 요소가 10개이므로 40
    printf("%d\n", sizeof(numArr) / sizeof(int));    // 10: 배열의 크기를 구할 때는
                                                     // 전체 공간을 요소의 크기로 나눠줌

    return 0;
}

C 언어는 인덱스가 배열의 범위를 벗어났는지 검사하지 않으므로 프로그래머가 항상 이 부분을 생각하면서 작성해야 합니다. 
배열의 크기(요소 개수)를 구해놓고, 배열에 접근하기 전에 인덱스가 요소 개수 - 1을 넘지 않는지 확인하는 것도 좋은 방법입니다.

int numArr[10];    // 요소가 10개인 배열
int index = 10;    // 배열의 범위를 벗어나는 인덱스
int count = sizeof(numArr) / sizeof(int);    // 배열의 크기(요소의 개수)를 구함

if (index <= count - 1)    // 인덱스가 count - 1보다 작거나 같으면 배열의 범위를 벗어나지 않았음
{
    numArr[index] = 999;
}

  int col = sizeof(numArr[0]) / sizeof(int);    // 4: 2차원 배열의 가로 크기를 구할 때는 
                                                  // 가로 한 줄의 크기를 요소의 크기로 나눠줌

    int row = sizeof(numArr) / sizeof(numArr[0]); // 3: 2차원 배열의 세로 크기를 구할 때는 
                                    // 배열이 차지하는 전체 공간을 가로 한 줄의 크기로 나눠줌


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