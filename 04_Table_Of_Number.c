#include<stdio.h>
int main(){
    int num;
    printf("Enter Number To Print Table:");
    scanf("%d",&num);

    for(int i=1; i<=10; i++){
        int table= i*num;
        printf("%d * %d ==> %d\n", i,num,table);

    }
}