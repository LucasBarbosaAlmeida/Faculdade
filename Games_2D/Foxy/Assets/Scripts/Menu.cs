﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Menu : MonoBehaviour
{
    public void Iniciar(string scene_name){
        SceneManager.LoadScene(scene_name);
    }

    public void Sair(){
        Application.Quit();
    }
}