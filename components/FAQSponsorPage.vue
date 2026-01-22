<template>
  <div id="faq" class="section">
    <div class="content-wrapper">
      <div class="faq-text-div">
        <h1>Frequently asked questions</h1>
      </div>
      <div class="faq-contents">
        <div class="Question_Wrapper">
          <div v-for="(questions, i) in [questions_left, questions_right]" :key="i" class="Question_Column">
            <div v-for="(faq, i) in questions" :key="i" class="Question" :faq="faq">
              <button class="Question_Button" :class="{ opened: faq.question === currentOpenedQuestion }"
                @click="toggleButton(faq.question)">
                {{ faq.question }}
              </button>
              <div :class="faq.question === currentOpenedQuestion ? 'Answer_Opened' : 'Answer'" v-html="faq.answer"></div>
            </div>
          </div>
        </div>
      </div>
      <div id="sponsors" class="sponsor-header">
        <div class="sponsor-text-div">
          <h1>Sponsors</h1>
        </div>
      </div>
      <div class="sponsor-logo-container">
        <a 
          v-for="(sponsor, i) in sponsors" 
          :key="i" 
          :href="sponsor.url" 
          target="_blank"
          class="sponsor-card"
        >
          <img :src="sponsor.image" :alt="sponsor.name">
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

interface FAQ {
  question: string;
  answer: string;
}

interface Sponsor {
  name: string;
  amount: number;
  url: string;
  image: string;
}

const questions = ref<FAQ[]>([
  {
    question: 'What is Bitcamp?',
    answer: "Bitcamp is a hackathon that values participant experience and mentorship over competitiveness and points. Come to have fun with your friends, learn something new, eat s'mores, and have a generally awesome time. We have all sorts of crazy activities planned for you...come find out the rest!",
  },
  {
    question: "What's a hackathon?",
    answer: "A hackathon is a creative marathon all about building something cool. Students are encouraged to come up with an idea, form teams, and then build out that idea (typically through programming!) into a product in 36 hours. We want you to take something you love (sports, art, camping, anything!) and combine it with technology to make something awesome. It's a great time to push the envelope and learn some new skills.",
  },
  {
    question: 'Do I have to be experienced to attend?',
    answer: 'No prior experience is required to attend Bitcamp. Exciting workshops and helpful mentors will give you the resources to help you build your dream project. Just come with your head and a willingness to learn!',
  },
  {
    question: "Is it okay if I don't have an idea or team?",
    answer: 'No idea? No team? No problem! There will be dedicated events during Bitcamp for idea creation and team formations.',
  },
  {
    question: "Can I attend if I'm a minor (under 18)?",
    answer: 'Yes! Minors can attend with a chaperone, and can apply <a class="link" href="https://register.bit.camp" target="_blank">here</a>!',
  },
  {
    question: "Can I attend if I don't want to participate in hacking?",
    answer: "Although Bitcamp is a hackathon, there is no requirement to hack if you don't want to. If hacking isn't your thing, you can still participate in our exciting workshops and fun mini-events.",
  },
  {
    question: 'How else can I get involved?',
    answer: "We'd love to get you on our volunteering or mentoring teams! If you'd like to help, please register as a <a class='link' href='https://register.bit.camp/mentor' target='_blank'>mentor</a> or <a class='link' href='https://register.bit.camp/volunteer' target='_blank'>volunteer</a>. Also, be sure to follow us on Facebook and Twitter for updates!",
  },
  {
    question: 'How do I join a team?',
    answer: "Projects are submitted by teams to DevPost. You don't need to finalize your team until project submissions are due during the event. You may work individually or in a team of up to four campers. Don't have a team in mind? No problem! Bitcamp will kick off with an optional team formation event.",
  },
  {
    question: 'How competitive is the application process?',
    answer: 'It’s not competitive at all! The application process primarily serves as a way for us to verify application details as they come in. Unless you receive any contact from us (other than the confirmation email), we’ll see you by the campfire!',
  },
  {
    question: 'Who can apply to Bitcamp?',
    answer: 'Any college student, high school student, or middle school student is more than welcome to apply to Bitcamp!',
  },
  {
    question: 'Is Bitcamp free to attend?',
    answer: 'Yes! There is no cost to attend Bitcamp.',
  },
  {
    question: 'Can people not registered for Bitcamp attend?',
    answer: 'People not registered for Bitcamp will not be allowed entrance to the hackathon.',
  },
  {
    question: 'What have people made in the past at Bitcamp?',
    answer: 'From Augmented Reality Human-Scale Pong to a research paper detailing vulnerabilities in Google\'s reCaptcha system, the projects at Bitcamp span across all categories and interests. You can check out all of the amazing submissions at the <a class="link" href="https://bitcamp2024.devpost.com/project-gallery"> Bitcamp 2024 Devpost!</a>',
  },
  {
    question: 'What hardware is provided at Bitcamp?',
    answer: 'Arduinos, sensors (ultrasonic, photoresistors, thermistors), inputs (buttons, switches), outputs (LEDs, piezo speakers, 7-segment displays, micro servo motors), passive components (resistors, capacitors, diodes), and wiring.',
  },
  {
    question: "Does Bitcamp provide travel accomodations or reimbursement?",
    answer: "Due to an unforeseen amount of applications and a limited budget, we unfortunately have closed our reimbursement application process from further interest. However, we will be evaluating reimbursement requests on a case-by-case basis during the weekend of Bitcamp.",
  }, 
]);

