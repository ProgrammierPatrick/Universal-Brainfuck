#include <stdio.h>

// this file needs the size and pos flag
#brainfuck flags

#define PAS 
#define INC ++*ptr;
#define DEC --*ptr;
#define MVR ++ptr;
#define MVL --ptr;
#define SOL while(*ptr){
#define EOL }
#define PTC putchar(*ptr);
#define GTC *ptr=getchar();

#ifdef pbrain
    typedef void (*function)(char*,void*);
    #define RUN funcs[*ptr](ptr, funcs);
    #define SOP funcs[*ptr] = [](char* ptr, void* x){function* funcs = (function*) x;
    #define EOP };
    void null(char* ptr, void* x){}
#endif

int main(){
    char array[size]={0};
    char *ptr=array+pos;
    #ifdef pbrain
        function funcs[256];
        for(unsigned int i = 0; i < 256; ++i){
            funcs[i]=null;
        }
    #endif
    #brainfuck code
    putchar('\n');
}
