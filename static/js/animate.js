var animateControl = (function() { 
    var leftCoords = [];
    var scroll;
    var j=0;

    function yCoords() {
        var leftElements = $('.aml');
        for(var i=0; i<leftElements.length; i++) {
            var temp = leftElements[i].getBoundingClientRect().top;
            leftCoords.push(temp);
        }
    }

    function scrollAnimate() {
        scroll = window.scrollY;
        if(j==leftCoords.length) {
            console.log("p");
        }
        else if(scroll >= (leftCoords[j]-400)) {
            $('.aml')[j].className += " aml-visible animated fadeInLeft";
            $('.amr')[j].className += " amr-visible animated fadeInRight";
            j++;
        }
    }
    function rotateLogo() {
        if($(".small-logo").hasClass("rotate-45-final")) {
            $(".small-logo").removeClass("rotate-45-final");
        }
        else {
            $(".small-logo").addClass("rotate-45-final");   
        }
    }


    function init() {
        yCoords();
        $(document).scroll(scrollAnimate);
        $(".small-logo").click(rotateLogo);
    }
    
    return {
        init : init,
    };
})();
