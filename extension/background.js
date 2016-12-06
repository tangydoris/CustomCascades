var storage = chrome.storage.local;
chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    if (changeInfo.status == 'complete') {
        chrome.tabs.query({active:true, currentWindow: true}, function(tabs) {
            var host = tabs[0].url.replace('https://','');
            host = host.replace('http://','');
            host = host.split('/')[0];
            storage.get('ccHosts', function(items) {
                var found = 0;
                var spec = "";
                if (items.ccHosts) {
                    for (var i = 0; i < items.ccHosts.length; i++) {
                        if (items.ccHosts[i].host == host) {
                            found = 1;
                            spec = items.ccHosts[i].spec;
                            break;
                        }
                    }
                }
                if (found) {
                    var req = new XMLHttpRequest();
                    var url = 'http://localhost:8000/css_app/api/';
                    url += host + "/" + spec;
                    req.open('GET', url, true);
                    req.addEventListener('load', function() {
                        var CSS = JSON.parse(req.responseText);
                        if (CSS.css) {
                            chrome.tabs.insertCSS({code: CSS.css}, function() {
                                return;
                            });
                        }
                    });
                    req.send();
                }
            });
        });
    }
});
