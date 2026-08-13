// Fibo Series
#include<stdio.h>
int main(){

    int i=0,j=1,k;
    for(int l=0; l<=20;l++){
        printf("%d ",i);
        k=i+j;
        i=j;
        j=k;
        
    }
    
}