package com.tjhsst19.geoquiz_sb;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import java.util.Collections;
import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;

public class Endgame extends AppCompatActivity {
    public static final String mFileName = "PrefsFile";
    public static final String mHighScoreKey = "HighScoreKey";
    private int mScore;
    private int mHighScore;
    private int mGlobalHighScore;
    private TextView mScoreTextView;
    private TextView mLocalHighScoreTextView, mGlobalHighScoreTextView;
    private Button mStartOverButton;
    private SharedPreferences sharedPreferences;

    private FirebaseDatabase database;
    private DatabaseReference myRef;

    private ArrayList<Integer> leaderboard = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_endgame);

        mScore = getIntent().getIntExtra("SCORE", 0);

        sharedPreferences = getSharedPreferences(mFileName, Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        database = FirebaseDatabase.getInstance();
        myRef = database.getReference("high_score");

        if(sharedPreferences.contains(mHighScoreKey)){
            mHighScore = sharedPreferences.getInt(mHighScoreKey, 0);
            myRef.setValue(mHighScore);
        }

        if(mScore > mHighScore){
            myRef.setValue(mScore);
            editor.putInt(mHighScoreKey, mScore);
            editor.commit();
        }

        mScoreTextView = (TextView) findViewById(R.id.score_text_view);
        mScoreTextView.setText("Score: " + mScore);
        mLocalHighScoreTextView = (TextView) findViewById(R.id.local_high_score_text_view);
        mLocalHighScoreTextView.setText("Local High Score: " + sharedPreferences.getInt(mHighScoreKey, 0));
        mGlobalHighScoreTextView = (TextView) findViewById(R.id.global_high_score_text_view);
        //mGlobalHighScoreTextView.setText("Leaderboard (1st Place): " + mGlobalHighScore);

        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                // This method is called once with the initial value and again
                // whenever data at this location is updated.
                mGlobalHighScore = dataSnapshot.getValue(Integer.class);
                mGlobalHighScoreTextView.setText("Leaderboard (1st Place): " + mGlobalHighScore);
            }
            @Override
            public void onCancelled(DatabaseError error) {
                // Failed to read value
                //Log.w(TAG, "Failed to read value.", error.toException());
            }
        });

        mStartOverButton = (Button) findViewById(R.id.start_over_answer_button);
        mStartOverButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(Endgame.this, MainActivity.class);
                startActivity(i);
            }
        });
    }
}
