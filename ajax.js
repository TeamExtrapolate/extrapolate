/**
 * Copyright 2018 Team Extrapolate Authors. All Rights Reserved..
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
var ajax_req = function() {
    function a(a) {
        a.preventDefault();
        b = "/";
        c = new FormData(this);
        $.ajax({
            url: b,
            type: "POST",
            data: c,
            contentType: !1,
            processData: !1,
            dataType: "json",
            success: function() {},
            error: function() {}
        });
    }
    var b, c;
    return {
        init: function() {
            document.getElementsById("").addEventListener("submit", a);
        }
    };
}();