const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm] });
map.
    locate()
    .on("locationfound", (e) => map.setView(e.latlng, 8))
    .on("locationerror", () => map.setView([0, 0], 5));

async function load_markers() {
    const users_url = `/api/users/?in_bbox=${map.getBounds().toBBoxString()}`
    const response = await fetch(users_url)
    const geojson = await response.json()
    return geojson
}

async function render_markers() {
    const users = await load_markers();
    L.geoJSON(users)
    .bindPopup((layer) => layer.feature.properties.username)
    .addTo(map);
}

map.on("moveend", render_markers);
