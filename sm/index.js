var express = require('express')
  , sm = require('sitemap');

  

var app = express()
  , sitemap = sm.createSitemap ({
      hostname: 'https://meraki.cisco.com',
      cacheTime: 600000,        // 600 sec - cache purge period
      urls: [
        { url: '/products/',  changefreq: 'daily', priority: 0.3 }
      ]
    });

app.get('/sitemap.xml', function(req, res) {
  sitemap.toXML( function (err, xml) {
      if (err) {
        return res.status(500).end();
      }
      res.header('Content-Type', 'application/xml');
      res.send( xml );
  });
});

app.listen(3000, function(){
    console.log('Port started at 3000');
});