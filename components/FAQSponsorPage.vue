<template>
  <div id="faq" class="section" ref="containerRef">
    <div class="content-wrapper">
      <div class="faq-text-div">
        <h1>Frequently asked questions</h1>
      </div>
      <div class="faq-contents">
        <div class="Question_Wrapper">
          <div
            v-for="(questions, i) in [questions_left, questions_right]"
            :key="i"
            class="Question_Column"
          >
            <div
              v-for="(faq, i) in questions"
              :key="i"
              class="Question"
              :faq="faq"
            >
              <button
                class="Question_Button"
                :class="{ opened: faq.question === currentOpenedQuestion }"
                @click="toggleButton(faq.question)"
              >
                {{ faq.question }}
              </button>
              <div
                :class="
                  faq.question === currentOpenedQuestion
                    ? 'Answer_Opened'
                    : 'Answer'
                "
                v-html="faq.answer"
              ></div>
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
          <img :src="sponsor.image" :alt="sponsor.name" />
        </a>
      </div>
      <div class="button-wrapper">
        <a
          target="_blank"
          href="https://bit.camp/sponsor"
          class="sponsor-button"
          >BECOME A SPONSOR</a
        >
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick } from "vue";
import { gsap } from "gsap";
import { SplitText } from "gsap/SplitText";
import { ScrollTrigger } from "gsap/ScrollTrigger";

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
    question: "What is Bitcamp?",
    answer:
      "Bitcamp is a hackathon that values participant experience and mentorship over competitiveness and points. Come to have fun with your friends, learn something new, eat s'mores, and have a generally awesome time. We have all sorts of crazy activities planned for you...come find out the rest!",
  },
  {
    question: "What's a hackathon?",
    answer:
      "A hackathon is a creative marathon all about building something cool. Students are encouraged to come up with an idea, form teams, and then build out that idea (typically through programming!) into a product in 36 hours. We want you to take something you love (sports, art, camping, anything!) and combine it with technology to make something awesome. It's a great time to push the envelope and learn some new skills.",
  },
  {
    question: "Do I have to be experienced to attend?",
    answer:
      "No prior experience is required to attend Bitcamp. Exciting workshops and helpful mentors will give you the resources to help you build your dream project. Just come with your head and a willingness to learn!",
  },
  {
    question: "Is it okay if I don't have an idea or team?",
    answer:
      "No idea? No team? No problem! There will be dedicated events during Bitcamp for idea creation and team formations.",
  },
  {
    question: "Can I attend if I'm a minor (under 18)?",
    answer:
      'Yes! Minors can attend with a chaperone, and can apply <a class="link" href="https://register.bit.camp" target="_blank">here</a>!',
  },
  {
    question: "Can I attend if I don't want to participate in hacking?",
    answer:
      "Although Bitcamp is a hackathon, there is no requirement to hack if you don't want to. If hacking isn't your thing, you can still participate in our exciting workshops and fun mini-events.",
  },
  {
    question: "How else can I get involved?",
    answer:
      "We'd love to get you on our volunteering or mentoring teams! If you'd like to help, please register as a <a class='link' href='https://register.bit.camp/mentor' target='_blank'>mentor</a> or <a class='link' href='https://register.bit.camp/volunteer' target='_blank'>volunteer</a>. Also, be sure to follow us on Facebook and Twitter for updates!",
  },
  {
    question: "How do I join a team?",
    answer:
      "Projects are submitted by teams to DevPost. You don't need to finalize your team until project submissions are due during the event. You may work individually or in a team of up to four campers. Don't have a team in mind? No problem! Bitcamp will kick off with an optional team formation event.",
  },
  {
    question: "How competitive is the application process?",
    answer:
      "It's not competitive at all! The application process primarily serves as a way for us to verify application details as they come in. Unless you receive any contact from us (other than the confirmation email), we'll see you by the campfire!",
  },
  {
    question: "Who can apply to Bitcamp?",
    answer:
      "Any college student, high school student, or middle school student is more than welcome to apply to Bitcamp!",
  },
  {
    question: "Is Bitcamp free to attend?",
    answer: "Yes! There is no cost to attend Bitcamp.",
  },
  {
    question: "Can people not registered for Bitcamp attend?",
    answer:
      "People not registered for Bitcamp will not be allowed entrance to the hackathon.",
  },
  {
    question: "What have people made in the past at Bitcamp?",
    answer:
      'From Augmented Reality Human-Scale Pong to a research paper detailing vulnerabilities in Google\'s reCaptcha system, the projects at Bitcamp span across all categories and interests. You can check out all of the amazing submissions at the <a class="link" target="_blank" href="https://bitcamp2025.devpost.com/project-gallery"> Bitcamp 2025 Devpost!</a>',
  },
  {
    question: "What hardware is provided at Bitcamp?",
    answer:
      "Arduinos, sensors (ultrasonic, photoresistors, thermistors), inputs (buttons, switches), outputs (LEDs, piezo speakers, 7-segment displays, micro servo motors), passive components (resistors, capacitors, diodes), and wiring.",
  },
  {
    question:
      "Is travel reimbursement guaranteed, and will I be fully reimbursed?",
    answer:
      "Due to a limited budget, we're unable to guarantee reimbursement, nor can we guarantee full reimbursement on travel expenses. Please do not depend on the travel reimbursement when planning your trip.",
  },
  {
    question: "Where can I access the reimbursement application?",
    answer:
      "We will be sending out the application for travel reimbursement through email for those who expressed interest in the Bitcamp registration form.",
  },
  {
    question: "What kind of transportation is eligible for reimbursement?",
    answer:
      "We will consider reimbursing public transportation, rideshare, and interstate transportation (train/plane). However, it is important to note that due to a limited budget, public transportation is encouraged and is most likely to be reimbursed!",
  },
  {
    question: "When will I hear back about my reimbursement status?",
    answer:
      "You will hear back within 3-4 business days regarding your reimbursement decision.",
  },
  {
    question: "How will I receive my reimbursement?",
    answer:
      "Reimbursements will be provided at the event, and hackers must be present in person to receive the reimbursement.",
  },
  {
    question: "Have other travel questions?",
    answer:
      'Contact <a class="link" href="mailto:travel@bit.camp">travel@bit.camp</a>!',
  },
]);

