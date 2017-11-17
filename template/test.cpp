#include <stdio.h>

#define pbrain

#define INC ++*ptr;
#define DEC --*ptr;
#define MVR ++ptr;
#define MVL --ptr;
#define SOL while(*ptr){
#define EOL }
#define PTC putchar(*ptr);
#define GTC *ptr=getchar();

#ifdef pbrain
    typedef void (*function)(char*);
    #define RUN funcs[*ptr](ptr);
    #define SOP funcs[*ptr] = [=](char* ptr){
    #define EOP };
#endif

#define SIZE 100
#define POS 50

int main(){
    char array[SIZE]={0};
    char *ptr=array+POS;
    #ifdef pbrain
        auto null = [=](char* ptr){};
        function funcs[256];
        for(unsigned int i = 0; i < 256; ++i){
            funcs[i]=null;
        }
    #endif
    printf("SOP\n");
    SOP
    printf("INC\n");
    INC
    printf("PTC\n");
    PTC
    printf("EOP\n");
    EOP
    printf("MVL\n");
    MVL
    printf("GTC\n");
    GTC
    printf("MVR\n");
    MVR
    printf("RUN\n");
    RUN
}
