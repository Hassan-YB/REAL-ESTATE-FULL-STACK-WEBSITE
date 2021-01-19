GMaps.prototype.addStyle = function (options) {
    var styledMapType = new google.maps.StyledMapType(options.styles, options.styledMapName);
    this.map.mapTypes.set(options.mapTypeId, styledMapType);
};

GMaps.prototype.setStyle = function (mapTypeId) {
    this.map.setMapTypeId(mapTypeId);
};



map = new GMaps({
    div: '#map-hero',
    lat: 40.712784,
    lng: -74.005941,
    enableNewStyle: true,
    zoom: 11,
    scrollwheel: false


});
/* Remove comment for geolocation 
GMaps.geolocate({
    success: function (position) {
        map.setCenter(position.coords.latitude, position.coords.longitude);
    },
    error: function (error) {
        alert('Geolocation failed: ' + error.message);
    },
    not_supported: function () {
        alert("Your browser does not support geolocation");
    },
    always: function () {
        alert("We found your location!");
    }
}); */

var styles = [
    {
        stylers: [
            {
                hue: "#0075BF"
            },
            {
                saturation: -20
            }
]
}, {
        featureType: "road",
        elementType: "geometry",
        stylers: [
            {
                lightness: 100
            },
            {
                visibility: "simplified"
            }
]
}, {
        featureType: "road",
        elementType: "labels",
        stylers: [
            {
                visibility: "off"
            }
]
}
];

map.addStyle({
    styledMapName: "Styled Map",
    styles: styles,
    mapTypeId: "map_style"
});

map.setStyle("map_style");



map.addMarker({
    lat: 40.796138,
    lng: -74.060898,
    title: 'Im your custom marker',
    icon: 'images/map-marker-blue.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-8.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});
map.addMarker({
    lat: 40.692093,
    lng: -74.279251,
    title: 'Im your custom marker',
    icon: 'images/map-marker-blue.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-6.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised btn-default">View Listing</a></p></div></div>'
    }
});

map.addMarker({
    lat: 40.688969,
    lng: -74.382248,
    title: 'Im your custom marker',
    icon: 'images/map-marker.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-9.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});

map.addMarker({
    lat: 40.737893,
    lng: -74.206467,
    title: 'Im your custom marker',
    icon: 'images/map-marker-blue.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-4.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});
map.addMarker({
    lat: 40.716038,
    lng: -73.979874,
    title: 'Im your custom marker',
    icon: 'images/map-marker.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-1.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});
map.addMarker({
    lat: 40.676472,
    lng: -73.962021,
    title: 'Im your custom marker',
    icon: 'images/map-marker.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-7.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});
map.addMarker({
    lat: 40.808119,
    lng: -73.88237,
    title: 'Im your custom marker',
    icon: 'images/map-marker.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-6.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});

map.addMarker({
    lat: 40.665015,
    lng: -73.816452,
    title: 'Im your custom marker',
    icon: 'images/map-marker-blue.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-5.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});

map.addMarker({
    lat: 40.725015,
    lng: -73.881452,
    title: 'Im your custom marker',
    icon: 'images/map-marker-blue.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-4.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});

map.addMarker({
    lat: 40.70015,
    lng: -73.81452,
    title: 'Im your custom marker',
    icon: 'images/map-marker-blue.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-2.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});
map.addMarker({
    lat: 40.519019,
    lng: -74.20372,
    title: 'Im your custom marker',
    icon: 'images/map-marker.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-1.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});
map.addMarker({
    lat: 40.660327,
    lng: -74.120979,
    title: 'Im your custom marker',
    icon: 'images/map-marker.png',
    infoWindow: {
        content: '<div class="map-card"><img src="images/home-8.jpg" alt="" class="img-responsive"><div class="card-content"><h3>1B Alexander Court, Lewisham, Tas 7173</h3><p class="price">$390,000 - $430,000</p><p><a href="details.html" class="btn btn-sm btn-raised">View Listing</a></p></div></div>'
    }
});