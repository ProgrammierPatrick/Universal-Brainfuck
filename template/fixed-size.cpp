#include <stdio.h>

// this file needs the size and pos flag
#brainfuck flags


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

int main(){
    char array[size]={0};
    char *ptr=array+pos;
    #ifdef pbrain
        auto null = [=](char* ptr){};
        function funcs[256];
        for(unsigned int i = 0; i < 256; ++i){
            funcs[i]=null;
        }
    #endif
    #brainfuck code
}
