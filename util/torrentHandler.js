var WebTorrent = require("webtorrent");
var fs = require("fs");

const PATH_TO_MAGNETS =
  "C:\\Users\\Magnus\\Documents\\plex-torrent-server\\instance\\magnetlinks.txt";

var client = new WebTorrent();

var magnetURIs = fs.readFileSync(PATH_TO_MAGNETS, "utf8");
var arrMagnetURIS = magnetURIs.split(",");
console.log(arrMagnetURIS[0]);

client.add(arrMagnetURIS[0], { path: "C:\\Users\\Magnus\\Downloads" }, function(
  torrent
) {
  torrent.on("done", function() {
    console.log("torrent download finished");
    process.exit(1);
  });
});
