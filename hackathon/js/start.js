var start = (function() { 
    
    function takeAction () {
        $("#intro").addClass("animated");
        $("#intro").addClass("fadeOutUp");
    }

    function init() {
        $(".web-enter").click(takeAction);
    }
    
    return {
        init : init,
    };
})();
