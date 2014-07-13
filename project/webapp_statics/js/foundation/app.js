;(function ($, window, undefined) {
'use strict';

var $doc = $(document),
    Modernizr = window.Modernizr;

function column_equalizer(){
    // Equalize content text columns to the same height
    $('.equal-heights').equalize({children: '.equalized-item', reset: true, breakpoint: 750});
    return;
}

$(document).ready(function() {
    // Automatically add "no-reset-click" class on direct input parent label to 
    // follow their natural behavior (to propagate the click to their input child, 
    // usually only for radio or checkbox)
    $("form .button.dropdown label.no-reset-click input").each(function(index) {
        $(this).addClass('no-reset-click');
    });
    
    // Pop-in gallery
    $('.image-popin').magnificPopup({
        delegate: '.th',
        type: 'image',
        gallery:{
            enabled: false
        },
        // Only for medium and more screen resolution, mobiles will have 
        // default link behaviors
        disableOn: function() {
            if( $(window).innerWidth() < 768 ) {
                return false;
            } 
            return true;
        }
        
    });
    // Pop-in gallery
    $('.gallery').magnificPopup({
        delegate: '.th, .row .columns a',
        type: 'image',
        gallery:{
            enabled: true
        },
        // Only for medium and more screen resolution, mobiles will have 
        // default link behaviors
        disableOn: function() {
            if( $(window).innerWidth() < 768 ) {
                return false;
            } 
            return true;
        }
        
    });
    
    //$.fn.foundationAlerts           ? $doc.foundationAlerts() : null;
    $.fn.foundationButtons          ? $doc.foundationButtons() : null;
    //$.fn.foundationAccordion        ? $doc.foundationAccordion() : null;
    //$.fn.foundationNavigation       ? $doc.foundationNavigation() : null;
    $.fn.foundationTopBar           ? $doc.foundationTopBar() : null;
    //$.fn.foundationCustomForms      ? $doc.foundationCustomForms() : null;
    //$.fn.foundationMediaQueryViewer ? $doc.foundationMediaQueryViewer() : null;
    //$.fn.foundationTabs             ? $doc.foundationTabs({callback : $.foundation.customForms.appendCustomMarkup}) : null;
    //$.fn.foundationTooltips         ? $doc.foundationTooltips() : null;
    //$.fn.foundationMagellan         ? $doc.foundationMagellan() : null;
    //$.fn.foundationClearing         ? $doc.foundationClearing() : null;
    $.fn.placeholder                ? $('input, textarea').placeholder() : null;
    
    // Bind equalizer action on window resize
//     $(window).resize(function() {
//         column_equalizer();
//     });
    
//     // Display the current lang label
//     $('.dropdownselect').each(function(index) {
//         var current_lang = $(this).attr('data-dropdownselect-current');
//         if(current_lang){
//             var current_item = $("li[data-dropdownselect-value='"+current_lang+"']", $(this));
//             $(".selected-label", $(this)).html( $("a", current_item).html() );
//             current_item.attr("data-dropdownselect-selected", "true");
//         }
//     });
});

$(window).load(function () {
    // Equalize some columns after full page loading
    // NOTE: Needed to be in the $.load(), because webkit raise ready() even if it have 
    //       not download all ressources, this cause false dimensions because all images 
    //       have not yet be downloaded, so they doesn't set true dimensions on their 
    //       parent and etc..
    column_equalizer();
});
    
// Bind equalizer action on window resize
$(window).resize(function() {
    column_equalizer();
});

// UNCOMMENT THE LINE YOU WANT BELOW IF YOU WANT IE8 SUPPORT AND ARE USING .block-grids
// $('.block-grid.two-up>li:nth-child(2n+1)').css({clear: 'both'});
// $('.block-grid.three-up>li:nth-child(3n+1)').css({clear: 'both'});
// $('.block-grid.four-up>li:nth-child(4n+1)').css({clear: 'both'});
// $('.block-grid.five-up>li:nth-child(5n+1)').css({clear: 'both'});

// Hide address bar on mobile devices (except if #hash present, so we don't mess up deep linking).
if (Modernizr.touch && !window.location.hash) {
    $(window).load(function () {
    setTimeout(function () {
        // At load, if user hasn't scrolled more than 20px or so...
                        if( $(window).scrollTop() < 20 ) {
        window.scrollTo(0, 1);
        }
    }, 0);
    });
}

})(jQuery, this);