const questions_left = questions.value.slice(
  0,
  Math.ceil(questions.value.length / 2),
);
const questions_right = questions.value.slice(
  Math.ceil(questions.value.length / 2),
);
const currentOpenedQuestion = ref<string | null>(null);

function toggleButton(question: string) {
  if (currentOpenedQuestion.value === question) {
    currentOpenedQuestion.value = null;
  } else {
    currentOpenedQuestion.value = question;
  }
}

const sponsors: Sponsor[] = [
  {
    name: "UMD Student Government Association",
    image: "/img/logos/sga.svg",
    amount: -1,
    url: "https://www.umdsga.com/",
  },
  {
    name: "Department of Computer Science",
    image: "/img/logos/DepartmentOfCS.svg",
    amount: -1,
    url: "https://www.cs.umd.edu/",
  },
  {
    name: "College of Computer, Mathematical, and Natural Sciences",
    image: "/img/logos/CMNS.svg",
    amount: -1,
    url: "https://cmns.umd.edu/",
  },
  {
    name: "University of Maryland Institute for Advanced Computer Studies",
    image: "/img/logos/UMIACS.svg",
    amount: -1,
    url: "https://www.umiacs.umd.edu/",
  },
  {
    name: "Peraton",
    image: "/img/logos/Peraton.svg",
    amount: -1,
    url: "https://www.peraton.com/",
  },
  {
    name: "Capital One",
    image: "/img/logos/CapitalOne.svg",
    amount: -1,
    url: "https://www.capitalone.com/",
  },
  {
    name: "Bloomberg",
    image: "/img/logos/Bloomberg.svg",
    amount: -1,
    url: "https://www.bloomberg.com/",
  },
  {
    name: "Cipher Tech Solutions",
    image: "/img/logos/cipher_tech.svg",
    amount: -1,
    url: "https://www.ciphertechsolutions.com/",
  },
  {
    name: "Endeavor",
    image: "/img/logos/endeavor.svg",
    amount: -1,
    url: "https://www.endeavor.ai/",
  },
  {
    name: "Cloudforce",
    image: "/img/logos/cloud_force.svg",
    amount: -1,
    url: "https://gocloudforce.com/",
  },
  {
    name: "Microsoft",
    image: "/img/logos/microsoft.svg",
    amount: -1,
    url: "https://www.microsoft.com/en-us",
  },
  {
    name: "Robert H. Smith School of Business",
    image: "/img/logos/school_of_business.svg",
    amount: -1,
    url: "https://www.rhsmith.umd.edu/",
  },
  {
    name: "Robert H. Smith School of Business - Plus 1",
    image: "/img/logos/smith_plus.svg",
    amount: -1,
    url: "https://www.rhsmith.umd.edu/programs/plus-1",
  },
  {
    name: "Ionq",
    image: "/img/logos/ionq.svg",
    amount: -1,
    url: "https://www.ionq.com/",
  },
  {
    name: "University of Maryland Sustainability Fund",
    image: "/img/logos/sustainability.svg",
    amount: -1,
    url: "https://sustainability.umd.edu/",
  },
  {
    name: "A. James Clark School of Engineering",
    image: "/img/logos/ClarkSchool.svg",
    amount: -1,
    url: "https://eng.umd.edu/",
  },
];

