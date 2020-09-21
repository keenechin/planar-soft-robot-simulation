#include<raylib.h>
#include<iostream>
#include<string>

using std::cout;
using std::endl;
using std::cin;

int main(int argc, char *argv[]){

	int screenWidth = 640;
	int screenHeight = 480;
	InitWindow(screenWidth, screenHeight, "simulation window");
	SetTargetFPS(60);
	while (!WindowShouldClose())
	{
		BeginDrawing();
		ClearBackground(BLACK);
		DrawText("Simulation output goes here.", 190, 200, 20, LIGHTGRAY);
		EndDrawing();
	}

	CloseWindow();

	return 0;	
}

	
