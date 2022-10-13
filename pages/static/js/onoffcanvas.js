/*!
* onoffcanvas - v2.2.4
* An offcanvas plugin
* https://github.com/onokumus/onoffcanvas
*
* Made by onokumus <onokumus@gmail.com> (https://github.com/onokumus)
* Under MIT License
*/
!function(t,e){"object"==typeof exports&&"undefined"!=typeof module?module.exports=e():"function"==typeof define&&define.amd?define(e):(t=t||self).OnoffCanvas=e()}(this,function(){"use strict";
/*! *****************************************************************************
    Copyright (c) Microsoft Corporation. All rights reserved.
    Licensed under the Apache License, Version 2.0 (the "License"); you may not use
    this file except in compliance with the License. You may obtain a copy of the
    License at http://www.apache.org/licenses/LICENSE-2.0

    THIS CODE IS PROVIDED ON AN *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED
    WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR PURPOSE,
    MERCHANTABLITY OR NON-INFRINGEMENT.

    See the Apache Version 2.0 License for specific language governing permissions
    and limitations under the License.
    ***************************************************************************** */var i=function(){return(i=Object.assign||function(t){for(var e,n=1,i=arguments.length;n<i;n++)for(var r in e=arguments[n])Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r]);return t}).apply(this,arguments)},t=".onoffcanvas",n={HIDE:"hide"+t,SHOW:"show"+t},r="is-open",o='[data-toggle="onoffcanvas"]',a={createDrawer:!0,hideByEsc:!0};function c(t){var e=t.getAttribute("data-target");e&&"#"!==e||(e=t.getAttribute("href")||"");try{return 0<document.querySelectorAll(e).length?e:null}catch(t){throw new Error("Target Not Found!")}}function d(t,e){var n=this;this.element=Boolean(t.classList)?t:document.querySelector(t),this.config=i(i({},a),e),this.triggerElements=[].slice.call(document.querySelectorAll(o+'[href="#'+this.element.id+'"],\n      '+o+'[data-target="#'+this.element.id+'"]')),this.addAriaExpanded(this.triggerElements),this.triggerElements.forEach(function(t){t.addEventListener("click",function(t){var e=t.target;e&&"A"===e.tagName&&t.preventDefault(),n.toggle()})}),this.drawer=document.createElement("div"),this.drawer.classList.add("onoffcanvas-drawer"),document.documentElement.appendChild(this.drawer)}return d.attachTo=function(t,e){return new d(t,e)},d.autoinit=function(t){void 0===t&&(t=a);for(var e=document.querySelectorAll(""+o),n=function(t){for(var e=[],n=0,i=t;n<i.length;n++){var r=c(i[n]);e.push(r)}return e}([].slice.call(e)),i=0,r=n.filter(function(t,e,n){return e===n.indexOf(t)});i<r.length;i++){var s=r[i];d.attachTo(s,t)}},d.prototype.on=function(t,e){return this.listen(t,e),this},d.prototype.toggle=function(){this.element.classList.contains(r)?this.hide():this.show()},d.prototype.show=function(){var e=this;this.element.classList.contains(r)||(this.element.classList.add(r),this.addAriaExpanded(this.triggerElements),this.emit(n.SHOW,this.element),this.config.createDrawer&&(this.drawer.classList.add("is-open"),this.drawer.addEventListener("click",this.hide.bind(this))),this.config.hideByEsc&&window.addEventListener("keydown",function(t){27===t.keyCode&&e.hide()}))},d.prototype.hide=function(){this.element.classList.contains(r)&&(this.config.createDrawer&&(this.drawer.classList.remove("is-open"),this.drawer.removeEventListener("click",this.hide.bind(this))),this.element.classList.remove(r),this.addAriaExpanded(this.triggerElements),this.emit(n.HIDE,this.element))},d.prototype.listen=function(t,e){return this.element.addEventListener(t,e,!1),this},d.prototype.emit=function(t,e,n){var i;return void 0===n&&(n=!1),"function"==typeof CustomEvent?i=new CustomEvent(t,{bubbles:n}):(i=document.createEvent("CustomEvent")).initCustomEvent(t,n,!1,e),this.element.dispatchEvent(i),this},d.prototype.addAriaExpanded=function(t){var n=this.element.classList.contains(r);Array.prototype.forEach.call(t,function(t,e){t.setAttribute("aria-expanded",n?"true":"false")})},d});