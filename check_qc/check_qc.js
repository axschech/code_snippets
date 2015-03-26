var http = require('http');
var url = require('url');
var cheerio = require('cheerio');
var fs = require('fs');

var html = "";
var file = 'img.json';
var content = JSON.parse(fs.readFileSync(file, 'utf8'));
var curImg = content['img'];

var work = function () {

    http.get('http://questionablecontent.net', function (response) {
        response.setEncoding('utf8');
        response.on('data', function (chunk) {
            html += chunk;
        });
        response.on('end', function () {
            var $ = cheerio.load(html);
            $('img').each(function (img, test) {
                if (img === 3) {
                    var parsed = url.parse($(test).attr('src'));
                    var pathname = parsed.pathname;
                    var splits = pathname.split('/');
                    var more = splits[2].split('.');
                    var imgNum = more[0];
                    if (parseInt(imgNum) === parseInt(curImg)) {
                        console.log(true);
                    } else {
                        console.log(false);
                        content['img'] = imgNum;
                        fs.writeFileSync(file, JSON.stringify(content), 'utf8');
                        curImg = imgNum;
                    }
                }
            });
        });
    });

};

work();

setInterval(function () {
    work();
}, 10000);
