// home.js
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Swiper for certificates
    new Swiper('.certificates-slider', {
      slidesPerView: 3,
      spaceBetween: 30,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });
  
    // Initialize Swiper for testimonials
    new Swiper('.testimonials-slider', {
      slidesPerView: 1,
      spaceBetween: 30,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
    });
  
    // Initialize Typed.js for the typing effect
    new Typed('.typing', {
      strings: ['a Developer', 'a Designer', 'an Innovator'],
      typeSpeed: 50,
      backSpeed: 50,
      loop: true
    });
  });