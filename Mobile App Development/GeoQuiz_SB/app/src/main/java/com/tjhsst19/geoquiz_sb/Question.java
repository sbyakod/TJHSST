package com.tjhsst19.geoquiz_sb;

public class Question {
    private int mTextResId; //refers to the string
    private boolean mAnswerTrue;
    private int mPointValue = 5;

    public Question(int textResId, boolean answerTrue)
    {
        mTextResId = textResId;
        mAnswerTrue = answerTrue;
    }

    public int getTextResId() {
        return mTextResId;
    }

    public void setTextResId(int textResId) {
        mTextResId = textResId;
    }

    public boolean isAnswerTrue() {
        return mAnswerTrue;
    }

    public void setAnswerTrue(boolean answerTrue) {
        mAnswerTrue = answerTrue;
    }

    public int getPointValue() {
        return mPointValue;
    }
}