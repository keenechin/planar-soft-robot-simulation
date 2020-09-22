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
     // Define the camera to look into our 3d world
     Camera camera = { 0 };
     camera.position = (Vector3){ 0.0f, 0.0f, 50.0f };
     camera.target = (Vector3){ 0.0f, 0.0f, 0.0f };
     camera.up = (Vector3){ 0.0f, 1.0f, 0.0f };
     camera.fovy = 90.0f;
     camera.type = CAMERA_PERSPECTIVE;

	SetTargetFPS(60);
	
	auto pose = -10.0f;
	float speed = 1;
	
	Vector3 rotation_vector = {0.0f,0.0f,1.0f};
	Mesh mesh = GenMeshCylinder(2.0f, 40.0f, 10);
	Model link = LoadModelFromMesh(mesh);
	Vector3 scale = {1,1,1};
	Vector3 origin = {-37.50f, 0.0f, 0.0f};
	float theta = 0.0f;

	while (!WindowShouldClose())
	{
		theta+=speed;
		BeginDrawing();
		ClearBackground(GRAY);
		DrawText("Simulation output goes here.", 190, 200, 20, LIGHTGRAY);
		BeginMode3D(camera);

    DrawModelWiresEx(link, origin, rotation_vector, theta, scale, MAROON);
		EndMode3D();

		EndDrawing();

	}

	CloseWindow();

	return 0;	
}

	
