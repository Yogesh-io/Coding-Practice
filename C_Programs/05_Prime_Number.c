// Prime Number Program

#include<stdio.h>
int main(){
    int num;
    printf("Enter Any Number to Check Prime:");
    scanf("%d",&num);
    int x=0;


    for(int i=2; i<num; i++){
        if(num%i==0){
            x=1;
        }
    }
    if(x==1){
        printf("%d is Not Prime NUmber.", num);
    }
    else{
        printf("%d is Prime NUmber.", num);

    }


}