gsap.registerPlugin(SplitText, ScrollTrigger);

const containerRef = ref<HTMLElement | null>(null);

let ctx: gsap.Context | null = null;
let played = false;

let refreshInitHandler: (() => void) | null = null;

function setup() {
  if (!containerRef.value) return;
  if (played) return;

  ctx?.revert();

  ctx = gsap.context(() => {
    const scroller = (document.querySelector(".wrapper") as Element) ?? window;
    ScrollTrigger.defaults({ scroller });

    const questionEls = gsap.utils.toArray<HTMLElement>(".Question");

    const splits: SplitText[] = [];

    questionEls.forEach((q) => {
      const btn = q.querySelector<HTMLElement>(".Question_Button");
      if (!btn) return;

      gsap.set([q, btn], { willChange: "transform,opacity", force3D: true });

      const split = new SplitText(btn, {
        type: "lines",
        linesClass: "faq-line",
      });

      splits.push(split);

      gsap.set(q, { opacity: 0, y: 30 });
      gsap.set(split.lines, {
        opacity: 0,
        rotationX: -90,
        transformOrigin: "50% 50% -120px",
        force3D: true,
      });

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: q,
          start: "top 90%",
          toggleActions: "play none none none",
          onEnter: () => {
            if (q === questionEls[questionEls.length - 1]) played = true;
          },
        },
      });

      tl.to(q, { opacity: 1, y: 0, duration: 0.55, ease: "power3.out" }, 0).to(
        split.lines,
        {
          opacity: 1,
          rotationX: 0,
          duration: 0.6,
          ease: "power3.out",
          stagger: 0.08,
          force3D: true,
        },
        0,
      );
    });

    if (!refreshInitHandler) {
      refreshInitHandler = () => {
        splits.forEach((s) => s.revert());
      };
      ScrollTrigger.addEventListener("refreshInit", refreshInitHandler);
    }
  }, containerRef.value);

// ScrollTrigger.refresh();
}

onMounted(async () => {
  await nextTick();
  setup();
  window.addEventListener("resize", setup);
});

