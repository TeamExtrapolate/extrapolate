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


    function init() {
        yCoords();
        $(document).scroll(scrollAnimate);
    }

    return {
        init : init,
    };
})();
