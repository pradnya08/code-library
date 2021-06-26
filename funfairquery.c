// https://www.hackerrank.com/contests/week-of-array-query/challenges/fun-fair-queries/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int min(int shops[],int si, int ei){

int Smallest = 999999999;
  for(int i=si; i<=ei; i++)
   {
    if( shops[i] < Smallest )
     {
       Smallest = shops[i];
     }
   }
   return Smallest;
}

int main() {
    int a,b;
    int c,d;
    scanf("%d %d",&a,&b);


    int shops[a];
    for(int j =0; j<a;j++){
        scanf("%d",&shops[j]);
     }
    int size= 2*b;
     int arr[size];

    if(a>b){

			for(int i=0;i<size - 1;i+=2){
						scanf("%d %d",&arr[i], &arr[i+1]);
			}
    }
for (int k=0;k<size - 1;k+=2){
    int res = min(shops, arr[k], arr[k+1]);
    printf("%d\n",res);
}
}