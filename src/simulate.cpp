#include<raymath.h>
#include<pch.h>

struct KinematicState
{
	Vector2 node1;
	Vector2 node2; 
	Vector2 node3;
	Vector2 node4;
	Vector2 node5;
};

struct LinkFrame
{
	float angle;
	float length;
}

std::vector<KinematicState> trajectory;


int main(void){
	return 0;
}
