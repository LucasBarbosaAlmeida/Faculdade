using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class PlayerMove : MonoBehaviour
{

    public static bool vivo = true;
    public Animator anim;
    public static bool podeMover=true;
    public SpriteRenderer Sprite;
    public bool NoChao = true;
    public GameObject GameOver;

    public GameObject Inimigos;
    public GameObject CanvasFim;

    // Start is called before the first frame update
    void Start()
    {
        vivo = true;
        anim = GetComponent<Animator>();
        anim.SetBool("Parado", true);
        anim.SetBool("Correndo", false);
        anim.SetBool("Pulando", false);
    }

    void FixedUpdate(){
        	if (podeMover == true) {
			if (Input.GetKey (KeyCode.UpArrow) || Input.GetKey (KeyCode.W) || Input.GetKey (KeyCode.Space)) {
				transform.Translate (new Vector3 (0, 7.5f * Time.deltaTime, 0), Space.Self);
                anim.SetBool("Correndo", false);
                anim.SetBool("Parado", false);
                anim.SetBool("Pulando", true);
                    if (Input.GetKey (KeyCode.LeftArrow) || Input.GetKey (KeyCode.A)) {
				transform.Translate (new Vector3 (-5f * Time.deltaTime, 0, 0), Space.Self);
                Sprite.flipX = true;
                    }
                    if (Input.GetKey (KeyCode.RightArrow) || Input.GetKey (KeyCode.D)) {
				transform.Translate (new Vector3 (5f * Time.deltaTime, 0, 0), Space.Self);
                Sprite.flipX = false;
                    }
			}
            else if (Input.GetKey (KeyCode.LeftArrow) || Input.GetKey (KeyCode.A)) {
				transform.Translate (new Vector3 (-5f * Time.deltaTime, 0, 0), Space.Self);
                Sprite.flipX = true;
                anim.SetBool("Pulando", false);
				anim.SetBool("Parado", false);
                if(NoChao == true){
                    anim.SetBool("Correndo", true);
                }
			}
            else if (Input.GetKey (KeyCode.RightArrow) || Input.GetKey (KeyCode.D)) {
				transform.Translate (new Vector3 (5f * Time.deltaTime, 0, 0), Space.Self);
                Sprite.flipX = false;
                anim.SetBool("Pulando", false);
				anim.SetBool("Parado", false);
                if(NoChao == true){
                anim.SetBool("Correndo", true);
                } 
			} else {
                anim.SetBool("Correndo", false);
                anim.SetBool("Pulando", false);
				anim.SetBool("Parado", true);
            }
		if (podeMover == false) {
                anim.SetBool("Parado", true);
		}
    }

}

        void OnCollisionExit2D (Collision2D col) {
		if (col.gameObject.tag == "chao")
        {
            NoChao = false;
            
        }
        if (col.gameObject.tag == "chaoConcreto")
        {
            NoChao = false;
        }
        }

        void OnCollisionEnter2D (Collision2D col){
            if (col.gameObject.tag == "chao" )
        {
            NoChao = true;
        }
        if (col.gameObject.tag == "chaoConcreto")
        {
            NoChao = true;
        }

        if (col.gameObject.tag == "Inimigo"){
            Time.timeScale = 0f;
            GameOver.SetActive(true);
            vivo = false;
        }

        if(col.gameObject.tag == "cristal"){
            Destroy(GameObject.FindWithTag("cristal"));
            CanvasFim.SetActive(true);
            Inimigos.SetActive(false);
        }
}
}
