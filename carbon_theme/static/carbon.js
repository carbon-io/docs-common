
function getQueryStringParams (sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&');

    for (var i = 0; i < sURLVariables.length; i++) {
        var sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] == sParam) {
            return sParameterName[1];
        }
    }
}

function jIdEscape (str) {
    return str.replace(/\./g, "\\.");
}

// Highlight page in top nav
function highlightNavLink () {
    var highlightLink,
        lastURISegment = window.location.href.substr(window.location.href.lastIndexOf('/') + 1).split("?")[0];

    if (lastURISegment === "support.html") {
        $(".js-header-link.m-support").addClass("s-active");
    
    } else if (lastURISegment === "examples.html") {
        $(".js-header-link.m-examples").addClass("s-active");
    
    } else {
        $(".js-header-link.m-docs").addClass("s-active");
    }
}

// Remove '#typedef-' headings in the left nav
$(".toctree-l2 a").each(function (index, node) {
    if ($(node).text().startsWith("Typedef:")) {
          $(node).parent(".toctree-l2").remove();
            }
});

$(document).ready(function () {
    highlightNavLink();

    // Remove hrefs to #object
    $("[href='#object']").each(function () {
      var link = $(this);
      var linkParent = link.parent();
      var text = link.find(".pre").clone();
      link.remove();
      linkParent.append(text);
    });

    // Scroll sidebar to location in URL query string
    if (getQueryStringParams("navScrollTop")) {
        $(".wy-nav-side").scrollTop(getQueryStringParams("navScrollTop"));
    }

    var header_height = $('header#mlab-header').height();

//    function scroll_to_id(id) {
//        var elem = $(jIdEscape(id));
//        if (elem) {
//            $('html, body').scrollTop(elem.offset().top - header_height - 20);
//        }
//    }

    $(".wy-nav-side a").click(function (event, node) {
        event.preventDefault();

        var targetHref = $(event.target).attr("href");

        if ((event.metaKey || event.ctrlKey) && targetHref) {
            window.open(targetHref);
            return;
        }

        if (this.hash && this.hash.startsWith('#')) {
            if (history.pushState) {
                history.pushState(null, null, this.hash);
                //scroll_to_id(this.hash);

            } else {
                location.hash = this.hash;
            }
        
        } else {
            var scrollTop = $(".wy-nav-side").scrollTop();

            if (scrollTop) {
                href = targetHref + "?navScrollTop=" + scrollTop;
            
            } else {
                href = targetHref;
            }

            window.location.href = href;
        }
    });

    // Override default action on link elements when the href is an anchor.
    // Avoid the hashchange event altogether, as it will flicker -- scroll to
    // where the browser thinks we should be first, then our real position via
    // the call to scroll_to_id
/*    $('.wy-nav-content a').on('click', function (event) {
        if (this.hash && this.hash.startsWith('#')) {
            if (history.pushState) {
                history.pushState(null, null, this.hash);
                //scroll_to_id(this.hash);
            }
            else {
                location.hash = this.hash;
            }
            event.preventDefault();
        }
    });*/

    // Triger after timeout because we can't prevent the default action of a
    // hashchange on page load
/*    $(window).on('hashchange', function () {
        setTimeout(function () { scroll_to_id(window.location.hash) }, 25);
    });

    // Initial trigger, if there is a hash in the URL
    if (window.location.hash) {
        setTimeout(function () { scroll_to_id(window.location.hash) }, 25);
    }*/

    // Mobile menu
    $('header#mlab-header div.mobile-menu a').on('click', function(event) {
        $('header#mlab-header').toggleClass('shift');
        event.preventDefault();
    });

    $(".js-toggle-sidebar").click(function (e, node) {
        setTimeout(function(){
            $(".wy-nav-side").toggleClass("s-visible");
            $(".js-toggle-sidebar").toggleClass("s-open");
        }, 10)
    });

    $(".wy-nav-side").click(function (e) {
        e.stopPropagation();
    });

    $("body").click(function () {
        $(".wy-nav-side").removeClass("s-visible");
        $(".js-toggle-sidebar").removeClass("s-open");
    });

    // Override scrolling from theme
    SphinxRtdTheme.StickyNav.onScroll = function () {};

    // Syntax highlighting for '$' or '%' in shell code blocks.
    $(".highlight-sh pre").each(function (i, el) {
        $(el).html(function (i, html) {
            return html.replace(/(\$ |\% )/g, '<span class="sh-first-char">$1</span>');
        });
    });
});
