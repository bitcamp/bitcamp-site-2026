<template>
  <div id="roster" class="gradient">
    <div class="page_container">
      <div class="mid_content_container">
        <div class="vertical">
          <div class="small_poloroid_top">
            <img
              class="small_photo"
              src="../assets/img/images/NehaVeeragandham.webp"
              alt="Neha Veeragandham"
            />
            <div class="small_caption">
              <span class="small_name">Neha Veeragandham</span>
              <span class="small_title">Co-Executive Director</span>
            </div>
          </div>
          <div class="small_poloroid_bottom">
            <img
              class="small_photo"
              src="../assets/img/images/SaloniShah.webp"
              alt="Saloni Shah"
            />
            <div class="small_caption">
              <span class="small_name">Saloni Shah</span>
              <span class="small_title">Co-Executive Director</span>
            </div>
          </div>
        </div>
        <div class="second_vertical">
          <div class="team_text">
            <img
              class="orbit"
              src="../assets/img/icons/our-team.png"
              alt="lebron"
            />
          </div>
          <div class="big_poloroid">
            <img
              class="team_photo"
              src="../assets/img/images/DirectorGroupPhoto.webp"
              alt="lebron"
            />
            <div class="caption_box">
              <div class="polo_box">
                We’re the co-executive directors of Bitcamp 2026, and we’re over
                the moon to be working with this stellar team to lead Bitcamp
                into a new frontier of hackathon culture. Every one of our 83
                organizers is an essential part of this mission, helping to make
                Bitcamp 2026 a universe of creativity and innovation. We can’t
                wait to see these brilliant minds guide hackers like you as you
                Explore the Unknown and discover what’s possible! - Saloni and
                Neha
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, onBeforeUnmount, nextTick } from "vue";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

export default defineComponent({
  name: "PastEventsGrid",
  setup() {
    let ctx: gsap.Context | null = null;
    let played = false;

    onMounted(async () => {
      if (played) return;

      await nextTick();

      ctx = gsap.context(() => {
        const scroller =
          (document.querySelector(".wrapper") as Element) ?? window;

        ScrollTrigger.defaults({ scroller });

        gsap.set(
          [
            ".small_poloroid_top",
            ".small_poloroid_bottom",
            ".big_poloroid",
            ".orbit",
          ],
          { willChange: "transform,opacity", force3D: true },
        );

        gsap.from(".small_poloroid_top", {
          x: () => -window.innerWidth * 0.6,
          y: () => -window.innerHeight * 0.8,
          rotation: -45,
          scale: 0.4,
          force3D: true,
          scrollTrigger: {
            trigger: "#roster",
            start: "top bottom",
            end: "top top",
            scrub: 1,
            once: true,
          },
        });

        gsap.from(".small_poloroid_bottom", {
          x: () => window.innerWidth * 0.5,
          y: () => window.innerHeight * 0.6,
          rotation: 35,
          scale: 0.4,
          force3D: true,
          scrollTrigger: {
            trigger: "#roster",
            start: "top bottom",
            end: "top top",
            scrub: 1.4,
            once: true,
          },
        });

        gsap.from(".big_poloroid", {
          x: () => window.innerWidth * 0.3,
          y: () => window.innerHeight,
          rotation: -12,
          scale: 0.5,
          force3D: true,
          scrollTrigger: {
            trigger: "#roster",
            start: "top 80%",
            end: "top top",
            scrub: 1.8,
            once: true,
          },
        });

        gsap.fromTo(
          ".orbit",
          { y: -60, opacity: 0, force3D: true },
          {
            y: 0,
            opacity: 1,
            duration: 1.4,
            ease: "power2.out",
            scrollTrigger: {
              trigger: "#roster",
              start: "top 40%",
              once: true,
            },
            onComplete: () => {
              played = true;
            },
          },
        );
      });

      // ScrollTrigger.refresh();
    });

    onBeforeUnmount(() => {
      ctx?.revert();
    });

    return {};
  },
});
</script>

<style scoped>
.gradient {
  position: relative;
  overflow: hidden;
  height: auto;
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  /* background: transparent; */
  background-size: 100% 100%;
  background-repeat: no-repeat;
}

.gradient::after {
  content: "";
  position: absolute;

  top: 50%;
  left: -120vw;
  transform: translateY(-50%);

  width: 160vw;
  height: 260vh;

  /* background-image: url("@/assets/img/blue-planet.webp");
    background-repeat: no-repeat;
    background-size: contain;
    background-position: left center; */

  z-index: 0;
  pointer-events: none;
}

.title {
  position: relative;
}

.orbit {
  width: 70%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 5%;
}

.page_container {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 2;
  margin-top: 4rem;
}

.page_header {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-top: 10%;
}

.meet {
  width: 23vw;
  aspect-ratio: 10/2.5;
  background-color: #ff6f3f;
  border: 0.3rem solid #e54d1a;
  text-align: center;
  font-size: 1.7cqi;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 3cqi;
  font-family: Avenir;
  font-weight: 500;
  font-style: Bold;
}

.header_image {
  display: flex;
  margin-right: auto;
  margin-left: auto;
}

.header_image_mv {
  display: none;
}

.mid_content_container {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 10%;
  gap: 8%;
  width: 85%;
}

.team_image {
  width: 83%;
}

.team_text {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-end;
}

.second_vertical {
  display: flex;
  flex-direction: column;
  margin: 0;
  align-items: center;
  justify-content: center;
}

