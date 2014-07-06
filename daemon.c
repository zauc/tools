#include <stdio.h>


int main()
{
char buf[1024];

        memset(buf,0,1024);

        sprintf(buf,"/bin/bash /home/timo/github/zauc/tools/abc.sh");

        daemon(0,0);

        while(1)
        {
                system(buf);
                sleep(120);
         }
}
