/*********************************************************************************
 Template Name: Optimal Multipurpose eCommerce Bootstrap 5 Html Template
 Description: A perfect template to build beautiful and unique Fashion websites. It comes with nice and clean design.
 Version: 1.0
 **********************************************************************************/


/*************************************************
 1. Preloader Loading
 2. Promotional Bar Header
 3. Top Bar Slider Header
 4. Header Search Drawer
 5. Setting Box dropdown
 6. Masonry Collection Banners
 7. Mobile Main Menu
 8. Promotion / Notification Cookie Bar 
 9. Slick Slider
 10. Sidebar Categories Level links
 11. Price Range Slider
 12. Color Swacthes
 13. Footer links for mobiles
 14. Show hide Product Tags
 15. Show hide Product Filters
 16. Timer Count Down
 17. Scroll Top
 18. Height Product Grid Image
 19. Product Zoom
 20. Product Detail Slider
 21. Product Sticky Bottom Cart
 22. Product Page Popup
 23. Quantity Plus Minus
 24. Visitor Fake Message
 25. Tabs With Accordian Responsive
 26. Product Tabs
 27. Image to background js
 28. Sticky Product Slider
 29. Infinite Scroll js
 30. QuickView Popup
 31. Tooltip
 32. Product Grid/List change view
 32. Write Review Toggle Box
 34. Background Parallax image
 *************************************************/

