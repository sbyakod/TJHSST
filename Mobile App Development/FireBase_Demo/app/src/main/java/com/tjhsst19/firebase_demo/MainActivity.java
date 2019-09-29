package com.tjhsst19.firebase_demo;

import android.support.v7.app.AppCompatActivity;
import java.util.Collections;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {

    private EditText mInput;
    private Button mSendButton, mRetrieveButton;
    private TextView mResult;
    // Write a message to the database
    private FirebaseDatabase database;
    private DatabaseReference myRef;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        database = FirebaseDatabase.getInstance();
        myRef = database.getReference("message");

        mInput = (EditText)findViewById(R.id.input);
        mSendButton = (Button)findViewById(R.id.send_button);
        mRetrieveButton = (Button)findViewById(R.id.retrieve_button);
        mResult = (TextView)findViewById(R.id.result);

        mSendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                myRef.setValue(mInput.getText().toString());
            }
        });

        mRetrieveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });

        // Read from the database
        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                // This method is called once with the initial value and again
                // whenever data at this location is updated.
                String value = dataSnapshot.getValue(String.class);
                mResult.setText(value);
            }

            @Override
            public void onCancelled(DatabaseError error) {
                // Failed to read value
                //Log.w('TAG', "Failed to read value.", error.toException());
            }
        });
    }
}