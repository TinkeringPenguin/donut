int k;
double sin() ,cos();

// main
int main() {
    float a=0, b=0, i, j, z[1760];
    char screen[1760];
    printf("\x1b[2J");
    while (1) {
        // init arrays
        for (int la=0;la<1760;la++) {
            z[la] = 0;
        }
        for (int la=0;la<1760;la++) {
            screen[la] = ' ';
        }
        for(j=0; 6.28>j; j+=0.07) {
            for(i=0; 6.28 >i; i+=0.02) {
                float sini=sin(i),
                      cosj=cos(j),
                      sinA=sin(a),
                      sinj=sin(j),
                      cosA=cos(a),
                      cosj2=cosj+2,
                      mess=1/(sini*cosj2*sinA+sinj*cosA+5),
                      cosi=cos(i),
                      cosB=cos(b),
                      sinB=sin(b),
                      t=sini*cosj2*cosA-sinj* sinA;
                int x=40+30*mess*(cosi*cosj2*cosB-t*sinB),
                    y= 12+15*mess*(cosi*cosj2*sinB +t*cosB),
                    o=x+80*y,
                    N=8*((sinj*sinA-sini*cosj*cosA)*cosB-sini*cosj*sinA-sinj*cosA-cosi *cosj*sinB);

                // debug
                // printf("%d %d %d %d\n",x,y,o,N);
                if(22>y&&y>0&&x>0&&80>x&&mess>z[o]){
                    z[o]=mess;
                    if (N>0) {
                        screen[o] = ".,-~:;=!*#$@"[N];
                    } else {
                        screen[o] = '.';
                    }
                }
            }
        }

        // prints
        printf("\x1b[d");
        for(k=0; 1761>k; k++)
        if (k%80==0) {
            putchar(10);
        } else {
            putchar(screen[k]);
        }
        a+=0.04;
        b+= 0.02;
    }

    return 0;
}
