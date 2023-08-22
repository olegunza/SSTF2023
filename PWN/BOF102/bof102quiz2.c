#include <stdio.h>
#include <string.h>

   char msg[16];
   void bofme() {
     char payload[16];
     printf("Print out '%s'.\n", msg);
     printf("Payload > ");
     scanf("%s", payload);
     puts("bye.");
  }

   int main() {
     strncpy(msg, "Congratulation!", sizeof(msg));
     bofme();
     return 0;
   }
