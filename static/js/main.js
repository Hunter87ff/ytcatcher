function sel(id_class){return document.querySelector(id_class);}
function selAll(id_class){return document.querySelectorAll(id_class);}

var sbtn = sel('#search_btn');

function Search(){
        sbtn.innerHTML = 'Fetching...';
        sbtn.style.background = 'green';
}