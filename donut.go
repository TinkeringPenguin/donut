package main

import (
	"fmt"
	"math"
	"os"
	"os/signal"
)

func main() {
	// handling ctrl+c to make cursor visible again
	sig := make(chan os.Signal)
	signal.Notify(sig, os.Interrupt)

	var a, b, i, j float64
	var z [1760]float64
	var screen [1760]rune
	fmt.Printf("\x1b[H\x1b[2J")
	fmt.Printf("\x1b[?25l") // disable cursor
	a, b = 0, 0
	for {
		for la := 0; la < 1760; la++ {
			z[la] = 0
		}
		for la := 0; la < 1760; la++ {
			screen[la] = ' '
		}
		for j = 0; 6.28 > j; j += 0.07 {
			for i = 0; 6.28 > i; i += 0.02 {
				sini := math.Sin(i)
				cosj := math.Cos(j)
				sinA := math.Sin(a)
				sinj := math.Sin(j)
				cosA := math.Cos(a)
				cosj2 := cosj + 2
				mess := 1 / (sini*cosj2*sinA +
					sinj*cosA + 5)
				cosi := math.Cos(i)
				cosB := math.Cos(b)
				sinB := math.Sin(b)
				t := sini*cosj2*cosA - sinj*sinA
				x := int(40 + 30*mess*(cosi*cosj2*cosB-t*sinB))
				y := int(12 + 15*mess*(cosi*cosj2*sinB+t*cosB))
				o := x + 80*y
				N := int(8 * ((sinj*sinA-sini*cosj*cosA)*cosB - sini*cosj*sinA -
					sinj*cosA - cosi*cosj*sinB))

				if 22 > y && y > 0 && x > 0 && 80 > x && mess > z[o] {
					z[o] = mess
					if N > 0 {
						screen[o] = rune(".,-~:;=!*#$@"[N])
					} else {
						screen[o] = '.'
					}
				}
			}
		}

		fmt.Printf("\x1b[d")
		for k := 0; 1761 > k; k++ {
			if k%80 == 0 {
				fmt.Printf("%c", 10)
			} else {
				fmt.Printf("%c", screen[k])
			}
		}
		a += 0.04
		b += 0.02

		// handling ctrl+c to make cursor visible again
		go func() {
			<-sig
			fmt.Printf("\x1b[?25h")
			os.Exit(0)
		}()
	}
}