const questions_left = questions.value.slice(0, Math.ceil(questions.value.length / 2));
const questions_right = questions.value.slice(Math.ceil(questions.value.length / 2));
const currentOpenedQuestion = ref<string | null>(null);

function toggleButton(question: string) {
  if (currentOpenedQuestion.value === question) {
    currentOpenedQuestion.value = null;
  } else {
    currentOpenedQuestion.value = question;
  }
}

const sponsors: Sponsor[] = Array(12).fill({
  name: "Sponsor",
  image: "",
  amount: -1,
  url: ""
});
</script>

<style scoped lang="scss">
.section {
  flex-shrink: 0;
  position: relative;
}

.content-wrapper {
  width: 100%;
  margin: 0 auto;
  background-color: #03072A;
  position: relative;
  overflow: hidden;
  border-top: 1px solid #000;  
  text-align: left;

  &::after {
    content: '';
    position: absolute;
    top: clamp(-1000px, -110vh, -500px); 
    left: clamp(-2200px, -250vw, -300px);
    width: clamp(1000px, 400vw, 4000px);
    height: clamp(800px, 200vh, 2000px);
    background-image: url('../assets/img/faq/blue-planet.webp');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 0;
    pointer-events: none;
    opacity: 1;

    @media (max-width: 768px) {
      display: none;
    }

  }

  &::before {
    content: '';
    position: absolute;
    right: 0%;
    top: -40vh;
    width: 40vw;
    height: 70vh;
    background-image: url('../assets/img/faq/green-planet.webp');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 0;
    pointer-events: none;
    opacity: 1;

    @media (max-width: 768px) {
      display: none;
    }

  }
}

.faq-text-div {
  margin-top: 5vh;
  font-size: 2vw;
  margin-left: 4.21875vw;
  z-index: 2;
  color: #FFF7EB;
  position: relative;
  text-shadow: 0 0 20px #FFF7EB;
}

.sponsor-logo-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2vw;
  padding: 3rem;
  margin-bottom: 5vh;
  margin-left: 3.5vw;
  margin-right: 3.5vw;
}

.sponsor-card {
  aspect-ratio: 16 / 10;
  background-color: #D3D3D3;
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-family: 'Avenir';
  font-weight: 600;
  font-size: 2vw;
  color: #1A2E33;
  text-decoration: none;
  transition: all 0.3s ease;
  padding: 2rem;
  cursor: pointer;

  img {
    max-width: 80%;
    max-height: 80%;
    object-fit: contain;
  }

  &:hover {
    background-color: #BEBEBE;
    transform: scale(1.05);
    box-shadow: 0 4px 20px rgba(255, 247, 235, 0.3);
  }
}

.sponsor-text-div {
  font-size: 2vw;
  margin-left: 4.21875vw;
  z-index: 2;
  color: #FFF7EB;
  position: relative;
  text-shadow: 0 0 20px #FFF7EB;
}

