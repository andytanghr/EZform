( () => {



// register service worker
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker
      .register('sw.js')
      .then( registration => { console.log('Service worker registered with scope ', registration.scope);
    }, err => {
      console.log('Service worker failed to register: ', err);
    });
  
}


})();