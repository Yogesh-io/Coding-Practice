// factor program using for loop
#include<stdio.h>
int main(){
    int num;
    printf("Enter Any Number:");
    scanf("%d",&num);

    for(int i=2; i<num;i++){
        if(num%i==0){
            printf("%d ",i);
        }
    }
}