.faq-contents {
  position: relative;
  font-family: 'Avenir';
  font-style: normal;
  font-weight: 500;
  border-radius: 15px;
  padding: 3vw;
  overflow-y: visible;
  z-index: 10;
  text-align: center;
  min-height: 72vh;
  margin-bottom: 0;
}

.Question_Wrapper {
  display: flex;
  flex-wrap: wrap;
}

.Question_Column {
  flex: 1;
  min-width: 0;

  &:first-child {
    display: flex;
    flex-direction: column;
    &:has(.Question:nth-child(7):last-child) {
      justify-content: flex-start;
    }
  }
}

.Question {
  display: block;
  padding-bottom: 2px;
  padding-left: 10px;
  border-radius: 12px;
  font-family: 'Avenir';
  font-style: normal;
  font-weight: 500;
  color: white;
  width: 96%;
  position: relative;
  background-color: transparent;
  overflow: hidden;
}

.Question_Button {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 1rem;
  border: none;
  background: transparent;
  padding: 3rem 12px 2.8rem;
  text-align: left;
  font-family: 'Avenir';
  font-size: 1.6vw;
  line-height: 1.3;
  font-weight: bold;
  color: white;
  overflow: hidden;
  height: 6vw;
  width: 100%;
  cursor: pointer;

  &::before {
    content: url(../assets/img/icons/plus.svg);
    min-width: 3rem;
    min-height: 3rem;
    max-width: 10rem;
    max-height: 10rem;
    margin-top: 1rem;
    margin-right: 1rem;
    transform: rotateZ(0deg);
    transition: content 0.6s ease;
    flex-shrink: 0;
  }

  &.opened::before {
    content: url(../assets/img/icons/minus.png);
  }
}

.Answer {
  padding: 0px 12px;
  text-align: left;
  font-size: 1.4vw;
  max-height: 0px;
  overflow: hidden;
  transition: max-height 0.6s ease-in-out;
}

.Answer_Opened {
  padding: 0px 12px;
  padding-top: 1rem;
  margin-left: 4.6vw;
  text-align: left;
  font-size: 1.4vw;
  overflow-y: auto;
  transition: max-height 0.6s ease-in-out;
  margin-bottom: 2rem;
}

@media (max-width: 768px) {
  .faq-text-div, .sponsor-text-div {
    font-size: 5vw;
    text-align:left;
    margin-left: 5vw;
  }
  .sponsor-logo-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    padding: 1.5rem;
    margin-left: 1rem;
    margin-right: 1rem;
  }

  .sponsor-card {
    font-size: 4vw;
    padding: 1rem;
  }

  .Question_Column {
    min-width: 100%;
  }

  .Question, .Question_Button {
    font-size: 3vw;
  }

  .Question_Button {
    height: 10vw;
    padding: 2rem 12px 1.75rem;
    &::before {
      min-width: 4rem;
      min-height: 4rem;
    }
  }

  .Answer, .Answer_Opened {
    height: 100%;
    font-size: 2.5vw;
  }
}

@media (min-width: 1200px) {
  .Question_Button::before {
    min-width: 4rem;
    min-height: 4rem;
  }
}

@media (max-width: 1024px) {
  .sponsor-logo-container {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .faq-text-div, .sponsor-text-div {
    font-size: 5vw;
    text-align:left;
    margin-left: 5vw;
  }
  .sponsor-logo-container {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 1.5rem;
    padding: 1.5rem;
    margin-left: 1rem;
    margin-right: 1rem;
  }

  .sponsor-card {
    font-size: 4vw;
    padding: 1rem;
  }

  .Question_Column {
    min-width: 100%;
  }

  .Question, .Question_Button {
    font-size: 3vw;
  }

  .Question_Button {
    height: 10vw;
    padding: 2rem 12px 1.75rem;
    &::before {
      min-width: 4rem;
      min-height: 4rem;
    }
  }

  .Answer, .Answer_Opened {
    height: 100%;
    font-size: 2.5vw;
  }
}

@media (min-width: 1200px) {
  .Question_Button::before {
    min-width: 4rem;
    min-height: 4rem;
  }
}
</style>

<style lang="scss">
a.link {
  color: #6982ac;
}

ul {
  margin-block-start: 1rem;
  margin-block-end: 1rem;
  padding-inline-start: 1rem;
}
</style>