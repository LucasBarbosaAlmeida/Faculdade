using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerMusica : MonoBehaviour
{

    public GameObject MusicaToca;
    public GameObject MusicaPara;

    void Update(){

    }

     void OnTriggerEnter2D (Collider2D col){
        if(col.gameObject.tag == "Player"){
            MusicaPara.SetActive(false);
            MusicaToca.SetActive(true);
        }
    }
}