(function ($) {
    // Start of use strict
    'use strict';

    /*-----------------------------------------
     1. Preloader Loading 
     -----------------------------------------*/
    function pre_loader() {
        $("#load").fadeOut();
        $('#pre-loader').delay(500).fadeOut(500);
    }
    pre_loader();

    function dismiss() {
        $(".product-notification .close").on('click', function () {
            $(".product-notification").hide().fadeOut('slow');
        });
    }
    dismiss();

    /*-----------------------------------------
     2. Promotional Bar Header 
     -----------------------------------------*/
    function promotional_bar() {
        $(".closeHeader").on('click', function () {
            $(".promotion-header").slideUp();
            Cookies.set('promotion', 'true', {expires: 1});
            return false;
        });
    }
    promotional_bar();

    /*-----------------------------------------
     3. Top Bar Slider Header
     ----------------------------------------- */
    function promotional_bar_slider() {
        $('.topbar-slider-items').slick({
            dots: false,
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: true,
            autoplay: true,
            autoplaySpeed: 5000,
            rtl: true
        });
    }
    promotional_bar_slider();

    /* 3.1 Top Bar Slider */
    function topbar_slider() {
        $('.topBar-slider').slick({
            dots: false,
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows: false,
            autoplay: true,
            autoplaySpeed: 4000,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    topbar_slider();

    /* 3.2 Top Bar Slider 2 */
    function topbar_slider_style1() {
        $('.topBar-slider-style1').slick({
            dots: false,
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: false,
            autoplay: true,
            autoplaySpeed: 4000,
            fade: true,
            rtl: true
        });
    }
    topbar_slider_style1();

    /* 3.3 Store Bar Slider */
    function store_bar_slider() {
        $('.store-slider-items').slick({
            dots: false,
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows: false,
            autoplay: true,
            autoplaySpeed: 6000,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1199,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    store_bar_slider();

    /*-----------------------------------------
     4. Header Search Drawer
     -----------------------------------------*/
    $('.modalOverly, .closeSearch').on('click', function () {
        $('#search-popup').removeClass("active");
        $('body').removeClass("showOverly searchact");
    });

    $('.header-main .site-search').on('click', function (e) {
        e.preventDefault();
        $('body').addClass("showOverly searchact");
        $('#search-popup').addClass("active");
        //$('.header-main').addClass("searchact");
        $('.user-links,#set_box,#cart-drawer').removeClass("active");
        setTimeout(function () {
            $('input[name=q]').focus();
        }, 600);
    });

    /*-----------------------------------------
     5. Setting Box dropdown
     -----------------------------------------*/
    function setting_box() {
        $(".setting-link").on("click", function () {
            $("#settingsBox").toggleClass("active");
        });
        $("body").on("click", function (e) {
            var t = $(e.target);
            t.parents().is("#settingsBox") || t.parents().is(".setting-link") || t.is(".setting-link") || $("#settingsBox").removeClass("active");
        });
    }
    setting_box();

    /* 5.1 User Links dropdown */
    function user_links() {
        $(".user-link").on("click", function () {
            $("#userLinks").toggleClass("active");
        });
        $("body").on("click", function (e) {
            var t = $(e.target);
            t.parents().is("#userLinks") || t.parents().is(".user-link") || t.is(".user-link") || $("#userLinks").removeClass("active");
        });
    }
    user_links();

    /*-----------------------------------------
     6. Masonry Collection Banners
     -----------------------------------------*/
    var $grid = $('.banner-grid, .collection-page-grid, .category-page-grid, .lookbook, .custom-text-masonry-items').masonry({
        itemSelector: '.banner-item, .collection-page-item, .category-grid-item, .grid-lookbook, .custom-text-masonry-item',
        percentPosition: true,
        columnWidth: '.grid-sizer',
        isOriginLeft: false
    });

    // layout Masonry after each image loads
    $grid.imagesLoaded().progress(function () {
        $grid.masonry();
    });

    $(".btn-shop").on("click", function () {
        $(".products .grid-lb, .grid-lookbook").removeClass("active"),
                $(this).next().addClass("active"), $(this).parents(".grid-lookbook").addClass("active");
    });
    $(".btn-shop-close").on("click", function () {
        $(this).parent().removeClass("active");
    });

    /*-----------------------------------------
     7. Mobile Main Menu
     -----------------------------------------*/
    var selectors = {
        body: 'body',
        sitenav: '#siteNav',
        navLinks: '#siteNav .lvl1 > a',
        menuToggle: '.js-mobile-nav-toggle',
        mobilenav: '.mobile-nav-wrapper',
        menuLinks: '#MobileNav .an',
        closemenu: '.closemobileMenu'
    };

    $(selectors.navLinks).each(function () {
        if ($(this).attr('href') == window.location.pathname)
            $(this).addClass('active');
    });

    $(selectors.menuToggle).on("click", function () {
        body: 'body',
                $(selectors.mobilenav).toggleClass("active");
        $(selectors.body).toggleClass("menuOn");
        $(selectors.menuToggle).toggleClass('mobile-nav--open mobile-nav--close');
    });

    $(selectors.closemenu).on("click", function () {
        body: 'body',
                $(selectors.mobilenav).toggleClass("active");
        $(selectors.body).toggleClass("menuOn");
        $(selectors.menuToggle).toggleClass('mobile-nav--open mobile-nav--close');
    });

    $("body").on('click', function (event) {
        var $target = $(event.target);
        if (!$target.parents().is(selectors.mobilenav) && !$target.parents().is(selectors.menuToggle) && !$target.is(selectors.menuToggle)) {
            $(selectors.mobilenav).removeClass("active");
            $(selectors.body).removeClass("menuOn");
            $(selectors.menuToggle).removeClass('mobile-nav--close').addClass('mobile-nav--open');
        }
    });

    $(selectors.menuLinks).on('click', function (e) {
        e.preventDefault();
        $(this).toggleClass('an-plus-l an-minus-l');
        $(this).parent().next().slideToggle();
    });

    /*--------------------------------------
     8. Promotion / Notification Cookie Bar 
     -------------------------------------- */
    function cookie_promo() {
        if ($.cookie('promotion') != 'true') {
            $(".notification-bar").show();
        }
        $(".close-announcement").on('click', function () {
            $(".notification-bar").slideUp();
            $.cookie('promotion', 'true', {expires: 1});
        });
    }
    cookie_promo();

    /*-----------------------------------------
     9. Slick Slider
     -----------------------------------------*/
    /* 9.1 Homepage Slideshow */
    function home_slider() {
        $('.home-slideshow').slick({
            dots: true,
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            fade: true,
            arrows: true,
            autoplay: true,
            autoplaySpeed: 8000,
            lazyLoad: 'ondemand',
            rtl: true
        });
    }
    home_slider();

    // Full Size Banner on the Any Screen
    $(window).resize(function () {
        var bodyheight = $(this).height() - 35;
        $(".sliderFull .bg-size").height(bodyheight);
    }).resize();

    /* 9.2 Sidebar Product */
    function side_product_slider() {
        $('.sideProSlider').slick({
            dots: false,
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: true,
            autoplay: true,
            autoplaySpeed: 2500,
            rtl: true
        });
    }
    side_product_slider();

    /* 9.3 Category Page Slideshow */
    function category_slider() {
        $('.category-banner-slider').slick({
            dots: false,
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: true,
            rtl: true
        });
    }
    category_slider();


    /* 9.4 Products Slider */
    function product_slider() {
        $('.productSlider').slick({
            dots: false,
            infinite: true,
            slidesToShow: 4,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]

        });
    }
    product_slider();

    /* 9.5 Products Slider Style2 3 Items */
    function product_slider1() {
        $('.productSlider-style1').slick({
            dots: false,
            infinite: true,
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    product_slider1();

    /* 9.6 Products Slider Style3 */
    function product_slider2() {
        $('.productSlider-style2').slick({
            dots: false,
            infinite: true,
            slidesToShow: 5,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    product_slider2();

    /* 9.7 Products Slider Fullwidth */
    function product_slider_full() {
        $('.productSlider-fullwidth').slick({
            dots: false,
            infinite: true,
            slidesToShow: 6,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 600,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    product_slider_full();

    /* 9.8 Product Page */
    function product_slider_ppage() {
        $('.productPageSlider').slick({
            dots: false,
            infinite: true,
            slidesToShow: 5,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    product_slider_ppage();


    /* 9.9 Collection Slider */
    function collection_slider() {
        $('.collection-grid-slider').slick({
            dots: false,
            infinite: true,
            slidesToShow: 5,
            slidesToScroll: 1,
            arrows: true,
            autoplay: true,
            autoplaySpeed: 2000,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    collection_slider();

    /* 9.10 Collection Slider 3 Items */
    function collection_slider_3items() {
        $('.collection-slider-3items').slick({
            dots: false,
            infinite: true,
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows: true,
            autoplay: true,
            autoplaySpeed: 5000,
            rtl: true,
            responsive: [
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2
                    }
                }
            ]
        });
    }
    collection_slider_3items();

    /* 9.11 Collection Slider 4 Items */
    function collection_slider_4items() {
        $('.collection-slider-4items').slick({
            dots: false,
            infinite: true,
            slidesToShow: 4,
            slidesToScroll: 1,
            arrows: true,
            autoplay: true,
            autoplaySpeed: 5000,
            rtl: true,
            responsive: [
                {
                    breakpoint: 999,
                    settings: {
                        slidesToShow: 3
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2
                    }
                }
            ]
        });
    }
    collection_slider_4items();

    /* 9.12 Collection Slider 6 Items */
    function collection_slider_6items() {
        $('.collection-slider-6items').slick({
            dots: false,
            infinite: true,
            slidesToShow: 6,
            slidesToScroll: 1,
            arrows: true,
            autoplay: true,
            autoplaySpeed: 2000,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    collection_slider_6items();

    /* 9.13 Collection Slider 7 Items */
    function collection_slider_7items() {
        $('.collection-slider-7items').slick({
            dots: false,
            infinite: true,
            slidesToShow: 7,
            slidesToScroll: 1,
            arrows: true,
            autoplay: true,
            autoplaySpeed: 2000,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    collection_slider_7items();

    /* 9.14 Collection Slider2 4 Items */
    function collection_slider1() {
        $('.collection-grid-4item').slick({
            dots: false,
            infinite: true,
            slidesToShow: 4,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 600,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    collection_slider1();


    /* 9.15 Latest Blog Slider */
    function blogpost_slider() {
        $('.blog-post-slider').slick({
            dots: false,
            infinite: true,
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    blogpost_slider();

    /* 9.16 Blog Slider2 4 Items */
    function blogpost_slider_style1() {
        $('.blog-post-slider-style1').slick({
            dots: false,
            infinite: true,
            slidesToShow: 4,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    blogpost_slider_style1();

    /* 9.17 Blog Slider3 2 Items */
    function blogpost_slider_style2() {
        $('.blog-post-slider-style2').slick({
            dots: false,
            infinite: true,
            slidesToShow: 2,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 575,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    blogpost_slider_style2();

    /* 9.18 Logo Slider */
    function logo_slider() {
        $('.logo-bar').slick({
            dots: false,
            infinite: true,
            slidesToShow: 6,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 600,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    logo_slider();

    /* 9.19 Testimonial Slider */
    function testimonial_slider() {
        $('.quotes-slider').slick({
            dots: true,
            infinite: true,
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows: true,
            adaptiveHeight: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1,
                        arrows: false
                    }
                },
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1,
                        arrows: false
                    }
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1,
                        arrows: false
                    }
                }
            ]
        });
    }
    testimonial_slider();

    /* 9.20 Testimonial Slider 2 */
    function testimonial_slider_1item() {
        $('.quotes-slider-1item').slick({
            dots: true,
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: true,
            adaptiveHeight: true,
            rtl: true
        });
    }
    testimonial_slider_1item();


    /* 9.21 Instagram Slider */
    function instagram_slider() {
        $('.instagram-slider').slick({
            dots: false,
            infinite: true,
            slidesToShow: 7,
            slidesToScroll: 1,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 600,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    instagram_slider();

    /* 9.22 Instagram Slider 2 */
    function instagram_slider_style2() {
        $('.instagram-slider-style2').slick({
            dots: false,
            infinite: true,
            slidesToShow: 5,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 5000,
            arrows: true,
            rtl: true,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 600,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    instagram_slider_style2();

    /*-----------------------------------
     10. Sidebar Categories Level links
     -------------------------------------*/
    function categories_level() {
        $(".sidebar_categories .sub-level a").on("click", function () {
            $(this).toggleClass('active');
            $(this).next(".sublinks").slideToggle("slow");
        });
    }
    categories_level();

    $(".filter-widget .widget-title").on("click", function () {
        $(this).next().slideToggle('300');
        $(this).toggleClass("active");
    });

    /*-----------------------------------
     11. Price Range Slider
     -------------------------------------*/
    function price_slider() {
        $("#slider-range").slider({
            range: true,
            min: 12,
            max: 200,
            values: [0, 50],
            slide: function (event, ui) {
                $("#amount").val("ت" + ui.values[0] + " - ت" + ui.values[1]);
            }
        });
        $("#amount").val("ت" + $("#slider-range").slider("values", 0) +
                " - ت" + $("#slider-range").slider("values", 1));
    }
    price_slider();

    /*-----------------------------------
     12. Color Swacthes
     -------------------------------------*/
    function color_swacthes() {
        $.each($(".swacth-list"), function () {
            var n = $(".swacth-btn");
            n.on("click", function () {
                $(this).parent().find(n).removeClass("checked");
                $(this).addClass("checked");
            });
        });
    }
    color_swacthes();

    function img_swacthes() {
        var selector = '.swatches li';
        $(selector).on('click', function () {
            $(selector).removeClass('active');
            $(this).addClass('active');
        });
    }
    img_swacthes();

    function size_swacthes() {
        var selector = '.swatches-size li';
        $(selector).on('click', function () {
            $(selector).removeClass('active');
            $(this).addClass('active');
        });
    }
    size_swacthes();

    /*-----------------------------------
     13. Footer links for mobiles
     -------------------------------------*/
    function footer_dropdown() {
        $(".footer-links .h4").on('click', function () {
            if ($(window).width() < 767) {
                $(this).next().slideToggle();
                $(this).toggleClass("active");
            }
        });
    }
    footer_dropdown();

    // Resize Function 
    var resizeTimer;
    $(window).resize(function (e) {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () {
            $(window).trigger('delayed-resize', e);
        }, 250);
    });
    $(window).on("load resize", function (e) {
        if ($(window).width() > 767) {
            $(".footer-links ul").show();
        } else {
            $(".footer-links ul").hide();
        }
    });


    /* Blog Pages Sidebar Widget +/- */
    function blog_sidebar_dropdown() {
        $(".blog-sidebar .widget-title").on("click", function () {
            if ($(window).width() < 991) {
                $(this).next().slideToggle('300');
                $(this).toggleClass("active");
            }
        });
    }
    blog_sidebar_dropdown();
    $(window).on("load resize", function (e) {
        if ($(window).width() > 991) {
            $(".blog-sidebar .widget-content").show();
        } else {
            $(".blog-sidebar .widget-content").hide();
        }
    });

    /*-------------------------------
     14. Show hide Product Tags
     ----------------------------------*/
    $(".product-tags li").eq(10).nextAll().hide();
    $('.btnview').on('click', function () {
        $(".product-tags li").not('.filter--active').show();
        $(this).hide();
    });

    /*-------------------------------
     15. Show hide Product Filters
     ----------------------------------*/
    $('.btn-filter').on("click", function () {
        $(".filterbar").toggleClass("active");
    });
    $('.closeFilter').on("click", function () {
        $(".filterbar").removeClass("active");
    });
    // Hide Cart on document click
    $("body").on('click', function (event) {
        var $target = $(event.target);
        if (!$target.parents().is(".filterbar") && !$target.is(".btn-filter")) {
            $(".filterbar").removeClass("active");
        }
    });

    /*-------------------------------
     16. Timer Count Down
     ----------------------------------*/
    $('[data-countdown]').each(function () {
        var $this = $(this),
                finalDate = $(this).data('countdown');
        $this.countdown(finalDate, function (event) {
            $this.html(event.strftime('<span class="ht-count days"><span class="count-inner"><span class="time-count">%-D</span> <span>روز</span></span></span> <span class="ht-count hour"><span class="count-inner"><span class="time-count">%-H</span> <span>ساعت</span></span></span> <span class="ht-count minutes"><span class="count-inner"><span class="time-count">%M</span> <span>دقیقه</span></span></span> <span class="ht-count second"><span class="count-inner"><span class="time-count">%S</span> <span>ثانیه</span></span></span>'));
        });
    });

    /*-------------------------------
     17. Scroll Top
     ---------------------------------*/
    function scroll_top() {
        $("#site-scroll").on("click", function () {
            $("html, body").animate({scrollTop: 0}, 1000);
            return false;
        });
    }
    scroll_top();

    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $("#site-scroll").fadeIn();
        } else {
            $("#site-scroll").fadeOut();
        }
    });

    /*-------------------------------
     18. Height Product Grid Image
     ----------------------------------*/
    function productGridView() {
        var gridRows = [];
        var tempRow = [];
        productGridElements = $('.grid-products .item');
        productGridElements.each(function (index) {
            if ($(this).css('clear') != 'none' && index != 0) {
                gridRows.push(tempRow);
                tempRow = [];
            }
            tempRow.push(this);

            if (productGridElements.length == index + 1) {
                gridRows.push(tempRow);
            }
        });

        $.each(gridRows, function () {
            var tallestHeight = 0;
            var tallestHeight1 = 0;
            $.each(this, function () {
                $(this).find('.product-image > a').css('height', '');
                elHeight = parseInt($(this).find('.product-image').css('height'));
                if (elHeight > tallestHeight) {
                    tallestHeight = elHeight;
                }
            });

            $.each(this, function () {
                if ($(window).width() > 768) {
                    $(this).find('.product-image > a').css('height', tallestHeight);
                }
            });
        });
    }

    /*--------------------------
     19. Product Zoom
     ---------------------------- */
    function product_zoom() {
        $(".zoompro").elevateZoom({
            gallery: "gallery",
            galleryActiveClass: "active",
            zoomWindowWidth: 300,
            zoomWindowHeight: 100,
            scrollZoom: false,
            zoomType: "inner",
            cursor: "crosshair"
        });
    }
    product_zoom();

    /*----------------------------
     20. Product Detail Slider
     ------------------------------ */
    /* Product Detail Vertical Thumb Slider */
    function product_thumb() {
        $('.product-dec-slider-2').slick({
            infinite: true,
            slidesToShow: 5,
            vertical: true,
            verticalSwiping: true,
            centerPadding: '0',
            draggable: true,
            slidesToScroll: 1
        });
    }
    product_thumb();

    /* Product Detail Page Horizontal Thumb Slider */
    function product_thumb1() {
        $('.product-thumb-style1').slick({
            infinite: true,
            slidesToShow: 5,
            stageMargin: 5,
            slidesToScroll: 1,
            rtl: true
        });
    }
    product_thumb1();

    /* Product Detail Page Horizontal 2 Slide with Thumb Slider 2 */
    function product_single_style2() {
        $('.product-single-style2').slick({
            slidesToShow: 2,
            slidesToScroll: 2,
            arrows: true,
            fade: false,
            infinite: false,
            speed: 1000,
            asNavFor: '.product-thumb-style2',
            rtl: true
        });
        $('.product-thumb-style2').slick({
            slidesToShow: 5,
            slidesToScroll: 1,
            asNavFor: '.product-single-style2',
            dots: false,
            infinite: false,
            centerMode: false,
            focusOnSelect: true,
            rtl: true
        });
    }
    product_single_style2();

    /* Product Detail Page Center Slider */
    function product_center_mode() {
        $('.product-center-style3').slick({
            centerMode: true,
            infinite: true,
            centerPadding: '0',
            slidesToShow: 3,
            speed: 500,
            variableWidth: false,
            rtl: true,
            responsive: [
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        });
    }
    product_center_mode();


    /*----------------------------
     21. Sticky Header and Product Sticky Bottom Cart
     ------------------------------ */
    function sticky_cart() {
        window.onscroll = function () {
            /* Sticky Header */
            if ($(window).scrollTop() > 145) {
                $('.header-main').addClass("sticky-header animated fadeInDown");
            } else {
                $('.header-main').removeClass("sticky-header fadeInDown");
            }
            /* End Sticky Header */

            $(window).scrollTop() > 600 && $(".stickyCart").length ? (
                    $("body.template-product").css("padding-bottom", "70px"),
                    $(".stickyCart").slideDown()) : ($("body.template-product").css("padding-bottom", "0"),
                    $(".stickyCart").slideUp());
        };
        $(".stickyOptions .selectedOpt").on("click", function () {
            $(".stickyOptions ul").slideToggle("fast");
        }),
                $(".stickyOptions .vrOpt").on("click", function (e) {
            var t = $(this).attr("data-val"),
                    s = $(this).attr("data-no"),
                    a = $(this).text();
            $(".selectedOpt").text(a), $(".stickyCart .selectbox").val(t).trigger("change"), $(".stickyOptions ul").slideUp("fast"), this.productvariants = JSON.parse(document.getElementById("ProductJson-" + i).innerHTML), $(".stickyCart .product-featured-img").attr("src", this.productvariants.variants[s].featured_image.src.replace(/(\.[^\.]*$|$)/, "_60x60$&"));
        });
    }
    sticky_cart();

    /*--------------------------
     22. Product Page Popup
     ---------------------------- */
    function video_popup() {
        if ($('.popup-video').length) {
            $('.popup-video').magnificPopup({
                type: 'iframe', mainClass: 'mfp-zoom-in', removalDelay: 400, preloader: false, fixedContentPos: false
            });
        }
    }
    video_popup();

    /* Size Popup */
    function size_popup() {
        $('.sizelink').magnificPopup({
            type: 'inline',
            midClick: true,
            mainClass: 'mfp-zoom-in',
            removalDelay: 400
        });
    }
    size_popup();

    /*ShippingInfo Popup */
    function shippingInfo_popup() {
        $('.shippingInfo').magnificPopup({
            type: 'inline',
            midClick: true,
            mainClass: 'mfp-zoom-in',
            removalDelay: 400
        });
    }
    shippingInfo_popup();

    /* Inquiry Popup */
    function inquiry_popup() {
        $('.emaillink').magnificPopup({
            type: 'inline',
            midClick: true,
            mainClass: 'mfp-zoom-in',
            removalDelay: 400
        });
    }
    inquiry_popup();

    /* Addtocart Popup */
    function addtocart_popup() {
        $('.pro-addtocart-popup').magnificPopup({
            type: 'inline',
            midClick: true,
            mainClass: 'mfp-zoom-in',
            removalDelay: 400
        });
    }
    addtocart_popup();

    /* Portfolio Popup */
    function portfolio_popup() {
        $('.portfolio-popup').magnificPopup({
            type: 'inline',
            midClick: true,
            mainClass: 'mfp-zoom-in',
            removalDelay: 400
        });
    }
    portfolio_popup();

    /*----------------------------------
     23. Quantity Plus Minus
     ------------------------------------*/
    function qnt_incre() {
        $(".qtyBtn").on("click", function () {
            var qtyField = $(this).parent(".qtyField"),
                    oldValue = $(qtyField).find(".qty").val(),
                    newVal = 1;

            if ($(this).is(".plus")) {
                newVal = parseInt(oldValue) + 1;
            } else if (oldValue > 1) {
                newVal = parseInt(oldValue) - 1;
            }
            $(qtyField).find(".qty").val(newVal);
        });
    }
    qnt_incre();

    /*----------------------------------
     24. Visitor Fake Message
     ------------------------------------*/
    var userLimit = $(".userViewMsg").attr('data-user'),
            userTime = $(".userViewMsg").attr('data-time');
    $(".uersView").text(Math.floor((Math.random() * userLimit)));
    setInterval(function () {
        $(".uersView").text(Math.floor((Math.random() * userLimit)));
    }, userTime);

    /*-----------------------------------
     25. Tabs With Accordian Responsive
     -------------------------------------*/
    $(".tab_content").hide();
    $(".tab_content:first").show();
    /* if in tab mode */
    $("ul.tabs li").on('click', function () {
        $(".tab_content").hide();
        var activeTab = $(this).attr("rel");
        $("#" + activeTab).fadeIn();

        $("ul.tabs li").removeClass("active");
        $(this).addClass("active");

        $(".tab_drawer_heading").removeClass("d_active");
        $(".tab_drawer_heading[rel^='" + activeTab + "']").addClass("d_active");

        $('.productSlider').slick('refresh');
        $('.productSlider-style2').slick('refresh');
    });
    /* if in drawer mode */
    $(".tab_drawer_heading").on('click', function () {
        $(".tab_content").hide();
        var d_activeTab = $(this).attr("rel");
        $("#" + d_activeTab).fadeIn();

        $(".tab_drawer_heading").removeClass("d_active");
        $(this).addClass("d_active");

        $("ul.tabs li").removeClass("d_active");
        $("ul.tabs li[rel^='" + d_activeTab + "']").addClass("d_active");

        $('.productSlider').slick('refresh');
        $('.productSlider-style2').slick('refresh');
    });
    $('ul.tabs li').last().addClass("tab_last");


    /*----------------------------------
     26. Product Tabs
     ------------------------------------*/
    $(".tab-content").hide();
    $(".tab-content:first").show();
    /* if in tab mode */
    $(".product-tabs li").on('click', function () {
        $(".tab-content").hide();
        var activeTab = $(this).attr("rel");
        $("#" + activeTab).fadeIn();

        $(".product-tabs li").removeClass("active");
        $(this).addClass("active");

        $(this).fadeIn();
        if ($(window).width() < 767) {
            var tabposition = $(this).offset();
            $("html, body").animate({scrollTop: tabposition.top - 70}, 700);
        }
    });

    $('.product-tabs li:first-child').addClass("active");
    $('.tab-container h3:first-child + .tab-content').show();

    /* if in drawer mode */
    $(".acor-ttl").on("click", function () {
        $(".tab-content").hide();
        var activeTab = $(this).attr("rel");
        $("#" + activeTab).fadeIn();

        $(".acor-ttl").removeClass("active");
        $(this).addClass("active");
        if ($(window).width() < 767) {
            var tabposition = $(this).offset();
            $("html, body").animate({scrollTop: tabposition.top}, 700);
        }
    });

    /* Below 767 Accordian style */
    $(".tabs-ac-style").on("click", function () {
        $(".tab-content").hide();
        var activeTab = $(this).attr("rel");
        $("#" + activeTab).fadeIn();

        $(".tabs-ac-style").removeClass("active");
        $(this).addClass("active");

        $(this).fadeIn();
        if ($(window).width() < 767) {
            var tabposition = $(this).offset();
            $("html, body").animate({scrollTop: tabposition.top}, 700);
        }
    });

    /* --------------------------------------
     27. Image to background js
     -------------------------------------- */
    $(".bg-top").parent().addClass('b-top');
    $(".bg-bottom").parent().addClass('b-bottom');
    $(".bg-center").parent().addClass('b-center');
    $(".bg-left").parent().addClass('b-left');
    $(".bg-right").parent().addClass('b-right');
    $(".bg_size_content").parent().addClass('b_size_content');
    $(".bg-img").parent().addClass('bg-size');
    $(".bg-img.blur-up").parent().addClass('');
    jQuery('.bg-img').each(function () {
        var el = $(this),
                src = el.attr('src'),
                parent = el.parent();
        parent.css({
            'background-image': 'url(' + src + ')',
            'background-size': 'cover',
            'background-position': 'center',
            'background-repeat': 'no-repeat'
        });
        el.hide();
    });

    /*----------------------------------
     28. Sticky Product Slider
     ------------------------------------*/
    function sticky_pro_slider() {
        $('.product-single-style2 .product-details-img').slick({
            dots: false,
            infinite: false,
            item: 1,
            slidesToScroll: 1,
            rtl: true,
            responsive: [{
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1
                    }
                }]
        });
        $(window).width() > 767 ? $(".product-single-style2 .product-details-img").slick("unslick") : $(".product-single-style2 .product-details-img").slick("refresh");
    }
    sticky_pro_slider();

    function sticky_pro_slider_style4() {
        $('.product-single-style4 .product-details-img .row').slick({
            dots: false,
            infinite: false,
            item: 1,
            slidesToScroll: 1,
            rtl: true,
            responsive: [{
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1
                    }
                }]
        });
        $(window).width() > 767 ? $(".product-single-style4 .product-details-img .row").slick("unslick") : $(".product-single-style4 .product-details-img .row").slick("refresh");
    }
    sticky_pro_slider_style4();


    /*-----------------------------------
     29. Infinite Scroll js
     -------------------------------------*/
    function load_more() {
        $(".product-load-more .item").slice(0, 12).show();
        $(".loadMore").on('click', function (e) {
            e.preventDefault();
            $(".product-load-more .item:hidden").slice(0, 4).slideDown();
            if ($(".product-load-more .item:hidden").length == 0) {
                $(".infinitpagin").html('<div class="btn rounded loadMore">no more products</div>');
            }
        });
    }
    load_more();

    function load_more_five() {
        $(".product-five-load-more .item").slice(0, 10).show();
        $(".loadMoreFive").on('click', function (e) {
            e.preventDefault();
            $(".product-five-load-more .item:hidden").slice(0, 5).slideDown();
            if ($(".product-five-load-more .item:hidden").length == 0) {
                $(".infinitpagin-five").html('<div class="btn rounded loadMoreFive">no more products</div>');
            }
        });
    }
    load_more_five();

    function load_more_listview() {
        $(".product-load-more .list-product").slice(0, 7).show();
        $(".loadMore").on('click', function (e) {
            e.preventDefault();
            $(".product-load-more .list-product:hidden").slice(0, 5).slideDown();
            if ($(".product-load-more .list-product:hidden").length == 0) {
                $(".infinitpagin").html('<div class="btn rounded loadMore">no more products</div>');
            }
        });
    }
    load_more_listview();

    function load_more_post() {
        $(".blog--grid-load-more .article").slice(0, 5).show();
        $(".loadMorepost").on('click', function (e) {
            e.preventDefault();
            $(".blog--grid-load-more .article:hidden").slice(0, 1).slideDown();
            if ($(".blog--grid-load-more .article:hidden").length == 0) {
                $(".loadmore-post").html('<div class="btn btn-lg rounded loadMorepost">No more Blog Post</div>');
            }
        });
    }
    load_more_post();
    /*-----------------------------------
     End Infinite Scroll js
     -------------------------------------*/

    /* --------------------------------------
     30. QuickView Popup
     -------------------------------------- */
    function quick_view_popup() {
        $("body").on("click", ".quick-view-popup", function (e) {
            $.ajax({
                beforeSend: function () {
                    $("body").addClass("loading");
                },
                complete: function () {
                    $("body").removeClass("loading");
                }
            });
        });

        $('.quick-view-popup').magnificPopup({
            items: {
                src: '#quickView-modal'
            },
            type: 'inline',
            midClick: true,
            removalDelay: 500,
            mainClass: 'mfp-zoom-in'
        });
    }
    quick_view_popup();

    /*------------------------------------
     31. Tooltip
     -------------------------------------*/
    function tooltip() {
        if ($(window).width() > 991) {
            // $('[data-toggle="tooltip"]').tooltip();
            var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
            var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
                return new bootstrap.Tooltip(tooltipTriggerEl, {
                    trigger: 'hover'
                });
            });
        }
    }
    tooltip();

    /*------------------------------------
     32. Product Grid-List change view
     -------------------------------------*/
    function prd_change_view() {
        $('.change-view').on('click', function (e) {
            if ($(this).hasClass('prd-grid')) {
                $('.grid--view-items').removeClass('prd-list').addClass('prd-grid');
            } else if ($(this).hasClass('prd-list')) {
                $('.grid--view-items').removeClass('prd-grid').addClass('prd-list');
            }
        });

        $('.change-view').on('click', function () {
            $('.change-view').removeClass('change-view--active');
            $(this).addClass('change-view--active');
        });
    }
    prd_change_view();

    /*------------------------------------
     33. Write Review Toggle Box
     -------------------------------------*/
    function write_review() {
        $(".write-review-btn").on("click", function (e) {
            $('.write-review-btn').toggleClass('active');
            $(".product-review-form").slideToggle();
            e.preventDefault();
        });
    }
    write_review();

    /*------------------------------------
     34. Background Parallax image
     -------------------------------------*/
    function background_parallax_img() {
        var parallax = -0.5;
        var $bg_images = $(".background-parallax");
        var offset_tops = [];
        $bg_images.each(function (i, el) {
            offset_tops.push($(el).offset().top);
        });

        $(window).scroll(function () {
            var dy = $(this).scrollTop();
            $bg_images.each(function (i, el) {
                var ot = offset_tops[i];
                $(el).css("background-position", "50% " + (dy - ot) * parallax + "px");
            });
        });
    }
    background_parallax_img();


})(jQuery);

