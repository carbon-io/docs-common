
var list = $(".arguments-field .simple");
var listItems = list.children();
listItems.each(function (index, node) {
  var $potentialParent = $(node);
  var text = $potentialParent.find("strong").text();
  var props = [];


  for (var i = index; i < listItems.length; i++) {
    var $siblingNode = $(listItems[i]);

    var nodeText = $siblingNode.find("strong").text();

    if (nodeText.startsWith(text + ".")) {
      props.push($siblingNode);
    }
  }

  var tableRows = [];
  props.forEach(function (item, index) {
    var $node = $(item);

    var tableInfo = {};

    var $strong = $node.find("strong");
    tableInfo.title = $strong.text();
    tableInfo.title = tableInfo.title.split(".").slice(-1)[0]

    var $strongParent = $strong.parent()
    if ($strongParent.is("a")) {
      tableInfo.titleHref = $strongParent.attr("href");
    }

    $strong.remove();


    var $em = $node.find("em");
    if (!$em[0]){
      $em = $node.find("code");
      tableInfo.typeEl = "code";
    }
    tableInfo.type = $em.text();

    var $emParent = $em.parent()
    if ($emParent.is("a")) {
      tableInfo.typeHref = $emParent.attr("href");
    } else if ($emParent.is("code")){
      var $emParentParent = $emParent.parent()
      if ($emParentParent.is("a")) {
        tableInfo.typeHref = $emParentParent.attr("href");
      }
    }
    
    $em.remove();


    tableInfo.description = $node.text();
    tableInfo.description = tableInfo.description.replace("() – ", "");
    $node.remove();
    tableRows.push(tableInfo);
  });
  if (tableRows.length) {
    renderPropsTable(tableRows, $potentialParent);
  }
});

function renderPropsTable (rows, parent) {
  var $table = $("<table><tbody></tbody></table>");

  rows.forEach(function (item, index) {
    var $row = $("<tr></tr>");

    if (item.titleHref) {
      $row.append($("<td><a href='" + item.titleHref + "'>" + item.title + "</a></td>"));
    } else {
      $row.append($("<td>" + item.title + "</td>"));
    }
    
    if (item.typeEl == "code") {
      if (item.typeHref) {
        $row.append($("<td><code><a href='" + item.typeHref + "'>" + item.type + "</a></code></td>"));
      } else {
        $row.append($("<td><code>" + item.type + "</code></td>"));
      }
    } else {
      if (item.typeHref) {
        $row.append($("<td><a href='" + item.typeHref + "'>" + item.type + "</a></td>"));
      } else {
        $row.append($("<td>" + item.type + "</td>"));
      }
	}
    $row.append($("<td>" + item.description + "</td>"));

    $table.find("tbody").append($row);
  });

  var $listItem = $("<li></li>").append($table[0]);

  $(parent).after($listItem);
}


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

    // Remove hrefs to #object (TODO: why are these happening?)
    $("[href$='#object']").replaceWith(function() {
      return $('*', this);
    })

    // Scroll sidebar to location in URL query string
    if (getQueryStringParams("navScrollTop")) {
        $(".wy-nav-side").scrollTop(getQueryStringParams("navScrollTop"));
    }

    if (location.hash) {
        adjustScrollPosition();
    }

    function adjustScrollPosition () {
        setTimeout(function () {
            var $document = $(document)

            var adjustedScrollHeight = $document.scrollTop() - header_height;
            $document.scrollTop(adjustedScrollHeight);
            console.log(adjustedScrollHeight);
        }, 20);
    }

    var header_height = $('#mlab-header').height();

    $(".wy-nav-side a").click(function (event, node) {
        var targetHref = $(event.target).attr("href");

        if ((event.metaKey || event.ctrlKey) && targetHref) {
            window.open(targetHref);
            return;
        }

        if (this.hash && this.hash.startsWith('#')) {
            if (history.pushState) {
                history.pushState(null, null, this.hash);

                adjustScrollPosition();
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


    $("table.docutils").find("colgroup").remove();
});
