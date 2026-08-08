// Base And Power example
#include<stdio.h>
int main(){
    int base,power;
    printf("Enter The Base:");
    scanf("%d",&base);
    printf("Enter The Power:");
    scanf("%d",&power);
    int result=1, sum=0;

    for(int i=1; i<=power;i++){

        result=base*result;//5
    }
    printf("%d", result);

}