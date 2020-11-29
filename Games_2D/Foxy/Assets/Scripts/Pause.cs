using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Pause : MonoBehaviour
{

    public static bool Pausado = false;
	public GameObject PauseUI;
	public AudioSource Musica1;
    public AudioSource Musica2;


    // Start is called before the first frame update
    void Start()
    {
        Pausado = true;
		Resume();
    }

    // Update is called once per frame
    void Update()
    {
		if(PlayerMove.vivo == true){
        if (Input.GetKeyDown (KeyCode.Escape)) {
			if (Pausado) {
				Resume();
			} 
			else {
				Pausar(true);
			}
		}
		}
    }

    	public void Resume(){
		PauseUI.SetActive(false);
		Time.timeScale = 1f;
		Pausado = false;
		Musica1.UnPause ();
        Musica2.UnPause ();
	}
	public void Pausar(bool menu){
		PauseUI.SetActive(menu);
		Time.timeScale = 0f;
		Pausado = true;
		Musica1.Pause ();
        Musica2.Pause ();
	}
	public void Menu(){
		SceneManager.LoadScene ("Menu");
		PlayerMove.vivo = true;
	}

    	public void Reiniciar(){
		SceneManager.LoadScene ("Game");
		PlayerMove.vivo = true;
		Resume();
	}

}
