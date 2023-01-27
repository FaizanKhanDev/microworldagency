const testominalslider = new Swiper(".testominal-slider", {
    spaceBetween: 100,
    grabCursor:true,
    loop:true,
    centerSlides:true,
    autoplay:  {
        delay:98600,
        disableOnInteration:false,
    },
    navigation: {
        prevEl: '.prev',
        nextEl:'.next',
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
        },
        600: {
            slidesPerView: 1,
        },
        991: {
            slidesPerView: 1,
        },
        1240: {
            slidesPerView: 2,
        },
        1540: {
            slidesPerView: 3,
        },
      
    },
});

