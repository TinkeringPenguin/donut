use std::{f64::consts::PI, io::{self, Write}};

fn main() {
    let mut a = 0.0;
    let mut b = 0.0;
    let mut z = vec![0.0; 1760];
    let mut screen = vec![' '; 1760];
    
    print!("\x1b[2J");
    io::stdout().flush().unwrap();
    
    loop {
        for la in 0..1760 {
            z[la] = 0.0;
        }

        for la in 0..1760 {
            screen[la] = ' ';
        }

        for j in (0..628).map(|x| x as f64 / 100.0) {
            for i in (0..628).map(|x| x as f64 / 100.0) {
                let sini = f64::sin(i);
                let cosj = f64::cos(j);
                let sinA = f64::sin(a);
                let sinj = f64::sin(j);
                let cosA = f64::cos(a);
                let cosj2 = cosj + 2.0;
                let mess = 1.0 / (sini * cosj2 * sinA + sinj * cosA + 5.0);
                let cosi = f64::cos(i);
                let cosB = f64::cos(b);
                let sinB = f64::sin(b);
                let t = sini * cosj2 * cosA - sinj * sinA;

                let x = (40.0 + 30.0 * mess * (cosi * cosj2 * cosB - t * sinB)) as i32;
                let y = (12.0 + 15.0 * mess * (cosi * cosj2 * sinB + t * cosB)) as i32;
                let o = x + 80 * y;
                let N = (8.0 * ((sinj * sinA - sini * cosj * cosA) * cosB - sini * cosj * sinA - sinj * cosA - cosi * cosj * sinB)) as i32;

                if 22 > y && y > 0 && x > 0 && 80 > x && mess > z[o as usize] {
                    z[o as usize] = mess;
                    if N > 0 {
                        screen[o as usize] = vec!['.', ',', '-', '~', ':', ';', '=', '!', '*', '#', '$', '@'][N as usize];
                    } else {
                        screen[o as usize] = '.';
                    }
                }
            }
        }

        print!("\x1b[d");
        io::stdout().flush().unwrap();

        for (k, &ch) in screen.iter().enumerate() {
            if k % 80 == 0 {
                println!();
            } else {
                print!("{}", ch);
            }
        }

        a += 0.04;
        b += 0.02;
    }
}
