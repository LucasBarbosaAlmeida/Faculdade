using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Parallax : MonoBehaviour
{

    public Transform camera;
    public Transform[] camadas;
    public float[] multiplicador;
    private Vector3[] posiçãoInicial;

    private void Awake()
    {
        posiçãoInicial = new Vector3[camadas.Length];

        for (int i = 0; i < camadas.Length; i++)
        {
            posiçãoInicial[i] = camadas[i].position;
        }
    }

    // Update is called once per frame
    void Update()
    {
        for (int i = 0; i < camadas.Length; i++)
        {
            camadas[i].position = posiçãoInicial[i] + multiplicador[i] * (new Vector3(camera.position.x, camera.position.y, camadas[i].position.z));
        }

    }
}
