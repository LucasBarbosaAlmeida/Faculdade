using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ConversaSapo : MonoBehaviour
{
    
    public Animator anim;
    public Canvas texto;
    public AudioSource SomSapo;

    // Start is called before the first frame update
    void Start()
    {
        anim = GetComponent<Animator>();
        texto = GetComponent<Canvas>();
        SomSapo = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnTriggerEnter2D (Collider2D col){
        if(col.gameObject.tag == "Player"){
            texto.enabled = true;
            SomSapo.Play();
            anim.SetBool("Trigger", true);
            anim.SetBool("Trigger", false);
            Debug.Log("Entrou no Tigger Sapo");
            anim.Play("Sapo Parado");
        }
    }

}
