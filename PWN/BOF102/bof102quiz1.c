#include <stdio.h>
#include <string.h>

void callme(unsigned int arg1) {
     if(arg1 == 0xcafebabe) {
           puts("Congratulation!");
     } else {
         puts("Try again.");
     }
}

void bofme() {
    char payload[16];
    puts("Call 'callme' with arg as 0xcafebabe.");
    printf("Payload > ");
    scanf("%s", payload);
    puts("bye.");
}

int main() {
    bofme();
    return 0;
 }
