<template>
    <div id="campfire-games" class="cfg-top">
        <div class="cfg-content">
            <picture>
                <source media="(max-width: 1024px)" srcset="assets/img/images/cfgTitleMobile.svg">
                <img
                    class="cfg-title"
                    src="assets/img/images/cfgTitle.svg"
                    alt="Campfire games title"
                />
            </picture>
            <div class="cfg-box"> 
                <p id="cfg-blurb-first">
                    The Campfire Games are a way to learn, grow, and build with the Bitcamp Community. 
                    At the start of this year's event, you will join one of three teams based on your personality and 
                    interests—joining forces with hackers from around the world! 
                </p>
                <p id="cfg-blurb-second">
                    By winning unique challenges, attending workshops, 
                    and participating in mini-events, you'll rack up points for your team. At the end of Bitcamp, members of the 
                    winning team will receive limited edition Bitcamp swag. 
                </p>
            </div>
        </div>
    </div>
    <div class="gradient">
        <div class="vertical-img-container">
            <img src="assets/img/images/marshies-mv.svg" class="dinos-vertical">
        </div>
    </div>
    
</template>

<script lang="ts">
export default {
    name: 'PastEventsGrid',
};
</script>

<style scoped>
.cfg-top {
    padding: 5% 0;
    background-color: #010B18;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
}

.cfg-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 5rem 0;
}

.cfg-title {
    width: 100%;
    max-width: 60%;
}

.cfg-box {
    padding-left: 7%;
    padding-right: 50%;
}

#cfg-blurb-first, #cfg-blurb-second {
    font-family: 'Avenir';
    color: #FFF7EB;
    font-size: 2.2rem;
    line-height: 150%;
    text-align: left;
    margin: 0;
}

#cfg-blurb-first {
    font-weight: 700;
}

#cfg-blurb-second {
    font-weight: 300;
    margin-top: 2rem;
}

.vertical-img-container {
    display: none;
}

@media screen and (max-width: 1024px) {
    .cfg-top {
        display: block;
    }
    
    .cfg-content {
        padding-left: 0;
        align-items: flex-start;
    }
    
    .cfg-title {
        width: 150%;
        max-width: none;
    }
    
    .cfg-box {
        width: 80%;
        margin: 0 auto;
        align-items: center;
    }
}

.gradient {
    background-image: url(assets/img/images/marshies-new.webp);
    background-repeat: no-repeat;
    background-size: cover;
    height: 176vh;
    background-position: center;
}


@media screen and (max-width: 700px) {
    #cfg-blurb-first, #cfg-blurb-second {
        font-size: 16px;
    }

    .cfg-title {
        width: 125%;
    }
}

@media screen and (max-width: 515px) {
    #cfg-blurb-first, #cfg-blurb-second {
        font-size: 14px;
    }

    .cfg-title {
        width: 110%;
    }
}
</style>