const SitemapGenerator = require('sitemap-generator');

  // create generator
  const generator = SitemapGenerator('https://meraki.cisco.com', {
    maxDepth: 0,
  filepath: './sitemap.xml',
  maxEntriesPerFile: 50000,
  stripQuerystring: true
  });
  
  // register event listeners
  generator.on('done', () => {
    // sitemaps created
    console.log('done');
  });
  
  generator.on('add', (url) => {
    console.log(url);
  });

  // start the crawler
  generator.start(function()
  {console.log('Start');
});