(function() {
  var loadExample;

  loadExample = function(loadExampleName) {
    if (typeof ga !== "undefined" && ga !== null) {
      ga("send", "pageview", "/iterations/" + loadExampleName);
    }
    $("#code").attr("src", "code.html?name=" + loadExampleName);
    $("#example").attr("src", "iteration.html?name=" + loadExampleName);
    return $("a.download").attr("href", "/static/iterations/" + loadExampleName + ".zip");
  };

  $(window).load(function() {
    var loadExampleName;
    loadExampleName = window.location.hash.slice(1);
    return loadExample(loadExampleName);
  });

  $(document).ready(function() {
    var showExample;
    showExample = function(exampleName) {
      if (typeof ga !== "undefined" && ga !== null) {
        ga("send", "pageview", "/iterations/" + exampleName);
      }
      $("#code").attr("src", "code.html?name=" + exampleName);
      $("#example").attr("src", "iteration.html?name=" + exampleName);
      return $("a.download").attr("href", "/static/iterations/" + exampleName + ".zip");
    };
    if (!window.location.hash.slice(1)) {
      window.location.hash = "gallery_0.0.1.framer";
      loadExample("gallery_0.0.1.framer");
    }
    $(".navigation ul li a").click(function() {
      var exampleName;
      exampleName = $(this).attr("href").slice(1);
      showExample(exampleName);
      $(".navigation ul li").removeClass("active");
      $(this).parent().addClass("active");
      $(".navigation").removeClass("appear");
      return $('#topbar').removeClass("active");
    });
    return $('#topbar img').click(function() {
      $(".navigation").toggleClass("appear");
      return $('#topbar').toggleClass("active");
    });
  });

}).call(this);
