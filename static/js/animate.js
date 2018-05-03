/**
 * Copyright 2018 Team Extrapolate Authors. All Rights Reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * @emails extrapolate@googlegroups.com
 */
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
        else if(scroll >= (leftCoords[j]-550)) {
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
