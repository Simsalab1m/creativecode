let a = 0.0;
let s = 0.0;
let rad = 10; // Width of the shape
let xpos, ypos; // Starting position of shape


let xspeed = 6.5; // Speed of the shape
let yspeed = 8.4; // Speed of the shape

let xdirection = 1; // Left or Right
let ydirection = 1; // Top to Bottom

function setup() {
  createCanvas(windowWidth, windowHeight)
  //createCanvas(600, 600);
  noStroke();
  frameRate(60);
  ellipseMode(RADIUS);
  // Set the starting position of the shape
  xpos = width / 2;
  ypos = height / 2;
  ellipseMode(CENTER)
}

function draw() {
  background(0, 0, 0, 0);

  // Update the position of the shape
  xpos = xpos + xspeed * xdirection;
  ypos = ypos + yspeed * ydirection;

  //Slowly increase 'a' and then animate 's' with
  //a smooth cyclical motion by finding the cosine of 'a'
  a = a + .001;
  s = cos(a) * 1;
  //https://p5js.org/examples/transform-scale.html


  // Test to see if the shape exceeds the boundaries of the screen
  // If it does, reverse its direction by multiplying by -1
  if (xpos > width - rad || xpos < rad) {
    xdirection *= -1;
    //fill(random(0,255) , random(0,255),random(0,255))
  }
  if (ypos > height - rad || ypos < rad) {
    ydirection *= -1;
  }

  // Draw the shape
  noStroke();
  translate(width / 2, height / 2);
  scale(s);
  fill(51);
  fill(random(0, 100), random(0, 255), random(0, 255))
  ellipse(xpos, ypos, rad + 15, rad + 15);
  fill(random(0, 255), random(0, 100), random(0, 255))
  ellipse(-xpos, -ypos, rad + 15, rad + 15);
  fill(random(0, 255), random(0, 255), random(0, 100))
  ellipse(xpos, -ypos, rad + 15, rad + 15);
  fill(random(100, 255), random(100, 255), random(100, 255))
  ellipse(-xpos, ypos, rad + 15, rad + 15);

  //ellipse(width / height, height / width, rad + 15, rad + 15);
}
