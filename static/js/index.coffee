loadExample = (loadExampleName) ->
	if ga?
		ga("send", "pageview", "/iterations/#{loadExampleName}")

	$("#code").attr "src", "code.html?name=#{loadExampleName}"
	$("#example").attr "src", "iteration.html?name=#{loadExampleName}"
	$("a.download").attr "href", "/static/iterations/#{loadExampleName}.zip"

$(window).load ->
	loadExampleName = window.location.hash[1..]
	loadExample loadExampleName	

$(document).ready ->
	
	showExample = (exampleName) ->
		if ga?
			ga("send", "pageview", "/iterations/#{exampleName}")
	
		$("#code").attr "src", "code.html?name=#{exampleName}"
		$("#example").attr "src", "iteration.html?name=#{exampleName}"
		$("a.download").attr "href", "/static/iterations/#{exampleName}.zip"
			
	if not window.location.hash[1..]
		window.location.hash = "carousel-onboarding.framer"
		loadExample "carousel-onboarding.framer"	
			
	$(".navigation ul li a").click ->
	
		exampleName = $(@).attr("href")[1..]
		showExample exampleName	
		
		$(".navigation ul li").removeClass "active"
		$(@).parent().addClass "active"

		$(".navigation").removeClass "appear"
		$('#topbar').removeClass "active"
			
		
	$('#topbar img').click ->
	    $(".navigation").toggleClass "appear"
	    $('#topbar').toggleClass "active"
	    
	 



	
	

