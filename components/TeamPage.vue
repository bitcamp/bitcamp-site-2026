<template>
    <div id="roster" class="gradient">
        <div class="page_container">
            <div class="mid_content_container">
                <div class="vertical">
                <div class="small_poloroid_top">
                    <img class="small_photo" src="../assets/img/images/place_holder.jpeg" alt="lebron" />
                </div>
                <div class="small_poloroid_bottom">
                    <img class="small_photo" src="../assets/img/images/place_holder.jpeg" alt="lebron" />
                </div>
                </div>
                <div class="second_vertical">
                    <div class="team_text">
                        <img class ="orbit" src="../assets/img/icons/our-team.png" alt="lebron" />
                    </div>
                <div class="big_poloroid">
                    <img class="team_photo" src="../assets/img/images/gang.png" alt="lebron" />
                    <div class="caption_box">
                        <div class="polo_box">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. In mollis facilisis urna, in pellentesque 
                        nisi ultrices non. Duis vestibulum felis quis magna laoreet pretium. Aliquam ut pretium massa, a 
                        eleifend ligula. Quisque elementum arcu finibus vestibulum efficitur.
                        </div>
                        <div class="meet">
                            Meet the Team
                        </div>
                    </div>
                </div>
                </div>

            </div>

        </div>
    </div>
</template>

<script lang="ts">
export default {
    name: 'PastEventsGrid',
};
</script>