.vertical {
  display: flex;
  flex-direction: column;
  margin: 0;
  align-items: center;
  row-gap: 0;
}

.small_photo,
.team_photo {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}

.small_poloroid_top {
  width: 23vw;
  height: auto;
  display: flex;
  position: relative;
  left: 6vw;
  top: -9vh;
  flex-direction: column;
  align-items: center;
  background-color: white;
  padding: 5% 5% 20% 5%;
  margin: 0;
  rotate: -4deg;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.small_poloroid_bottom {
  width: 23vw;
  height: auto;
  position: relative;
  left: 0.5vw;
  top: -5vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: white;
  padding: 5% 5% 20% 5%;
  margin: 0;
  rotate: 6deg;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.small_caption {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-top: 8%;
}

.small_name {
  font-family: Avenir;
  font-weight: 700;
  color: #000;
  font-size: 1.1cqi;
  line-height: 1.3;
}

.small_title {
  font-family: Avenir;
  font-weight: 400;
  color: #555;
  font-size: 0.9cqi;
  line-height: 1.3;
  font-style: italic;
}

.big_poloroid {
  width: 50vw;
  height: auto;
  margin-bottom: 5%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: white;
  padding: 3%;
  rotate: 2deg;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.6);
}

.polo_box {
  width: 100%;
  font-family: Avenir;
  font-weight: 500;
  color: #000000;
  padding-top: 2%;
  padding-bottom: 2%;
  font-style: Medium;
  font-size: 1.2cqi;
  line-height: 1.4;
}

.caption_box {
  display: flex;
  height: auto;
  justify-content: center;
  align-items: center;
  flex-direction: row;
  width: 100%;
}

.message {
  background-image: url(../assets/img/images/message_background.svg);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  width: 55%;
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  margin-top: 1%;
}

.message_text {
  margin-left: 12%;
  margin-right: 5%;
  text-align: center;
  font-size: 17px;
}

.bottom_button_container {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 13%;
  margin-bottom: 5%;
}

.meet_team_image {
  width: 40%;
  display: flex;
  margin-left: 5%;
}

/* @media screen and (max-width: 1300px) {
    .gradient {
        min-height: 110vh;
    }
    .small_poloroid_top {
        top: -2vh;
    }
    .small_poloroid_bottom {
        top: 3vh;
    }
}

@media screen and (max-width: 1150px) {
    .gradient {
        min-height: 130vh;
    }
}

@media screen and (max-width: 1050px) {
    .gradient {
        min-height: 120vh;
    }
} */

@media screen and (max-width: 650px) {
  .gradient::after {
    display: none;
  }

  .gradient {
    max-height: 140dvh;
    height: auto;
  }

  .page_header {
    display: block;
  }

  .header_image {
    display: none;
  }

  .header_image_mv {
    margin: auto;
    display: block;
    margin-bottom: 5%;
    width: 60%;
    height: auto;
  }

  .vertical {
    flex-direction: row;
    width: 110%;
    justify-content: center;
    align-items: flex-start;
    gap: 5%;
    margin-top: 8%;
  }

  .polo_box {
    font-size: 2.1cqi;
  }

  .small_name {
    font-size: 2.8cqi;
  }

  .small_title {
    font-size: 2.2cqi;
  }

  .small_caption {
    padding-top: 14%;
  }
  .orbit {
    width: 110%;
    margin-top: 5%;
  }

  .big_poloroid {
    width: 105%;
    padding: 5%;
    box-shadow: 0px 8px 8px rgba(0, 0, 0, 0.6);
  }

  .small_poloroid_top {
    width: 50vw;
    left: 0;
    top: -4vh;
    padding: 4% 4% 18% 4%;
    rotate: -5deg;
    z-index: 99999;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.6);
  }

  .small_poloroid_bottom {
    width: 50vw;
    left: 0;
    top: -2vh;
    padding: 4% 4% 18% 4%;
    z-index: 99999;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.6);
  }

  .mid_content_container {
    flex-direction: column-reverse;
    justify-content: center;
    align-items: center;
  }

  .team_image {
    width: 80%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .team_photo {
    display: flex;
    /* margin-left: 25%; */
  }

  .message {
    background-image: none;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 80%;
  }
  .meet {
    font-size: 2.1cqi;
  }

  /* @media screen and (max-width: 700px) {
        .gradient {
            min-height: 190vh;
        }
         .small_poloroid_top {
            top: -2vh;
        }
        .small_poloroid_bottom {
            top: 3vh;
        }
    }
    @media screen and (max-width: 650px) {
        .gradient {
            min-height: 170vh;
        }
    }
    @media screen and (max-width: 550px) {
        .gradient {
            min-height: 150vh;
        }
    }
    @media screen and (max-width: 500px) {
        .gradient {
            min-height: 130vh;
        }
    }
    @media screen and (max-width: 450px) {
        .gradient {
            min-height: 120vh;
        }
    }
    @media screen and (max-width: 400px) {
        .gradient {
            min-height: 110vh;
        }
    }
    @media screen and (max-width: 350px) {
        .gradient {
            min-height: 0vh;
        }
    } */

  @media screen and (min-width: 700px) {
    .gradient {
      max-height: 145dvh;
      height: auto;
    }
  }

  @media screen and (min-width: 500px) {
    .gradient {
      max-height: 160dvh;
      height: auto;
    }
  }

  @media screen and (min-width: 1000px) {
    .gradient {
      max-height: 160dvh;
      height: auto;
    }
  }
}
</style>
