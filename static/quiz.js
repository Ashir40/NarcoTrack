const quizDB = [
  {
    question: "Q1: How often do you use drugs other than alcohol?",
    a: "Never",
    b: "Monthly or less",
    c: "2 to 4 times a month",
    d: "2 to 3 times a week",
    e: "4 or more times a week",
  },
  {
    question: "Q2: Do you use more than one type of drug on the same occasion?",
    a: "Never",
    b: "Monthly or less",
    c: "2 to 4 times a week",
    d: "2 to 3 times a week",
    e: "4 or more times a week",
  },
  {
    question: "Q3: How many times do you take drugs on a typical day when you use drugs?",
    a: "None",
    b: "1-2 times",
    c: "3-4 times",
    d: "5-6 times",
    e: "7 or more",
  },
  {
    question: "Q4: How often are you influenced heavily by drugs?",
    a: "Never",
    b: "Less than monthly",
    c: "Monthly",
    d: "Weekly",
    e: "Daily or almost daily",
  },
  {
    question: "Q5: Over the past year, have you felt that your longing for drugs was so strong that you could not resist it?",
    a: "Never",
    b: "Less than monthly",
    c: "Monthly",
    d: "Weekly",
    e: "Daily or almost daily",
  },
  {
    question: "Q6: Has it happened, over the past year, that you have not been able to stop taking drugs once you started?",
    a: "Never",
    b: "Less than monthly",
    c: "Monthly",
    d: "Weekly",
    e: "Daily or almost daily",
  },
  {
    question: "Q7: How often over the past year have you taken drugs and then neglected to do something you should have done?",
    a: "Never",
    b: "Less than monthly",
    c: "Monthly",
    d: "Weekly",
    e: "Daily or almost daily",
  },
  {
    question: "Q8: How often over the past year have you needed to take a drug the morning after heavy drug use the day before?",
    a: "Never",
    b: "Less than monthly",
    c: "Monthly",
    d: "Weekly",
    e: "Daily or almost daily",
  },
  {
    question: "Q9: How often over the past year have you had guilt feelings or a bad conscience because you used drugs?",
    a: "Never",
    b: "Less than monthly",
    c: "Monthly",
    d: "Weekly",
    e: "Daily or almost daily",
  },
  {
    question: "Q10: Have you or anyone else been hurt (mentally or physically) because you used drugs?",
    a: "No",
    b: "Not much",
    c: "Yes, but not in the last year",
    d: "Yes, during the last year",
    e: "Yes, during last week",
  },
  {
    question: "Q11: Has a relative or a friend, a doctor or a nurse, or anyone else, been worried about your drug use or said to you that you should stop using drugs?",
    a: "No",
    b: "Not much",
    c: "Yes, but not in the last year",
    d: "Yes, during the last year",
    e: "Yes, during last week",
  },
];

const question = document.querySelector(".question");
const options1 = document.querySelector("#option1");
const options2 = document.querySelector("#option2");
const options3 = document.querySelector("#option3");
const options4 = document.querySelector("#option4");
const options5 = document.querySelector("#option5");
const submit = document.querySelector("#submit");

const answers = document.querySelectorAll(".ans");

const showscore = document.querySelector("#showscore");

let questionCount = 0;
let score = 0;
const loadQuestion = () => {
  const questionList = quizDB[questionCount];

  question.innerText = questionList.question;
  options1.innerText = questionList.a;
  options2.innerText = questionList.b;
  options3.innerText = questionList.c;
  options4.innerText = questionList.d;
  options5.innerText = questionList.e;
};
loadQuestion();

const getChecked = () => {
  let answer;

  answers.forEach((curAnsElem) => {
    if (curAnsElem.checked) {
      answer = curAnsElem.value;
    }
  });
  return answer;
};

const deselectall = () => {
  answers.forEach((curAnsElem) => (curAnsElem.checked = false));
};

let result = [];
submit.addEventListener("click", () => {
  const checkedAnswer = getChecked();
  console.log(checkedAnswer);

  result = [...result, Number(checkedAnswer)];
  if (questionCount == 10) {
    var sum = 0;
    for (var i = 0; i < result.length; i++) {
      sum += result[i];
    }
    var cmnt="";
  
  if (sum < 10) {
    cmnt ="Your addiction level is moderate.";
  } else if (sum >= 10 && sum < 20) {
    
    cmnt="Your addiction level need some care.";
  }  
  else if (sum >= 20 && sum < 30) {
    
    cmnt="Your addiction level need good care.";
  }
  else if (sum >= 30 && sum < 40) {
    
    cmnt="Your addiction level need serious care.";
  }
  else if (sum >=40 && sum <=50){
  
    cmnt="You are at an emergency state and need help ASAP!";
  }
  else {
    cmnt="Please solve it correctly";
  }
      
    console.log(sum);
  }

  if (checkedAnswer == quizDB[questionCount].ans) {
    score++;
  }

  questionCount++;

  deselectall();

  if (questionCount < quizDB.length) {
    loadQuestion();
  } else {
    showscore.innerHTML = `
            <h3> Your Score ${sum} <br>${cmnt}  </h3>
            <button class="btn" onclick="location.reload()" > Test Again </button>
        `;
    showscore.classList.remove("scorearea");
  }
});
