package com.tjhsst19.geoquiz_sb;

import android.content.Intent;
import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class HintActivity extends AppCompatActivity {

    private Button mShowAnswer;
    private TextView mAnswerTextView, mWarningTextView;
    private Boolean mAnswer;
    private boolean mHintGiven = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hint);

        mAnswer = getIntent().getBooleanExtra("REALANSWER", false);

        mWarningTextView = (TextView) findViewById(R.id.warning_text);
        mShowAnswer = (Button) findViewById(R.id.show_answer_button);
        mAnswerTextView = (TextView) findViewById(R.id.answer_text_view);

        mShowAnswer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mHintGiven = true;
                if(mAnswer)
                    mAnswerTextView.setText(R.string.true_button);
                else
                    mAnswerTextView.setText((R.string.false_button));

            }
        });
    }

    @Override
    public void onBackPressed() {
        // call the superclass method first
        Intent returnIntent = getIntent();
        returnIntent.putExtra("result", mHintGiven);
        setResult(1, returnIntent);
        finish();
    }

}