document.addEventListener("DOMContentLoaded", function() {

var typewritetitle = `NAVERIS`
var typewriteInfo = `NAVERIS Is a Data-driven, Machine Learning Model Which Can Accurately Detect And Give Early Warnings For Incoming Natural Disasters, Potentially saving lives in the process`;
var title = document.getElementById("title");
var info = document.getElementById('info');
title.innerHTML = "";
info.innerHTML = "";
var i = 0;
var j = 0;

function typeTitle() {
    if (i < typewritetitle.length) {
        title.innerHTML += typewritetitle.charAt(i);
        i++;
        setTimeout(typeTitle, 110); 
    }
}

function typeInfo() {
    if (j < typewriteInfo.length) {
        info.innerHTML += typewriteInfo.charAt(j);
        j++;
        setTimeout(typeInfo, 28); 
    }
}

typeTitle();
setTimeout(() => {
    typeInfo();
}, "1300");

});