onUnmounted(() => {
  window.removeEventListener("resize", setup);
  if (refreshInitHandler) {
    ScrollTrigger.removeEventListener("refreshInit", refreshInitHandler);
    refreshInitHandler = null;
  }
  ctx?.revert();
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
  position: relative;
  overflow: hidden;
  text-align: left;

  &::after {
    content: "";
    position: absolute;
    top: -110vh;
    left: -250vw;
    width: 400vw;
    height: 200vh;
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
    content: "";
    position: absolute;
    right: 0%;
    top: -40vh;
    width: 40vw;
    height: 70vh;

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
  color: #fff7eb;
  position: relative;
  text-shadow: 0 0 20px #fff7eb;
}

.sponsor-logo-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  padding: 2rem 3vw;
  margin-bottom: 5vh;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  overflow: hidden;
}

.sponsor-card {
  aspect-ratio: 16 / 10;
  background-color: #a7a7a7;
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-family: "Avenir";
  font-weight: 600;
  font-size: 2vw;
  color: #1a2e33;
  text-decoration: none;
  transition: background-color 0.3s ease, transform 0.3s ease,
    box-shadow 0.3s ease;
  padding: 2rem;
  cursor: pointer;
  min-width: 0;

  img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  &:hover {
    background-color: #bebebe;
    transform: scale(1.05);
    box-shadow: 0 4px 20px rgba(255, 247, 235, 0.3);
  }
}

.button-wrapper {
  display: flex;
  justify-content: center;
}

.sponsor-button {
  background-color: #ff6f3f;
  border-radius: 5rem;
  border-style: solid;
  border-color: #e54d1a;
  color: white;

  font-weight: bold;
  letter-spacing: 0.2rem;
  margin-bottom: 2rem;
  cursor: pointer;
  transition: transform 0.25s ease, box-shadow 0.25s ease,
    background-color 0.25s ease;
  font-size: 1.4vw;
  padding: 0.6vw 2vw;
  border-width: 0.2vw;
}

.sponsor-button:hover {
  transform: scale(1.07);
  box-shadow: 0 0 20px rgba(255, 111, 63, 0.5);
  background-color: #ff8a5c;
}

.sponsor-text-div {
  font-size: 2vw;
  margin-bottom: 5vh;
  margin-left: 4.21875vw;
  z-index: 2;
  color: #fff7eb;
  position: relative;
  text-shadow: 0 0 20px #fff7eb;
}

.faq-contents {
  position: relative;
  font-family: "Avenir";
  font-style: normal;
  font-weight: 500;
  border-radius: 15px;
  padding: 3vw;
  overflow-y: visible;
  z-index: 10;
  text-align: center;
  min-height: auto;
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
  font-family: "Avenir";
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
  font-family: "Avenir";
  font-size: 1.6vw;
  line-height: 1.3;
  font-weight: bold;
  color: white;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  overflow: hidden;
  height: 6vw;
  width: 100%;
  cursor: pointer;

  &::before {
    content: "";
    width: 3rem;
    height: 3rem;
    margin-top: 1rem;
    margin-right: 1rem;

    display: inline-block;
    transform-origin: 50% 50%;
    transform: translateY(-4px);

    background-color: #fff7eb;

    -webkit-mask: url("../assets/img/icons/faq_star.svg") no-repeat center /
      contain;
    mask: url("../assets/img/icons/faq_star.svg") no-repeat center / contain;

    filter: drop-shadow(0 0 6px #fff7eb);

    transition: opacity 0.3s ease-out, transform 0.4s ease-out;
  }

  &.opened::before {
    transform: translateY(-4px) rotateZ(45deg);
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
  padding-left: calc(32px + 1rem + 3rem);
  text-align: left;
  font-size: 1.4vw;
  overflow-y: auto;
  transition: max-height 0.6s ease-in-out;
  margin-bottom: 2rem;
}

@media (max-width: 1024px) {
  .sponsor-logo-container {
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    padding: 1.5rem 3vw;
  }

  .sponsor-button {
    font-size: 2vw;
    padding: 0.8vw 2.5vw;
    border-width: 0.3vw;
  }

  .Answer_Opened {
    padding: 0px 12px;
    padding-top: 1rem;
    padding-left: calc(23px + 1rem + 3rem);
    text-align: left;
    font-size: 1.4vw;
    overflow-y: auto;
    transition: max-height 0.6s ease-in-out;
    margin-bottom: 2rem;
  }
}

@media (max-width: 768px) {
  .faq-text-div,
  .sponsor-text-div {
    font-size: 5vw;
    text-align: left;
    margin-left: 5vw;
  }

  .sponsor-logo-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    padding: 1rem 4vw;
  }

  .sponsor-card {
    font-size: 4vw;
    padding: 1rem;
  }

  .sponsor-button {
    border-radius: 5rem;
    letter-spacing: 0.25rem;
    font-size: 4vw;
    border-width: 0.7vw;
  }

  .Question_Column {
    min-width: 100%;
  }

  .Question,
  .Question_Button {
    font-size: 3.5vw;
    padding-bottom: 15px;
  }

  .Question_Button {
    height: 10vw;
    padding: 2rem 12px 1.75rem;
    &::before {
      width: 3rem;
      height: 3rem;
    }
  }

  .Answer,
  .Answer_Opened {
    height: 100%;
    font-size: 2.5vw;
  }

  .Answer_Opened {
    padding: 0px 12px;
    padding-top: 1rem;
    padding-left: calc(27px + 1rem + 3rem);
    text-align: left;
    font-size: 3vw;
    overflow-y: auto;
    transition: max-height 0.6s ease-in-out;
    margin-bottom: 2rem;
  }
}

@media (max-width: 480px) {
  .sponsor-logo-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    padding: 1rem 4vw;
  }

  .sponsor-card {
    padding: 0.5rem;
    font-size: 3vw;
  }
}

@media (min-width: 1200px) {
  .Question_Button::before {
    width: 3rem;
    height: 3rem;
  }
}
</style>

<style lang="scss">
a.link {
  color: #ff6f3f;
  text-decoration: underline;
}

ul {
  margin-block-start: 1rem;
  margin-block-end: 1rem;
  padding-inline-start: 1rem;
}
</style>
