package com.example.outfitpicker;

import android.content.Intent;
import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.lang.reflect.Array;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.AuthFailureError;
import android.widget.Toast;

import org.json.JSONObject;
import org.json.JSONException;


public class AddActivity extends AppCompatActivity {
    EditText nameInput;
    EditText colourInput;
    TextView output;

    Spinner typeSpinner;

    Button submitButton;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        typeSpinner = findViewById(R.id.typeSpinner);

        nameInput = findViewById(R.id.nameInput);
        colourInput = findViewById(R.id.colourInput);

        output = findViewById(R.id.message);

        final RequestQueue requestQueue = Volley.newRequestQueue(this);

        //imageButton = findViewById(R.id.imageButton);


        submitButton = (Button)findViewById(R.id.submit_add);
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.e("Json: ", "hello");
                String name = nameInput.getText().toString();
                String colour = colourInput.getText().toString();
                String type = typeSpinner.getSelectedItem().toString();

                output.setText("The " + colour + " " + name + " was added!");
                nameInput.setText("");
                colourInput.setText("");

                JSONObject addInfo = new JSONObject();
                try {
                    addInfo.put("name", name);
                    addInfo.put("colour", colour);
                    addInfo.put("clothing_type", type);
                } catch(JSONException e){
                    e.printStackTrace();
                }


                //String jsonString = addInfo.toString();
                String url = "http://10.0.2.2:8000/closet/add_clothing_item";
                JsonObjectRequest stringRequest = new JsonObjectRequest(
                        Request.Method.POST,
                        url,
                        addInfo,
                        new Response.Listener<JSONObject>() {
                            @Override
                            public void onResponse(JSONObject response) {
                                Log.e("Rest Response", response.toString());
                                Intent loginIntent = new Intent(AddActivity.this, AddActivity.class);
                                startActivity(loginIntent);
                            }
                        },
                        new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                Log.e("Rest Response", error.toString());
                            }
                        }
                );
                requestQueue.add(stringRequest);
            }
        });
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}