using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{

    private Animator animat;

    public Rigidbody2D rb;
    public SpriteRenderer spriteRenderer;

    float moveInput = 0;
    public int jumpForce = 4;
    public int speed = 4;
    public bool facingRight = true;

    public bool isGrounded = false;

    public LayerMask whatIsGround;

    public bool jumpNow = false;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        spriteRenderer = GetComponent<SpriteRenderer>();
        animat = GetComponent<Animator>();
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space) && isGrounded)
        {
            jumpNow = true; 
        }
    }


    void FixedUpdate()
    {
        if (jumpNow)
        {
            jumpNow = false;
            isGrounded = false;
            rb.velocity = Vector2.up * jumpForce;
        }
        else
        {
            isGrounded = Physics2D.OverlapArea(new Vector2(transform.position.x - 0.5f, transform.position.y - 0.5f),
                                               new Vector2(transform.position.x + 0.5f, transform.position.y - 0.51f), whatIsGround);
        }

        moveInput = Input.GetAxisRaw("Horizontal");
        if (moveInput == 1)
        {
            facingRight = true;
        }
        else if (moveInput == -1)
        {
            facingRight = false;
        }

        spriteRenderer.flipX = !facingRight;
        rb.velocity = new Vector2(moveInput * speed, rb.velocity.y);
    }
}
