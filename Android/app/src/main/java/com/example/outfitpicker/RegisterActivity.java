package com.example.outfitpicker;

import android.content.Intent;
import android.os.Bundle;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class RegisterActivity extends AppCompatActivity {
    EditText mTextUsername;
    EditText mTextEmail;
    EditText mTextPassword;
    EditText mTextConfirmPassWord;
    Button mButtonRegister;
    TextView mTextViewLogin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
        final RequestQueue requestQueue = Volley.newRequestQueue(this);

        mTextUsername = (EditText)findViewById(R.id.username);
        mTextEmail = (EditText)findViewById(R.id.email);
        mTextPassword = (EditText)findViewById(R.id.password);
        mTextConfirmPassWord = (EditText)findViewById(R.id.confirmPassword);
        mButtonRegister = (Button)findViewById(R.id.register_button);
        mTextViewLogin = (TextView) findViewById(R.id.login);
        mTextViewLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View View){
                Intent loginIntent = new Intent(RegisterActivity.this, LoginActivity.class);
                startActivity(loginIntent);
            }
        });
        mButtonRegister.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View View) {
                String username = mTextUsername.getText().toString();
                String email = mTextEmail.getText().toString();
                String password = mTextPassword.getText().toString();
                String confirmPassword = mTextConfirmPassWord.getText().toString();
                if (password != confirmPassword) {
                    //show message
                }
                JSONObject registerInfo = new JSONObject();
                try {
                    registerInfo.put("username", username);
                    registerInfo.put("email", email);
                    registerInfo.put("password", password);
                } catch(JSONException e){
                    e.printStackTrace();
                }
                String url = "";
                JsonObjectRequest objectRequest = new JsonObjectRequest(
                        Request.Method.POST,
                        url,
                        registerInfo,
                        new Response.Listener<JSONObject>() {
                            @Override
                            public void onResponse(JSONObject response) {
                                Log.e("Rest Response", response.toString());
                            }
                        },
                        new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                Log.e("Rest Response", error.toString());
                            }
                        }
                );
                requestQueue.add(objectRequest);

            }
        });

    }

}
