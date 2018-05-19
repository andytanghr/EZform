var dataCacheName = 'EZform-v1';
var cacheName = 'EZformPWA-1';
var filesToCache = [];

self.addEventListener('install', e => {
  console.log('Service worker installing');
  e.waitUntil(
    caches.open(cacheName).then( cache => {
      console.log('Service worker caching app shell');
      return cache.addAll(filesToCache);
    })
  );
});


self.addEventListener('activate', e => {
  console.log('Service worker activating');
  e.waitUntil(
    caches.keys().then( keyList => {
      return Promise.all(keyList.map( key => {
        if (key !== cacheName && key !== dataCacheName) {
          console.log('Service worker removing old cache');
          return caches.delete(key);
        }
      }));
    })
  );
  return self.clients.claim();
});


self.addEventListener('fetch', e => {
  console.log('Service worker fetching', e.request.url);
  var dataUrl = '' // point to Django?
  if (e.request.url.indexOf(dataUrl) > -1) {
    e.respondWith(
      caches.open(dataCacheName).then( cache => {
        return fetch(e.request).then( response => {
          cache.put(e.request.url, response.clone());
          return response;
        });
      })
    );
  } else {
    e.respondWith(
      cache.match(e.request).then( response => {
        return response || fetch(e.request);
      })
    );
  }
});