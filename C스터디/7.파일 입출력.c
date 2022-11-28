#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    char name[31];
    int order;

    scanf("%s %d", name, &order);

    FILE *fp = stdout;

    fprintf(stdout, "The %dth Satellite of Jupiter: %s", order, name);

    fclose(fp);

    return 0;
}




// 서식지정ㅇ
// fprintf
// 서식지정x
// fputs
// fwrite


// 서식지정ㅇ
// fscanf
// 서식지정x
// fgets
// fread


//fseek
//ftell
//feof feof(파일포인터);
int feof(FILE *_Stream);
파일의 끝이면 1, 끝이 아니면 0을 반환

//Null이 들어갈 공간까지 반환!!!!

//71.8 이해안됨