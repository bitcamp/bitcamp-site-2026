<template>
    <div id="roster" class="gradient">
        <div class="page_container">
            <div class="page_header">
                <img class="header_image" src="../assets/img/images/our_team_img.svg" alt="lebron" />
                <img class="header_image_mv" src="../assets/img/images/our_team_mv.svg" alt="lebron" />
            </div>
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
            <a href="/roster" target="_blank" class="bottom_button_container">
                <img class="meet_team_image" src="../assets/img/images/meet_team_button.svg" alt="lebron" />
            </a>

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
    min-height: 120vh;
    width: 100vw;
    margin-left: calc(-50vw + 50%);

    background-color: #03072A;

    background-image:
      radial-gradient(1px 1px at 10% 20%, rgba(255,255,255,0.9) 0, transparent 100%),
      radial-gradient(1px 1px at 30% 70%, rgba(255,255,255,0.8) 0, transparent 100%),
      radial-gradient(1px 1px at 50% 40%, rgba(255,255,255,0.7) 0, transparent 100%),
      radial-gradient(1px 1px at 70% 90%, rgba(255,255,255,0.6) 0, transparent 100%),
      radial-gradient(1px 1px at 90% 10%, rgba(255,255,255,0.8) 0, transparent 100%);

    background-size: 250px 250px;
    background-repeat: repeat;

     background-color: #03072A !important;
    background-image:
      radial-gradient(2px 2px at 10% 20%, red 0, transparent 100%),
      radial-gradient(2px 2px at 30% 70%, red 0, transparent 100%),
      radial-gradient(2px 2px at 50% 40%, red 0, transparent 100%);
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