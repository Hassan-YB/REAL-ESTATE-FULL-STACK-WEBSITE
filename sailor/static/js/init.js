//* LuxRealty Version 1.0
//* Realse date : 20.10.2015
//* Author : themeforest.net/user/codepixel
//* Web site: http://codenpixel.com


jQuery(document).ready(function () {
    "use strict";

    // Properties Details slider
    jQuery("#rev_slider_details").show().revolution({
        sliderType: "standard",
        jsFileLocation: "revolution/js/",
        sliderLayout: "auto",
        dottedOverlay: "none",
        delay: 9000,
        navigation: {
            keyboardNavigation: "off",
            keyboard_direction: "horizontal",
            mouseScrollNavigation: "off",
            onHoverStop: "off",
            arrows: {
                style: "uranus",
                enable: true,
                hide_onmobile: true,
                hide_under: 478,
                hide_onleave: true,
                hide_delay: 200,
                hide_delay_mobile: 1200,
                tmp: '',
                left: {
                    h_align: "left",
                    v_align: "center",
                    h_offset: 20,
                    v_offset: 0
                },
                right: {
                    h_align: "right",
                    v_align: "center",
                    h_offset: 20,
                    v_offset: 0
                }
            },
            thumbnails: {
                style: "erinyen",
                enable: true,
                width: 130,
                height: 100,
                min_width: 140,
                wrapper_padding: 0,
                wrapper_color: "#fff",
                wrapper_opacity: "0.01",

                visibleAmount: 6,
                hide_onmobile: false,
                hide_onleave: false,
                direction: "horizontal",
                span: true,
                position: "outer-bottom",
                space: 0,
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 0
            }
        },

        gridwidth: 1230,
        gridheight: 720,
        lazyType: "none",
        shadow: 0,
        spinner: "spinner2",
        stopLoop: "on",
        stopAfterLoops: 0,
        stopAtSlide: 1,
        shuffle: "off",
        autoHeight: "on",
        disableProgressBar: "on",
        hideThumbsOnMobile: "off",
        hideSliderAtLimit: 0,
        hideCaptionAtLimit: 0,
        hideAllCaptionAtLilmit: 0,
        debugMode: false,
        fallbacks: {
            simplifyAll: "off",
            nextSlideOnWindowFocus: "off",
            disableFocusListener: false,
        }
    });

    // Main Carousel 
    jQuery("#rev_slider_108_1").show().revolution({
        sliderType: "carousel",
        jsFileLocation: "revolution/js/",
        sliderLayout: "auto",
        dottedOverlay: "none",
        delay: 9000,
        navigation: {
            keyboardNavigation: "off",
            keyboard_direction: "horizontal",
            mouseScrollNavigation: "off",
            onHoverStop: "off",
            arrows: {
                style: "metis",
                enable: true,
                hide_onmobile: true,
                hide_under: 768,
                hide_onleave: false,
                tmp: '',
                left: {
                    h_align: "left",
                    v_align: "center",
                    h_offset: 0,
                    v_offset: 0
                },
                right: {
                    h_align: "right",
                    v_align: "center",
                    h_offset: 0,
                    v_offset: 0
                }
            },
            thumbnails: {
                style: "erinyen",
                enable: true,
                width: 220,
                height: 140,
                min_width: 180,
                wrapper_padding: 0,
                wrapper_color: "#fff",
                wrapper_opacity: "0.01",
                tmp: '<span class="tp-thumb-over"></span><span class="tp-thumb-image"><div class="thumb-info"></span><h3 class="tp-thumb-property">{{param1}}</h3><p class="tp-thumb-price">{{param2}}</p><span class="tp-thumb-more"></span></div>',
                visibleAmount: 10,
                hide_onmobile: false,
                hide_onleave: false,
                direction: "horizontal",
                span: true,
                position: "outer-bottom",
                space: 0,
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 0
            }
        },
        carousel: {
            horizontal_align: "center",
            vertical_align: "center",
            fadeout: "on",
            vary_fade: "off",
            maxVisibleItems: 4,
            infinity: "on",
            space: 0,
            stretch: "off"
        },
        responsiveLevels: [1240, 1024, 778, 480],
        gridwidth: [800, 640, 480, 480],
        gridheight: [550, 500, 420, 340],
        lazyType: "none",
        parallax: {
            type: "scroll",
            origo: "enterpoint",
            speed: 400,
            levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        },
        shadow: 0,
        spinner: "off",
        stopLoop: "on",
        stopAfterLoops: 0,
        stopAtSlide: 1,
        shuffle: "off",
        autoHeight: "off",
        fullScreenAlignForce: "off",
        fullScreenOffsetContainer: "",
        fullScreenOffset: "60px",
        disableProgressBar: "on",
        hideThumbsOnMobile: "off",
        hideSliderAtLimit: 0,
        hideCaptionAtLimit: 0,
        hideAllCaptionAtLilmit: 0,
        debugMode: false,
        fallbacks: {
            simplifyAll: "off",
            nextSlideOnWindowFocus: "off",
            disableFocusListener: false,
        }
    });

    // Tooltips
    $('[data-toggle~="tooltip"]').tooltip({
        container: "body"
    });
    // Popovers
    $('[data-toggle~="popover"]').popover({
        container: "body"
    });

    // Responsive video
    $(".container").fitVids();

    // Truncate text,limit number
    $(".truncate").ellipsis({
        "maxLength": 120
    });

    //ripple with default options
    $(".btn").ripple();

    // Parallax - tuts - to any,with  data-image-src="path/image" data-stellar-background-ratio="0.4" set ratio for parallax
    $.stellar({
        horizontalScrolling: false,
        responsive: true
    });

    // add image to the element via data atribute and class="bg-image" ,no need for extra css
    $(".bg-image").css('background', function () {
        var bg = ('url(' + $(this).data("image-src") + ') no-repeat center center');
        return bg;
    });

    // fit image 
    $(".bg-image").css("background-size", "cover");


    // LOADER                 
    $(window).load(function () {
        $(".loader").fadeOut("slow");
    });


}); /* end:ready*/

