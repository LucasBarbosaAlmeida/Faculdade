using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class Player : MonoBehaviour
{
    public int objects = 0;
    public Transform waterTransform;

    public GameObject grabShotgunPanel;
    public GameObject shotgun;

    public GameObject grabSwordPanel;
    public GameObject Sword;

    [SerializeField]
    private int lives = 1;

    //private bool canGrab=false;

    void Start(){
        grabShotgunPanel.SetActive(false);
        shotgun.SetActive(false);
        grabSwordPanel.SetActive(false);
        Sword.SetActive(false);
    }

    void Update(){
        if(transform.position.y < waterTransform.position.y)
            RenderSettings.fog = true;
        else    
           RenderSettings.fog = false; 
    }

    public void TakeDamage(){
        lives--;
        if(lives <=0){
            SceneManager.LoadScene(1);
        }
    }
    
    void OnTriggerEnter(Collider other){
        if(other.gameObject.tag == "Collectible"){
            //objects = objects+1;
            //objects += 1;
            objects++;
            Destroy(other.gameObject);
        } 
        if(other.gameObject.tag == "Gun"){
            grabShotgunPanel.SetActive(true);
            grabShotgunPanel.GetComponentInChildren<Text>().text = "Pressione 'E' para pegar";
            //canGrab=true;
        }    
            if(other.gameObject.tag == "Sword"){
            grabSwordPanel.SetActive(true);
            grabSwordPanel.GetComponentInChildren<Text>().text = "Pressione 'E' para pegar";
            //canGrab=true;
        } 
    }

    void OnTriggerExit(Collider other){
            if (other.gameObject.tag == "Gun")
            {
                grabShotgunPanel.SetActive(false);
                //canGrab = false;
            }
        }
            void OnTriggerExitt(Collider other){
        if(other.gameObject.tag == "Sword"){
            grabSwordPanel.SetActive(false);
            //canGrab = false;
        }
    }

    void OnTriggerStay(Collider other){
        if(other.gameObject.tag == "Gun"){
            if(Input.GetKeyDown(KeyCode.E)){
                Destroy(other.gameObject);
                grabShotgunPanel.SetActive(false);
                shotgun.SetActive(true);
            }
        }
    }
            
    void OnTriggerStayy(Collider other){
        if(other.gameObject.tag == "Sword"){
            if(Input.GetKeyDown(KeyCode.E)){
                Destroy(other.gameObject);
                grabSwordPanel.SetActive(false);
                Sword.SetActive(true);
            }
        }
    }
}
