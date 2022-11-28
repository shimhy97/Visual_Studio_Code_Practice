#define _CRT_SECURE_NO_WARNINGS    // strcpy 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
#include <string.h>    // strcpy 함수가 선언된 헤더 파일

struct Person {   // 구조체 정의
    char name[20];        // 구조체 멤버 1
    int age;              // 구조체 멤버 2
    char address[100];    // 구조체 멤버 3
};

int main()
{
    struct Person p1;     // 구조체 변수 선언

    // 점으로 구조체 멤버에 접근하여 값 할당
    strcpy(p1.name, "홍길동");
    p1.age = 30;
    strcpy(p1.address, "서울시 용산구 한남동");

    // 점으로 구조체 멤버에 접근하여 값 출력
    printf("이름: %s\n", p1.name);       // 이름: 홍길동
    printf("나이: %d\n", p1.age);        // 나이: 30
    printf("주소: %s\n", p1.address);    // 주소: 서울시 용산구 한남동

    return 0;
}



먼저 struct Person *p1과 같이 struct 키워드와 구조체 이름을 사용하여 구조체 포인터를 선언합니다. 이때 일반 변수가 아닌 포인터 변수이므로 반드시 *을 붙입니다. 그리고 malloc 함수로 메모리를 할당할 때 크기를 알아야 하므로 sizeof(struct Person)과 같이 구조체 크기를 구하여 넣어줍니다.

struct Person *p1 = malloc(sizeof(struct Person));    // 구조체 포인터 선언, 메모리 할당
다소 문법이 복잡하지만 구조체 이름 앞에는 반드시 struct 키워드를 붙여야 한다는 점만 기억하면 쉽습니다. 즉, 포인터를 선언할 때도, sizeof로 크기를 구할 때도 struct 키워드를 넣어줍니다.


구조체 별칭을 사용하면, 포인터에 메모리 할당할때 struct를 안붙여도 됨. 왜? 이미 별칭이 struct인걸 알고 있으니깐.