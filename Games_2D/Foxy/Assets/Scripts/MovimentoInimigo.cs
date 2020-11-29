using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovimentoInimigo : MonoBehaviour {

	[SerializeField]
	Transform[] waypoints;

	[SerializeField]
	float moveSpeed;

	int waypointIndex;
	public SpriteRenderer Sprite;
	void Start () {
		transform.position = waypoints [waypointIndex].transform.position;
	}

	void Update () {
		Move ();
	}

	void Move()
	{
		transform.position = Vector3.MoveTowards (transform.position, waypoints[waypointIndex].transform.position, moveSpeed * Time.deltaTime);

		if (transform.position == waypoints [waypointIndex].transform.position) {
			waypointIndex += 1;
		}
			
		if(waypointIndex == 1){
			Sprite.flipX = false;
		}

		if (waypointIndex == waypoints.Length){
			waypointIndex = 0;
			Sprite.flipX = true;
		}
	}
}
