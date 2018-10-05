var gridCells = jQuery('.Grid_grid___2VcYy .Grid_gridCell___1odvN'),
    arr = [],
    i,
    length = gridCells.length,
    html = '';

gridCells.each(function (index, el) {
    var jQueryEl = jQuery(jQuery('.sc-kQsIoO', el)[1]),
        time = jQueryEl.text().replace(' mins', '');

    if (time === 'Preorder') {
        return;
    }

    arr.push({
        time: time,
        el: el
    });
});

arr.sort(function (a, b) {
    return +a.time < +b.time ? -1 : 1;
});

for (i = 0; i < length; i++) {
    if (!arr[i]) {
        break;
    }
    html += arr[i].el.outerHTML;
}



jQuery('.Grid_grid___2VcYy').html(html)
//
//
//
//
//


var jq = document.createElement('script');
jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);
// ... give time for script to load, then type (or see below for non wait option)
jQuery.noConflict();