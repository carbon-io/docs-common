
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

function wrap(el, wrapper) {
    el.parentNode.insertBefore(wrapper, el);
    wrapper.appendChild(el);
}

function addTocItems() {
  var refList = $(".attribute dt, .function dt, .rubric");
  var sortObject = {}
  var $tocList = $("<ul id=\"pageTocTable\"></ul>")

  refList.each(function () {
    var id = $(this).attr("id")
    var className = $(this)[0].className
    if (id != undefined) {
     if (id.split(".").length > 1 || className == "rubric") {
       if (className == "rubric") {
        var displayId = $(this)[0].innerText.split("Typedef: ")[1]
        var $tocLink = $("<li class='toctree-l3'><a href='#" + id + "' class='reference internal'>" + displayId + "</a></li>");
        sortObject[displayId] = $tocLink
       } else {
         var displayId = $(this).attr("id")
         if (displayId != undefined) {
          displayId = displayId.split(".").pop();
          var $tocLink = $("<li class='toctree-l3'><a href='#" + id + "' class='reference internal'>" + displayId + "</a></li>");
          sortObject[displayId] = $tocLink
         }
       }
     }
    }
  })

  // sort the left nav links before writing to the $tocList, using the displayId as the key
  var keys = []
  for (var key in sortObject) {
    keys.push(key)
  }
  keys.sort(function (a, b) {
        return a.toLowerCase().localeCompare(b.toLowerCase());
  })

  for(var x = 0; x < keys.length; x++) {
    $tocList.append(sortObject[keys[x]])
  }

  return $tocList;
}

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


function updateVersionDropdown () {
    var $versionsList = $(".rst-other-versions dl:first-child")
    $(".rst-other-versions dl").remove()
    $(".rst-other-versions").append($versionsList)
}


// Props/Methods Table formatting: InheritedFrom
function updateInheritedFromProp () {
    $(".details-table").each(function () {
        var $table = $(this)

        $table.find("td").each(function () {
            var $this = $(this);
            if ($this.text().toLowerCase() === "inheritedfrom") {
                var $parent = $this.parent()
                var $siblingHtml = $($this.siblings()[0]).html()

                $parent.remove()

                $table.find(".annotate-field:last-of-type").after("<em class='inherited-from-prop' style='margin-left: 1rem;'>Inherited from </em>" + $siblingHtml)
            }
        });
    });
}

function addMobileTableTitle () {
    $(".details-table").each(function () {
        var $this = $(this)
        var $clone = $this.find("tr:first-of-type td:first-of-type").clone()
        $clone.addClass("mobile-prop-title")

        $this.before($clone)
    })
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


$(document).ready(function () {
    highlightNavLink();

    $(".toctree-l2.current").append(addTocItems());

    if (window.location.pathname.search("ref") !== -1) {
      // "ref" cross references (used for Typedefs) in rst do not wrap in a code class
      // so we have to do that manually
	  var typedefRefs = document.getElementsByClassName("std std-ref");

	  for(var z = 0; z < typedefRefs.length; z++) {
        console.log(typedefRefs[z])
        wrap(typedefRefs[z], document.createElement('code'))
      }
    }

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
        }, 20);
    }

    var header_height = $('#mlab-header').height();

    $(".wy-nav-side a").click(function (event, node) {
        var targetHref = $(event.target).attr("href");

		var pageTocTable = document.getElementById("pageTocTable")

		if($(event.target).attr("class") == "current reference internal") {
			if(pageTocTable.style.display === "none") {
			  pageTocTable.style.display = "block"
			} else {
			  pageTocTable.style.display = "none"
			}
        }

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

    updateInheritedFromProp()
    addMobileTableTitle()
    updateVersionDropdown()
});