<style scoped>
.gradient {
    position: relative;
    overflow: hidden;
    min-height: 140vh;
    width: 100vw;
    margin-left: calc(-50vw + 50%);

    background-color: #03072A;

    /* Dense star clusters created with radial gradients - focused on right side */
    background-image:
      /* Cluster 1 - Top Right */
      radial-gradient(3px 3px at 76% 10%, rgba(255,255,255,0.95) 0, transparent 100%),
      radial-gradient(2.5px 2.5px at 79% 8%, rgba(255,255,255,0.9) 0, transparent 100%),
      radial-gradient(2px 2px at 73% 12%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(2px 2px at 82% 11%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 77% 6%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(2px 2px at 75% 14%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 81% 13%, rgba(255,255,255,0.75) 0, transparent 100%),
      radial-gradient(2px 2px at 78% 9%, rgba(255,255,255,0.8) 0, transparent 100%),
      
      /* Cluster 2 - Upper Right */
      radial-gradient(3px 3px at 88% 25%, rgba(255,255,255,0.95) 0, transparent 100%),
      radial-gradient(2.5px 2.5px at 91% 23%, rgba(255,255,255,0.9) 0, transparent 100%),
      radial-gradient(2px 2px at 85% 27%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(2px 2px at 93% 26%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 89% 21%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(2px 2px at 87% 29%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 92% 28%, rgba(255,255,255,0.75) 0, transparent 100%),
      radial-gradient(2px 2px at 90% 24%, rgba(255,255,255,0.8) 0, transparent 100%),
      
      /* Cluster 3 - Middle Upper Right */
      radial-gradient(3px 3px at 80% 38%, rgba(255,255,255,0.95) 0, transparent 100%),
      radial-gradient(2.5px 2.5px at 83% 36%, rgba(255,255,255,0.9) 0, transparent 100%),
      radial-gradient(2px 2px at 77% 40%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(2px 2px at 86% 39%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 81% 34%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(2px 2px at 79% 42%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 85% 41%, rgba(255,255,255,0.75) 0, transparent 100%),
      radial-gradient(2px 2px at 82% 37%, rgba(255,255,255,0.8) 0, transparent 100%),
      
      /* Cluster 4 - Middle Right */
      radial-gradient(3px 3px at 92% 48%, rgba(255,255,255,0.95) 0, transparent 100%),
      radial-gradient(2.5px 2.5px at 95% 46%, rgba(255,255,255,0.9) 0, transparent 100%),
      radial-gradient(2px 2px at 89% 50%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(2px 2px at 97% 49%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 93% 44%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(2px 2px at 91% 52%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 96% 51%, rgba(255,255,255,0.75) 0, transparent 100%),
      radial-gradient(2px 2px at 94% 47%, rgba(255,255,255,0.8) 0, transparent 100%),
      
      /* Cluster 5 - Middle Lower Right */
      radial-gradient(3px 3px at 74% 60%, rgba(255,255,255,0.95) 0, transparent 100%),
      radial-gradient(2.5px 2.5px at 77% 58%, rgba(255,255,255,0.9) 0, transparent 100%),
      radial-gradient(2px 2px at 71% 62%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(2px 2px at 80% 61%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 75% 56%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(2px 2px at 73% 64%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 79% 63%, rgba(255,255,255,0.75) 0, transparent 100%),
      radial-gradient(2px 2px at 76% 59%, rgba(255,255,255,0.8) 0, transparent 100%),
      
      /* Cluster 6 - Lower Right */
      radial-gradient(3px 3px at 86% 72%, rgba(255,255,255,0.95) 0, transparent 100%),
      radial-gradient(2.5px 2.5px at 89% 70%, rgba(255,255,255,0.9) 0, transparent 100%),
      radial-gradient(2px 2px at 83% 74%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(2px 2px at 92% 73%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 87% 68%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(2px 2px at 85% 76%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 91% 75%, rgba(255,255,255,0.75) 0, transparent 100%),
      radial-gradient(2px 2px at 88% 71%, rgba(255,255,255,0.8) 0, transparent 100%),
      
      /* Cluster 7 - Bottom Right */
      radial-gradient(3px 3px at 78% 85%, rgba(255,255,255,0.95) 0, transparent 100%),
      radial-gradient(2.5px 2.5px at 81% 83%, rgba(255,255,255,0.9) 0, transparent 100%),
      radial-gradient(2px 2px at 75% 87%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(2px 2px at 84% 86%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 79% 81%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(2px 2px at 77% 89%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 83% 88%, rgba(255,255,255,0.75) 0, transparent 100%),
      radial-gradient(2px 2px at 80% 84%, rgba(255,255,255,0.8) 0, transparent 100%),

      /* Cluster 8 - Far Right Upper */
      radial-gradient(2.5px 2.5px at 96% 15%, rgba(255,255,255,0.9) 0, transparent 100%),
      radial-gradient(2px 2px at 98% 13%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(2px 2px at 94% 17%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 97% 16%, rgba(255,255,255,0.75) 0, transparent 100%),
      
      /* Cluster 9 - Far Right Lower */
      radial-gradient(2.5px 2.5px at 94% 92%, rgba(255,255,255,0.9) 0, transparent 100%),
      radial-gradient(2px 2px at 96% 90%, rgba(255,255,255,0.85) 0, transparent 100%),
      radial-gradient(2px 2px at 92% 94%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(1.5px 1.5px at 95% 93%, rgba(255,255,255,0.75) 0, transparent 100%);

    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.gradient::after {
    content: "";
    position: absolute;

    top: 50%;
    left: -90vw;
    transform: translateY(-50%);

    width: 160vw;
    height: 260vh;

    background-image: url("@/assets/img/blue-planet.webp");
    background-repeat: no-repeat;
    background-size: contain;
    background-position: left center;

    z-index: 0;
    pointer-events: none;
}


.title{
    position: relative;
}


.orbit {
    width:70%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 6%;
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
    background-color: #FF6F3F;
    border: 0.3rem solid #E54D1A;
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

.small_poloroid_top {
    width: 23vw;
    height: auto;
    aspect-ratio: 13/16;
    display: flex;
    position: relative;
    left: 6vw;
    top: -9vh;
    flex-direction: column;
    align-items: center;
    background-color: white;
    padding: 8.5%;
    object-fit: cover;
    object-position: center;
    margin:0;
    rotate: -4deg;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.small_poloroid_bottom {
    width: 23vw;
    height: auto;
    aspect-ratio: 13/16;
    position: relative;
    left: 0.5vw;
    top: -5vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: white;
    padding: 8.5%;
    margin:0;
    rotate: 6deg;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.big_poloroid {
    width: 50vw;
    aspect-ratio: 20/12.5;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: white;
    padding: 2.5%;
    rotate: 2deg;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.6);
}

.team_photo {
    height: 100%;
    width: 100%;
    padding-bottom: 2%;
    overflow: hidden;
}

.small_photo {
    width: 100%;
    aspect-ratio: 1/1;
    padding-bottom: 2%;
    overflow: hidden;
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

@media screen and (max-width: 750px) {
    .gradient::after {
        display: none;
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

    .vertical{
        flex-direction: row;
        width:110%;
        justify-content: center;
        gap: 5%;
    }

    .big_poloroid{
        width: 105%;
        padding: 5%;
        box-shadow: 0px 8px 8px rgba(0, 0, 0, 0.6);
    }

    .polo_box {
        font-size: 2.1cqi;
    }
    .orbit {
        width: 110%;
        margin-top: 10%;
    }

    .small_poloroid_top{
        width: 50vw;
        left: 0;
        top: 1vh;
        padding: 4%;
        rotate: -5deg;
        z-index: 99999;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.6);
    }
    .small_poloroid_bottom{
        width: 50vw;
        padding: 4%;
        left: 0;
        top: 0;
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
        width: 100%;
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

}
</style>