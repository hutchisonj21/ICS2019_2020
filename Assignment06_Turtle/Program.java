/**
 * 
 * This program draws a polygon with a number of sides that the user inputs
 * 
 * @author Jayden Hutchison
 * @version 1.0
 * @since 9/18/19
 * 
 **/

import java.util.Scanner;

public class Program
{
	public static void main(String[] args)
	{
		Scanner keyboard = new Scanner(System.in);
		int sides;
		
		//Explains program and asks user for a number of sides
		System.out.println("Hello, this is a program that will draw a polygon based on the number of sides that you input.");
		System.out.println("How many sides would you like the polygon to have?");
		sides = keyboard.nextInt();
		
		//Counter
		int n = sides;
		
		//Calculates the measure of each outside angle
		int outerAngle = 360 / sides;
		

		//Sets up turtle
		Turtle bob = new Turtle();
		
		
		drawPolygon(bob, sides, n, outerAngle);
		//Calls polygon method
		
	}
	
	//Draws the polygon using recursion
	public static void drawPolygon(Turtle bob, int sides, int n, int outerAngle)
	{
		//Moves turtle
		bob.forward(50);
		bob.left(outerAngle);
		bob.forward(50);
		
		n -= 1;
		
		//Uses recursion until the counter reaches 0
		if (n != 0) {
			drawPolygon(bob, sides, n, outerAngle);
		}
	}
}
