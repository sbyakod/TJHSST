package com.tjhsst19.geoquiz_sb;

import android.support.v7.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ProgressBar;
import android.os.CountDownTimer;
import android.media.MediaPlayer;
import android.provider.MediaStore;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {
    private Button mTrueButton;
    private Button mFalseButton;
    private Button mNextButton;
    private Button mPreviousButton;
    private Button mHintButton;
    private TextView mQuestionTextView;
    private TextView mTimerTextView;
    private ProgressBar mProgressBar;

    private Question[] mQuestionBank = new Question [] {
            new Question(R.string.Q1, false),
            new Question(R.string.Q2, true),
            new Question(R.string.Q3, false),
            new Question(R.string.Q4, false),
            new Question(R.string.Q5, true),
            new Question(R.string.Q6, true),
            new Question(R.string.Q7, false),
            new Question(R.string.Q8, true),
            new Question(R.string.Q9, false),
            new Question(R.string.Q10, false),
            new Question(R.string.Q11, true),
            new Question(R.string.Q12, true),
            new Question(R.string.Q13, false),
            new Question(R.string.Q14, true),
            new Question(R.string.Q15, false),
            new Question(R.string.Q16, true),
            new Question(R.string.Q17, false),
            new Question(R.string.Q18, true),
            new Question(R.string.Q19, false),
            new Question(R.string.Q20, true),
    };

    private int mCurrentIndex= 0;
    private int mQuestionsAnswered = 0;
    public int mScore = 0;
    private int mProgress = 0;

    private void updateQuestion(){
        mQuestionTextView.setText(mQuestionBank[mCurrentIndex].getTextResId());
    }

    private class MyCountDownTimer extends CountDownTimer {
        public MyCountDownTimer (long startTime, long interval) {
            super(startTime, interval);
        }
        public void onFinish() {
            Intent i = new Intent(MainActivity.this, Endgame.class);
            i.putExtra("SCORE", mScore);
            startActivityForResult(i, 1);
        }
        public void onTick (long millisUntilFinished) {
            mTimerTextView.setText("Time left: " + millisUntilFinished / 1000);
        }
    }

    private void checkAnswer(boolean userPressedTrue) {
        boolean answerIsTrue = mQuestionBank[mCurrentIndex].isAnswerTrue();
        int messageResId = 0;

        if(userPressedTrue == answerIsTrue) {
            mScore += mQuestionBank[mCurrentIndex].getPointValue();
            messageResId = R.string.correct_toast;
        }
        else {
            messageResId = R.string.incorrect_toast;
        }
        Toast.makeText(MainActivity.this, messageResId, Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //inflating an XML element
        mTrueButton =(Button) findViewById(R.id.true_button);
        mFalseButton =(Button) findViewById(R.id.false_button);
        mNextButton = (Button) findViewById(R.id.next_button);
        mPreviousButton = (Button) findViewById(R.id.previous_button);
        mQuestionTextView = (TextView) findViewById(R.id.question_text_view);
        mHintButton = (Button) findViewById(R.id.hint_button);
        updateQuestion();

        mProgressBar = (ProgressBar) findViewById(R.id.progress_bar);
        mProgressBar.setProgress(mProgress);
        final MediaPlayer mNBATheme = MediaPlayer.create(this, R.raw.nba_finals_theme);
        mNBATheme.start();

        mTimerTextView = (TextView) findViewById(R.id.timer_text_view);
        final MyCountDownTimer mTimer = new MyCountDownTimer(150000, 1000);
        mTimer.start();

        mTrueButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkAnswer(true);
            }
        });
        mFalseButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkAnswer(false);
            }
        });
        mNextButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(mQuestionsAnswered >= 19){
                    mNBATheme.stop();
                    mTimer.cancel();
                    Intent i = new Intent(MainActivity.this, Endgame.class);
                    i.putExtra("SCORE", mScore);
                    startActivityForResult(i, 1);
                }
                else {
                    mQuestionsAnswered += 1;
                    mProgress += 5;
                    mProgressBar.setProgress(mProgress);
                    mCurrentIndex = (mCurrentIndex + 1) % mQuestionBank.length;
                    updateQuestion();
                }
            }
        });
        mPreviousButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(mQuestionsAnswered > 0) {
                    mQuestionsAnswered -= 1;
                    mProgress -= 5;
                    mProgressBar.setProgress(mProgress);
                    mCurrentIndex = (mCurrentIndex - 1 + mQuestionBank.length) % mQuestionBank.length;
                    updateQuestion();
                }
            }
        });
        mHintButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mScore -= 4;
                Intent i = new Intent(MainActivity.this, HintActivity.class);
                i.putExtra("REALANSWER", mQuestionBank[mCurrentIndex].isAnswerTrue());
                startActivityForResult(i, 1);
            }
        });
    }
}
