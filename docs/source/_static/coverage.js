/*
 * SATRE Coverage & Mappings page.
 *
 * Fetches the build-time tag sidecar (_static/spec-tags.json) and renders an
 * interactive view: pick standards / patterns / products, and see which SATRE
 * requirements are covered by the selection and which are not.
 *
 * No external dependencies. CSV export is built by hand (zero-dependency).
 */
(function () {
  "use strict";

  var MATCH_MODE_UNION = "union"; // covered if matched by ANY selected tag
  var MATCH_MODE_INTERSECTION = "intersection"; // covered if matched by ALL selected tags

  // -- small DOM helpers ------------------------------------------------------

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        if (k === "class") node.className = attrs[k];
        else if (k === "text") node.textContent = attrs[k];
        else if (k === "html") node.innerHTML = attrs[k];
        else node.setAttribute(k, attrs[k]);
      });
    }
    (children || []).forEach(function (c) {
      if (c == null) return;
      node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    });
    return node;
  }

  function clear(node) {
    while (node.firstChild) node.removeChild(node.firstChild);
  }

  // -- tag identity -----------------------------------------------------------
  // A "tag" the user can filter on is one of:
  //   standard:<framework>, pattern:<name>, product:<name>
  // We build the set of available tags from the data, and for each requirement
  // the set of tag-ids it carries.

  function tagId(type, label) {
    return type + ":" + label;
  }

  function requirementTagIds(req) {
    var ids = [];
    (req.standards || []).forEach(function (s) {
      ids.push(tagId("standard", s.framework));
    });
    (req.patterns || []).forEach(function (p) {
      ids.push(tagId("pattern", p.name));
    });
    (req.products || []).forEach(function (p) {
      ids.push(tagId("product", p.name));
    });
    return ids;
  }

  // -- state ------------------------------------------------------------------

  var state = {
    data: null,
    selected: {}, // tagId -> true
    mode: MATCH_MODE_UNION,
    exportScope: "filtered", // "filtered" (covered only) | "all"
  };

  // -- build the list of selectable tags with counts --------------------------

  function collectTags(data) {
    var groups = { standard: {}, pattern: {}, product: {} };
    data.requirements.forEach(function (req) {
      (req.standards || []).forEach(function (s) {
        groups.standard[s.framework] = (groups.standard[s.framework] || 0) + 1;
      });
      (req.patterns || []).forEach(function (p) {
        groups.pattern[p.name] = (groups.pattern[p.name] || 0) + 1;
      });
      (req.products || []).forEach(function (p) {
        groups.product[p.name] = (groups.product[p.name] || 0) + 1;
      });
    });
    function toSorted(obj) {
      return Object.keys(obj)
        .sort(function (a, b) {
          return a.toLowerCase().localeCompare(b.toLowerCase());
        })
        .map(function (label) {
          return { label: label, count: obj[label] };
        });
    }
    return {
      standard: toSorted(groups.standard),
      pattern: toSorted(groups.pattern),
      product: toSorted(groups.product),
    };
  }

  // -- coverage computation ---------------------------------------------------

  function selectedIds() {
    return Object.keys(state.selected).filter(function (k) {
      return state.selected[k];
    });
  }

  function computeCoverage() {
    var sel = selectedIds();
    var covered = [];
    var notCovered = [];
    var matchMap = {}; // requirement_index -> [tagId, ...] that matched

    state.data.requirements.forEach(function (req) {
      if (sel.length === 0) {
        // With no selection, nothing is "covered" by the (empty) filter.
        notCovered.push(req);
        return;
      }
      var reqTags = requirementTagIds(req);
      var matched = sel.filter(function (id) {
        return reqTags.indexOf(id) !== -1;
      });
      var isCovered =
        state.mode === MATCH_MODE_UNION
          ? matched.length > 0
          : matched.length === sel.length;
      if (isCovered) {
        matchMap[req.requirement_index] = matched;
        covered.push(req);
      } else {
        notCovered.push(req);
      }
    });
    return { covered: covered, notCovered: notCovered, matchMap: matchMap };
  }

  // -- rendering: filter controls --------------------------------------------

  function renderFilters(root, tags) {
    var TYPES = [
      { key: "standard", title: "Standards" },
      { key: "pattern", title: "Patterns" },
      { key: "product", title: "Products" },
    ];

    var panel = el("div", { class: "coverage-filters" });

    TYPES.forEach(function (t) {
      var items = tags[t.key];
      var group = el("fieldset", { class: "coverage-filter-group" }, [
        el("legend", { text: t.title + " (" + items.length + ")" }),
      ]);
      if (items.length === 0) {
        group.appendChild(
          el("p", { class: "coverage-empty", text: "None tagged yet." }),
        );
      }
      items.forEach(function (item) {
        var id = tagId(t.key, item.label);
        var inputId = "flt-" + id.replace(/[^a-z0-9]+/gi, "-");
        var checkbox = el("input", {
          type: "checkbox",
          id: inputId,
          "data-tag-id": id,
        });
        checkbox.checked = !!state.selected[id];
        checkbox.addEventListener("change", function () {
          state.selected[id] = checkbox.checked;
          update();
        });
        var label = el("label", { for: inputId, class: "coverage-check" }, [
          checkbox,
          el("span", { text: " " + item.label }),
          el("span", { class: "coverage-count", text: " " + item.count }),
        ]);
        group.appendChild(label);
      });
      panel.appendChild(group);
    });

    // Controls row: match mode + clear + export.
    var controls = el("div", { class: "coverage-controls" });

    var modeWrap = el("div", { class: "coverage-mode" }, [
      el("span", { class: "coverage-mode-label", text: "Match: " }),
    ]);
    [
      { v: MATCH_MODE_UNION, t: "Any (OR)" },
      { v: MATCH_MODE_INTERSECTION, t: "All (AND)" },
    ].forEach(function (opt) {
      var rid = "mode-" + opt.v;
      var radio = el("input", {
        type: "radio",
        name: "coverage-mode",
        id: rid,
        value: opt.v,
      });
      radio.checked = state.mode === opt.v;
      radio.addEventListener("change", function () {
        if (radio.checked) {
          state.mode = opt.v;
          update();
        }
      });
      modeWrap.appendChild(
        el("label", { class: "coverage-radio", for: rid }, [
          radio,
          el("span", { text: " " + opt.t }),
        ]),
      );
    });
    controls.appendChild(modeWrap);

    var clearBtn = el("button", {
      type: "button",
      class: "coverage-btn",
      text: "Clear selection",
    });
    clearBtn.addEventListener("click", function () {
      state.selected = {};
      panel.querySelectorAll('input[type="checkbox"]').forEach(function (cb) {
        cb.checked = false;
      });
      update();
    });
    controls.appendChild(clearBtn);

    // Export scope + button.
    var scopeSelect = el(
      "select",
      { class: "coverage-scope", title: "What to export" },
      [
        el("option", { value: "filtered", text: "Covered only" }),
        el("option", { value: "all", text: "All requirements" }),
      ],
    );
    scopeSelect.value = state.exportScope;
    scopeSelect.addEventListener("change", function () {
      state.exportScope = scopeSelect.value;
    });
    var exportBtn = el("button", {
      type: "button",
      class: "coverage-btn coverage-btn-primary",
      text: "Export CSV",
    });
    exportBtn.addEventListener("click", exportCsv);
    var exportWrap = el("div", { class: "coverage-export" }, [
      el("span", { text: "Export: " }),
      scopeSelect,
      exportBtn,
    ]);
    controls.appendChild(exportWrap);

    panel.appendChild(controls);
    root.appendChild(panel);
  }

  // -- rendering: results -----------------------------------------------------

  function badge(text, cls) {
    return el("span", { class: "coverage-badge " + (cls || ""), text: text });
  }

  function maturityLabel(trl) {
    var labels = (state.data && state.data.maturity_labels) || {};
    var lbl = labels[String(trl)];
    return "TRL " + trl + (lbl ? " – " + lbl : "");
  }

  function renderRequirement(req, matchedIds) {
    var head = el("div", { class: "coverage-req-head" }, [
      el("span", { class: "coverage-req-ref", text: req.requirement_index }),
      el("span", {
        class: "coverage-req-importance " + importanceClass(req.importance),
        text: req.importance || "",
      }),
      el("span", {
        class: "coverage-req-statement",
        text: req.statement || "",
      }),
    ]);

    var tagWrap = el("div", { class: "coverage-req-tags" });

    (req.standards || []).forEach(function (s) {
      var id = tagId("standard", s.framework);
      var hit = matchedIds && matchedIds.indexOf(id) !== -1;
      tagWrap.appendChild(
        badge(
          s.framework + (s.reference ? " · " + s.reference : ""),
          "coverage-badge-standard" + (hit ? " coverage-badge-hit" : ""),
        ),
      );
    });
    (req.patterns || []).forEach(function (p) {
      var id = tagId("pattern", p.name);
      var hit = matchedIds && matchedIds.indexOf(id) !== -1;
      var parts = [p.name];
      if (p.coverage) parts.push(p.coverage);
      if (p.status) parts.push(p.status);
      tagWrap.appendChild(
        mkTagBadge(
          parts.join(" · "),
          "coverage-badge-pattern" + (hit ? " coverage-badge-hit" : ""),
          p.url,
        ),
      );
    });
    (req.products || []).forEach(function (p) {
      var id = tagId("product", p.name);
      var hit = matchedIds && matchedIds.indexOf(id) !== -1;
      var cls = "coverage-badge-product" + (hit ? " coverage-badge-hit" : "");
      if (p.local_process) {
        // Special "met by a local process" tag; no coverage/maturity to show.
        tagWrap.appendChild(
          mkTagBadge(p.name, cls + " coverage-badge-localprocess", p.url),
        );
        return;
      }
      var parts = [p.name];
      if (p.coverage) parts.push(p.coverage);
      if (p.maturity != null && p.maturity !== "")
        parts.push(maturityLabel(p.maturity));
      tagWrap.appendChild(mkTagBadge(parts.join(" · "), cls, p.url));
    });

    var children = [head];
    if (tagWrap.childNodes.length) children.push(tagWrap);
    return el("div", { class: "coverage-req" }, children);
  }

  function mkTagBadge(text, cls, url) {
    if (url) {
      return el("a", {
        class: "coverage-badge " + cls,
        href: url,
        target: "_blank",
        rel: "noopener",
        text: text,
      });
    }
    return badge(text, cls);
  }

  function importanceClass(importance) {
    if (!importance) return "";
    var i = importance.toLowerCase();
    if (i.indexOf("mandatory") === 0) return "imp-mandatory";
    if (i.indexOf("recommended") === 0) return "imp-recommended";
    if (i.indexOf("optional") === 0) return "imp-optional";
    return "";
  }

  function groupByPillar(reqs) {
    var order = [];
    var map = {};
    reqs.forEach(function (r) {
      var key = r.pillar || "Other";
      if (!map[key]) {
        map[key] = {};
        order.push(key);
      }
      var cap =
        (r.capability_index ? r.capability_index + " " : "") +
        (r.capability || "");
      if (!map[key][cap]) map[key][cap] = [];
      map[key][cap].push(r);
    });
    return { order: order, map: map };
  }

  function renderReqGroup(reqs, matchMap) {
    var grouped = groupByPillar(reqs);
    var container = el("div", { class: "coverage-groups" });
    grouped.order.forEach(function (pillar) {
      var pillarNode = el("div", { class: "coverage-pillar" }, [
        el("h3", { class: "coverage-pillar-title", text: pillar }),
      ]);
      var caps = grouped.map[pillar];
      Object.keys(caps).forEach(function (cap) {
        pillarNode.appendChild(
          el("h4", { class: "coverage-cap-title", text: cap }),
        );
        caps[cap].forEach(function (req) {
          pillarNode.appendChild(
            renderRequirement(
              req,
              matchMap ? matchMap[req.requirement_index] : null,
            ),
          );
        });
      });
      container.appendChild(pillarNode);
    });
    return container;
  }

  function renderResults(root) {
    var result = computeCoverage();
    var sel = selectedIds();

    var results = el("div", { class: "coverage-results" });

    var summary = el("div", { class: "coverage-summary" });
    if (sel.length === 0) {
      summary.appendChild(
        el("p", {
          class: "coverage-hint",
          text: "Select one or more tags above to see coverage.",
        }),
      );
    } else {
      summary.appendChild(
        el("p", {
          html:
            "<strong>" +
            result.covered.length +
            "</strong> requirement(s) covered · <strong>" +
            result.notCovered.length +
            "</strong> not covered · matching <em>" +
            (state.mode === MATCH_MODE_UNION ? "any" : "all") +
            "</em> of <strong>" +
            sel.length +
            "</strong> selected tag(s).",
        }),
      );
    }
    results.appendChild(summary);

    if (sel.length > 0) {
      results.appendChild(
        el(
          "details",
          { class: "coverage-section coverage-section-covered", open: "open" },
          [
            el("summary", { text: "Covered (" + result.covered.length + ")" }),
            result.covered.length
              ? renderReqGroup(result.covered, result.matchMap)
              : el("p", {
                  class: "coverage-empty",
                  text: "No requirements match the current selection.",
                }),
          ],
        ),
      );
      results.appendChild(
        el(
          "details",
          { class: "coverage-section coverage-section-notcovered" },
          [
            el("summary", {
              text: "Not covered (" + result.notCovered.length + ")",
            }),
            renderReqGroup(result.notCovered, null),
          ],
        ),
      );
    }

    var existing = root.querySelector(".coverage-results");
    if (existing) existing.parentNode.replaceChild(results, existing);
    else root.appendChild(results);
  }

  // -- CSV export -------------------------------------------------------------

  function csvEscape(value) {
    var s = value == null ? "" : String(value);
    if (/[",\n\r]/.test(s)) {
      return '"' + s.replace(/"/g, '""') + '"';
    }
    return s;
  }

  function exportCsv() {
    var result = computeCoverage();
    var rows =
      state.exportScope === "all" ? state.data.requirements : result.covered;

    var header = [
      "requirement_index",
      "pillar",
      "capability",
      "importance",
      "statement",
      "covered",
      "matched_tags",
      "standards",
      "patterns",
      "products",
    ];

    function joinStandards(req) {
      return (req.standards || [])
        .map(function (s) {
          return s.framework + (s.reference ? " (" + s.reference + ")" : "");
        })
        .join("; ");
    }
    function joinPatterns(req) {
      return (req.patterns || [])
        .map(function (p) {
          var meta = [p.coverage, p.status].filter(Boolean).join("/");
          return p.name + (meta ? " [" + meta + "]" : "");
        })
        .join("; ");
    }
    function joinProducts(req) {
      return (req.products || [])
        .map(function (p) {
          if (p.local_process) return p.name;
          var meta = [];
          if (p.coverage) meta.push(p.coverage);
          if (p.maturity != null && p.maturity !== "")
            meta.push("TRL" + p.maturity);
          return p.name + (meta.length ? " [" + meta.join("/") + "]" : "");
        })
        .join("; ");
    }

    var coveredSet = {};
    result.covered.forEach(function (r) {
      coveredSet[r.requirement_index] = true;
    });

    var lines = [header.map(csvEscape).join(",")];
    rows.forEach(function (req) {
      var matched = result.matchMap[req.requirement_index] || [];
      var line = [
        req.requirement_index,
        req.pillar,
        req.capability,
        req.importance,
        req.statement,
        coveredSet[req.requirement_index] ? "yes" : "no",
        matched.join(" | "),
        joinStandards(req),
        joinPatterns(req),
        joinProducts(req),
      ];
      lines.push(line.map(csvEscape).join(","));
    });

    var csv = "\ufeff" + lines.join("\r\n"); // BOM for Excel compatibility
    var blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    var url = URL.createObjectURL(blob);
    var a = el("a", {
      href: url,
      download: "satre-coverage-" + state.exportScope + ".csv",
    });
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () {
      URL.revokeObjectURL(url);
    }, 0);
  }

  // -- lifecycle --------------------------------------------------------------

  var appRoot;
  var filtersRendered = false;

  function update() {
    renderResults(appRoot);
  }

  function init() {
    appRoot = document.getElementById("coverage-app");
    if (!appRoot) return;

    var url = appRoot.getAttribute("data-tags-url") || "_static/spec-tags.json";

    fetch(url)
      .then(function (resp) {
        if (!resp.ok) throw new Error("HTTP " + resp.status);
        return resp.json();
      })
      .then(function (data) {
        state.data = data;
        clear(appRoot);
        var tags = collectTags(data);
        renderFilters(appRoot, tags);
        filtersRendered = true;
        renderResults(appRoot);
      })
      .catch(function (err) {
        clear(appRoot);
        appRoot.appendChild(
          el("p", {
            class: "coverage-error",
            text: "Could not load coverage data (" + err.message + ").",
          }),
        );
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
