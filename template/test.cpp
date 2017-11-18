#include <stdio.h>

#define SRT(x) rt##x:
#define GOT(x) goto rt##x;

int main(){
int x=10;
SRT(123)
if (x){
printf("hallo world");
--x;
GOT(123)
}

}
