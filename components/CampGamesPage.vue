<template>
    <link href='https://fonts.googleapis.com/css?family=Aleo' rel='stylesheet'>
    <div id="campfire-games" class="cfg-top">
        <img
            class="marshie-skeleton"
            src="assets\img\images\Marshieskeleton 1.svg"
            alt="Marshie skeleton"
        />
        <img
            class="cfg-title"
            src="assets\img\images\CAMPFIRE GAMES.svg"
            alt="Campfire games title"
        />
        <img
            class="dino-skeleton"
            src="assets\img\images\Dinoskeleton 2.svg"
            alt="Dino skeleton"
        />
    </div>
    <div class="gradient">
        <div class="cfg-box"> 
            <p id="cfg-blurb">
                The Campfire Games are a way to learn, grow, and build with the Bitcamp Community. 
                At the start of this year's event, you will join one of three teams based on your personality and 
                interests—joining forces with hackers from around the world! By winning unique challenges, attending workshops, 
                and participating in mini-events, you'll rack up points for your team. At the end of Bitcamp, members of the 
                winning team will receive limited edition Bitcamp swag. 
                <br><br>
                Find your community, develop your team identity, and collaborate on something bigger than yourself: #UnearthYourPotential
            </p>
        </div>
        <div class="team-row-desktop">
            <div class="team-row-item" v-for="team in teams" :key="'desktop-' + team.name">
                <img :src="team.src" :alt="team.name" />
            </div>
        </div>
        <div class="team-carousel">
            <div class="carousel-container">
                <button class="nav-button nav-button--left" @click="prevTeam">
                    <img src="assets/img/icons/left-arrow.svg" alt="Left Arrow" />
                </button>
                <div class="carousel-track" :style="trackStyle">
                    <div
                        v-for="(team, index) in teams"
                        :key="team.name"
                        class="carousel-item"
                    >
                        <img :src="team.src" :alt="team.name" />
                    </div>
                </div>
                <button class="nav-button nav-button--right" @click="nextTeam">
                    <img src="assets/img/icons/right-arrow.svg" alt="Right Arrow" />
                </button>
            </div>
        </div>
    </div>
    
</template>

<script lang="ts">
import redTeam from '@/assets/img/images/red-team.svg';
import greenTeam from '@/assets/img/images/green-team.svg';
import blueTeam from '@/assets/img/images/blue-team.svg';


export default {
    name: 'CampGamesPage',

    data() {
        return {
            currentTeamIndex: 1,
            teams: [
                { name: 'Red Team', src: redTeam },
                { name: 'Green Team', src: greenTeam },
                { name: 'Blue Team', src: blueTeam },
            ],
            
        };
    },
    computed: {
        trackStyle() {
            const ITEM_WIDTH  = 75;   // %
            const GAP         = 5;    // %
            const ITEM_STEP   = ITEM_WIDTH + GAP;
            const LEFT_OFFSET = (100 - ITEM_WIDTH) / 2; // 12.5

            const translateX = LEFT_OFFSET - this.currentTeamIndex * ITEM_STEP;
            return { transform: `translateX(${translateX}%)` };
        },
    },
    methods: {
        nextTeam() {
            this.currentTeamIndex =
                (this.currentTeamIndex + 1) % this.teams.length;
        },
        prevTeam() {
            this.currentTeamIndex =
                (this.currentTeamIndex - 1 + this.teams.length) %
                this.teams.length;
        },
    },
};


</script>

<style scoped>
.cfg-title {
    display: flex;
    width: 40%;
    margin-right: auto;
    margin-left: auto;
}
.dino-skeleton {
    width: 23%;
    margin-left: auto;
    visibility: visible;
}
.marshie-skeleton {
    width: 26%;
    margin-bottom: -5%;
    visibility: visible;
}
.dinos-vertical {
    display: none;
}
.cfg-box {
    background-color: #500001;
    border-color: #F98F37;
    border-style: solid;
    border-width: 17px;
    border-radius: 50px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 70%;
}
#cfg-blurb {
    font-family: 'Aleo'; 
    font-size: 24px;
    text-align:center;
    padding:4% 8%;
}
.cfg-top {
    padding-top: 5%;
    background-color: #701407;
    display: flex;
}
/* .horizontal-img-container {
    display: none;
} */
.gradient {
    background-image: url(assets/img/images/marshies-new.webp);
    background-repeat: no-repeat;
    background-size: cover;
    height: 176vh;
    background-position: center;
}
.team-row-desktop {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 3%;
    padding: 5vmax 2%;
    width: 100%;
    box-sizing: border-box;
}
.team-row-item {
    flex: 1;
    max-width: 33%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.team-row-item img {
    width: 100%;
    height: auto;
    object-fit: contain;
}
.team-carousel {
    display: none;
    justify-content: center;
    align-items: center;
    padding-top: 5vmax;
}
.carousel-container {
    overflow: hidden;
    width: 100%;
    margin: 0 auto;
    position: relative;
}
.carousel-track {
  display: flex;
  gap: 5%;
  transition: transform 0.5s ease;
}
.carousel-item {
  flex: 0 0 75%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 4vmax;
  padding-bottom: 4vmax;
}
.carousel-item img {
  width: 100%;
  height: auto;
  object-fit: contain;
}
.nav-button {
    position: absolute;
    top: 35%;
    z-index: 2;
    border: none;
    border-radius: 50%;
    width: 5vmax;
    height: 5vmax;
    min-width: 40px;
    min-height: 40px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    background: none;
}
.nav-button img {
    width: 100%;
    height: 100%;
    transition: filter 0.15s ease, transform 0.15s ease;
}
.nav-button:active img {
    filter: drop-shadow(0 0 6px #F98F37) drop-shadow(0 0 14px #F98F37);
    transform: scale(0.85);
}
.nav-button--left  { left:  1%; }
.nav-button--right { right: 1%; }
/* @media screen and (width:1024px) and (height: 1366px) {
    .gradient {
        height: 200vh;
    }
} */
@media screen and (max-width: 1024px) {
    #cfg-blurb {
        padding: 5% 10%;
    }
    .cfg-box {
        border-width: 12px;
        border-radius: 50px;
    }
    .dino-skeleton {
        visibility: hidden;
        width: 0px;
    }
    .marshie-skeleton {
        visibility: hidden;
        width: 0px;
    }
    .cfg-title {
        padding: inherit;
        margin: auto;
        width: 70%;
        display: block;
        margin-bottom: 5%;
    }
    .cfg-top {
        background-image: linear-gradient(180deg, #B94923 0%, #942F15 50%, #701407 100%);
        display: block;
    }
    .gradient {
        background-image: url(assets/img/images/Browncavestretched.webp);
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        height: auto;
    }
    .vertical-img-container {
        padding-top: 10%;
        padding-bottom: 40%;
        display: flex;
        margin-left: 15%;
    }
    /* .teams-horizontal {
        display: flex;
        width: 90%;
        visibility: visible;
    } */
    .team-carousel {
        display: flex;
    }
}
@media screen and (max-width: 700px) {
    #cfg-blurb {
        font-size: 19px;
    }
}
@media screen and (max-width: 515px) {
    #cfg-blurb {
        font-size: 17px;
    }
}
@media screen and (max-width: 400px) {
    #cfg-blurb {
        font-size: 15px;
    }
}
@media screen and (max-width: 270px) {
    #cfg-blurb {
        font-size: 10px;
    }
}
</style>