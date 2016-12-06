var storage = chrome.storage.local;
var popularButton = document.querySelector('button.popular');
var recentButton = document.querySelector('button.recent');
var hostInput = document.querySelector('input.nameInput');
popularButton.addEventListener('click', save.bind(popularButton));
recentButton.addEventListener('click', save.bind(recentButton));
var message = document.querySelector('.message');

function load() {
    storage.get({'ccHosts': []}, function (result) {
        var hosts = result.ccHosts;
        for (var i = 0; i < hosts.length; i++) {
            var div = document.createElement('div');
            document.body.appendChild(div);
            div.id = hosts[i].host;
            var hostElement = document.createTextNode(hosts[i].host + " (" + hosts[i].spec + ") ");
            div.appendChild(hostElement);
            var removeButton = document.createElement('button');
            removeButton.host = hosts[i].host;
            removeButton.addEventListener('click', remove.bind(removeButton));
            removeButton.textContent = 'Remove';
            div.appendChild(removeButton);
        }
    });
}

function save() {
    var that = this;
    var hostname = hostInput.value;
    storage.get('ccHosts', function(items) {
        var hosts = items.ccHosts;
        if (!hosts) {
            hosts = [];
        }
        var spec = that.classList[0];
        hosts.push({'host':hostname, 'spec': spec});
        storage.set({'ccHosts': hosts}, function() {
            message.innerText = 'Settings saved for ' + hostname;
            var div = document.createElement('div');
            document.body.appendChild(div);
            div.id = hostname;
            var hostElement = document.createTextNode(hostname + " (" + spec + ") ");
            div.appendChild(hostElement);
            var removeButton = document.createElement('button');
            removeButton.host = hostname;
            removeButton.addEventListener('click', remove.bind(removeButton));
            removeButton.textContent = 'Remove';
            div.appendChild(removeButton);
        });
    });
    hostInput.value = '';
}

function remove() {
    var hostname = this.host;
    storage.get('ccHosts', function(items) {
        var hosts = items.ccHosts;
        if (!hosts) {
            return;
        }
        var i;
        for (var i = 0; i < hosts.length; i++) {
            if (hosts[i].host == hostname) {
                break;
            }
        }
        hosts.splice(i, 1);
        storage.set({'ccHosts': hosts}, function() {
            var element = document.getElementById(hostname);
            element.parentElement.removeChild(element);
            message.innerText = 'removed css';
        });
    });
    hostInput.value = '';
}

load();
