<template>
  <div class="footer-container">
    <div class="footer-background">
      <picture>
        <source media="(max-width: 700px)" srcset="../assets/img/images/footer_bg_mobile.svg" />
        <img src="../assets/img/images/footer_bg.svg" alt="" class="background-image" />
      </picture>
      
      <div class="footer-content">
        <div class="logo-section">
          <img src="../assets/img/images/bitcamp_logo.svg" alt="Bitcamp" class="bitcamp-logo" />
        </div>

        <div class="links-section">
          <div class="link-columns">
            <div class="link-column">
              <a href="#tracks">Tracks</a>
              <a href="#campfire-games">Campfire Games</a>
              <a href="#roster">Our Team</a>
              <a href="#schedule">Schedule</a>
              <a href="#faq">FAQ</a>
            </div>
            <div class="link-column">
              <a href="mailto:hello@bit.camp">Contact Us</a>
              <a href="https://bit.camp/sponsor">Sponsor Us</a>
              <a href="http://mlh.io/code-of-conduct">MLH Code of Conduct</a>
              <a href="/brand.pdf">Brand Guidelines</a>
            </div>
          </div>
        </div>
      </div>

      <div class="social-icons">
        <a href="https://www.instagram.com/bitcamp" target="_blank" rel="noopener noreferrer">
          <img src="../assets/img/images/instagram_logo.svg" alt="Instagram" />
        </a>
        <a href="https://www.tiktok.com/@bitcamp_umd" target="_blank" rel="noopener noreferrer">
          <img src="../assets/img/images/tiktok_logo.svg" alt="TikTok" />
        </a>
        <a href="https://x.com/bitcmp" target="_blank" rel="noopener noreferrer">
          <img src="../assets/img/images/x_logo.svg" alt="X" />
        </a>
        <a href="https://www.facebook.com/bitcmp" target="_blank" rel="noopener noreferrer">
          <img src="../assets/img/images/facebook_logo.svg" alt="Facebook" />
        </a>
      </div>

      <div class="copyright">
        Copyright © 2019-2026 Bitcamp. All rights reserved.
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: 'Footer',
};
</script>

<style scoped>
.footer-container {
  width: 100%;
  position: relative;
  background-color: #010B18;
}

.footer-background {
  position: relative;
  width: 100%;
  overflow: visible;
  background-color: #010B18;
  aspect-ratio: 1442 / 813;
}

.footer-background picture {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
  z-index: 0;
}

.footer-content {
  position: absolute;
  z-index: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 100%;
  bottom: 2vw;
}

.logo-section {
  display: flex;
  align-items: center;
}

.bitcamp-logo {
  width: calc(5rem + 15vw);
  padding-left: 2vw;
}

.links-section {
  padding: calc(7rem + 23vw) 2vw 0;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.link-columns {
  display: flex;
  gap: 4vw;
}

.link-column {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.link-column a {
  color: #FFF7EB;
  text-decoration: none;
  font-size: calc(0.5rem + 1vw);
  font-family: 'Avenir';
  font-weight: 400;
  transition: opacity 0.2s;
}

.link-column a:hover {
  opacity: 0.7;
}

.social-icons {
  display: flex;
  gap: 1.2vw;
  align-items: center;
  position: absolute;
  bottom: 1.5vw;
  right: 2vw;
  z-index: 1;
}

.social-icons a {
  display: flex;
  align-items: center;
  transition: opacity 0.2s;
}

.social-icons a:hover {
  opacity: 0.7;
}

.social-icons img {
  width: calc(0.5rem + 2.5vw);
}

.copyright {
  position: absolute;
  bottom: 1.5vw;
  padding-left: 2vw;
  color: #FFF7EB;
  font-size: calc(0.5rem + 1vw);
  font-weight: 300;
  z-index: 1;
}

@media (max-width: 700px) {
  .footer-background {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start ;
    gap: 2rem;
  }

  .footer-content {
    position: static;
    height: auto;
    bottom: auto;
    flex-direction: column;
    gap: 2rem;
    align-items: flex-start;
    text-align: left;
    order: 1;
    padding: 4rem 0 0 4vw;
  }

  .logo-section {
    position: relative;
    align-items: flex-start;
    padding-top: 2.5rem;
  }

  .logo-section::before {
    content: "";
    position: absolute;
    width: 100%;
    top: 0;
    left: 0;
    height: 2px;
    width: 90vw;
    background: #FFFFFF;
    opacity: 0.5;
  }

  .bitcamp-logo {
    width: calc(10rem + 20vw);
  }

  .links-section {
    align-items: flex-start;
    padding: 0 4vw 0 0;
  }

  .link-columns {
    flex-direction: row;
    text-align: left;
    gap: 8rem;
  }

  .link-column a {
    font-size: calc(0.9rem + 1.5vw);
  }

  .social-icons {
    position: static;
    order: 2;
    gap: 1.5rem;
    justify-content: flex-start;
    padding: 2vw 0 2vw 4vw;
  }

  .social-icons img {
    width: calc(1.5rem + 3.5vw);
  }

  .copyright {
    position: static;
    order: 3;
    padding-left: 4vw;
    padding-bottom: 3rem;
    text-align: left;
  }
}
</style>