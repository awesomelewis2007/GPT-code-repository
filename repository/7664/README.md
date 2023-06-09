# Chaos Game Fractal Generator - 7664

**Language**: `Rust`

**Lines of code**: `69`

## Description

This Rust program generates a fractal image using the "Chaos Game" algorithm. The algorithm uses randomness to generate a series of points within a triangle and then iteratively connects those points to create a fractal image. The program takes user inputs for the number of points, the scale of the image, and the colors to be used.

The program takes user inputs for the number of points, scale of the image, and color choice, and generates a fractal image based on those inputs. It uses the rand crate to generate random points within a triangle and then iteratively connects those points to create the fractal image. Finally, the image is saved as a

## Code

``` Rust
extern crate rand;

use image::{ImageBuffer, Rgb};
use rand::prelude::*;
use std::io;

struct Point {
    x: f32,
    y: f32,
}

fn main() {
    let mut num_points = String::new();
    println!("Enter number of points (3-6): ");
    io::stdin()
        .read_line(&mut num_points)
        .expect("Failed to read line");
    let num_points: usize = num_points.trim().parse().unwrap();

    let mut scale = String::new();
    println!("Enter scale of image (1-100): ");
    io::stdin().read_line(&mut scale).expect("Failed to read line");
    let scale: u32 = scale.trim().parse().unwrap();

    let mut color_choice = String::new();
    println!("Enter color choice (1-5): \n1. Red\n2. Green\n3. Blue\n4. Yellow\n5. Purple");
    io::stdin()
        .read_line(&mut color_choice)
        .expect("Failed to read line");
    let color_choice: u8 = color_choice.trim().parse().unwrap();

    let mut points: Vec<Point> = Vec::with_capacity(num_points);
    let mut rng = rand::thread_rng();
    let triangle: [Point; 3] = [
        Point { x: 0.0, y: 0.0 },
        Point { x: (scale * 2) as f32, y: 0.0 },
        Point { x: (scale as f32), y: (scale * 2) as f32 },
    ];

    for _ in 0..num_points {
        points.push(triangle[rng.gen_range(0..3)]);
    }

    let mut imgbuf = ImageBuffer::new(scale * 3, scale * 3);

    let mut curr_point = triangle[rng.gen_range(0..3)];

    for _ in 0..(scale * scale) {
        let chosen_point = points[rng.gen_range(0..num_points)];
        curr_point.x = (curr_point.x + chosen_point.x) / 2.0;
        curr_point.y = (curr_point.y + chosen_point.y) / 2.0;

        let color = match color_choice {
            1 => Rgb([255, 0, 0]),
            2 => Rgb([0, 255, 0]),
            3 => Rgb([0, 0, 255]),
            4 => Rgb([255, 255, 0]),
            _ => Rgb([255, 0, 255]),
        };

        imgbuf.put_pixel(
            (curr_point.x + (scale as f32)) as u32,
            (curr_point.y + (scale as f32)) as u32,
            color,
        );
    }

    imgbuf.save("fractal.png").unwrap();
}

```

## Prompt

```
Make me a program in Rust that is more than 20 lines of code long and is complex and interesting. The program should contain lots of math

Program should be no more than 150 lines of code

When you create the program make a title for it and a short description of what it does.
```