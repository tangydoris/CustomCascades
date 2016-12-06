var storage = chrome.storage.local;
var popularButton = document.getElementById('popular');
var recentButton = document.getElementById('recent');
var idButton = document.getElementById('fileId');
var idInput = document.querySelector('input.idInput');
var saveButton = document.getElementById('saveHost')
var hostInput = document.querySelector('input.nameInput');
popularButton.addEventListener('click', toggleChosen.bind(popularButton));
recentButton.addEventListener('click', toggleChosen.bind(recentButton));
idButton.addEventListener('click', toggleChosen.bind(idButton));
saveButton.addEventListener('click', save);

function load() {
    storage.get({'ccHosts': []}, function (items) {
        var hosts = items.ccHosts;
        for (var i = 0; i < hosts.length; i++) {
            appendSaved(hosts[i].host, hosts[i].spec);
        }
    });
}

function save() {
    var host = hostInput.value;
    hostInput.value = '';
    storage.get('ccHosts', function(items) {
        var hosts = items.ccHosts;
        if (!hosts) {
            hosts = [];
        }
        var spec = 'popular'; //default
        var id = '';
        if (recentButton.classList.contains('chosen')) {
            spec = 'recent';
        } else if (idButton.classList.contains('chosen')) {
            spec = 'id';
            id = idInput.value;
        }
        idInput.value = '';
        recentButton.classList.remove('chosen');
        popularButton.classList.remove('chosen');
        idButton.classList.remove('chosen');
        hosts.push({'host':host, 'spec': spec, 'id': id});
        storage.set({'ccHosts': hosts}, function() {
            appendSaved(host, spec);
        });
    });
}

function remove() {
    var host = this.host;
    storage.get('ccHosts', function(items) {
        var hosts = items.ccHosts;
        if (!hosts) {
            return;
        }
        for (var i = 0; i < hosts.length; i++) {
            if (hosts[i].host == host) {
                break;
            }
        }
        hosts.splice(i, 1);
        storage.set({'ccHosts': hosts}, function() {
            var element = document.getElementById(host);
            element.parentElement.removeChild(element);
        });
    });
}

function toggleChosen() {
    popularButton.classList.remove('chosen');
    recentButton.classList.remove('chosen');
    idButton.classList.remove('chosen');
    this.classList.add('chosen');
}

function appendSaved(host, spec) {
    var div = document.createElement('div');
    div.classList.add('savedHost');
    document.getElementById('saved').appendChild(div);
    div.id = host;
    var hostElement = document.createElement('p');
    hostElement.classList.add('hostTitle');
    hostElement.textContent = host;
    var specText = document.createElement("span");
    specText.classList.add('specText');
    specText.textContent = " - " + spec;
    hostElement.appendChild(specText);
    div.appendChild(hostElement);
    var removeButton = document.createElement('button');
    removeButton.host = host;
    removeButton.addEventListener('click', remove.bind(removeButton));
    removeButton.textContent = 'Remove';
    removeButton.classList.add('remove');
    div.appendChild(removeButton);
}

load();
