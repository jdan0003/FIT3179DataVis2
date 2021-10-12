var vg_1 = "currentwork.vg.json";
var vg_2 = "combinedstacks.vg.json";
var vg_3 = "worldmapmichelin.vg.json";
var vg_4 = "zoomedEurope.vg.json";
var vg_5 = "zoomedEuropedotmap.vg.json";
var vg_6 = "choroplethmapprice.vg.json";

vegaEmbed("#worldmap2018-2019", vg_1).then(function(result) {}).catch(console.error);

vegaEmbed("#combinedstacks", vg_2).then(function(result){}).catch(console.error);

vegaEmbed("#worldmapmichelin", vg_3).then(function(result){}).catch(console.error);

vegaEmbed("#zoomedEuropeproportional",vg_4).then(function(result){}).catch(console.error);

vegaEmbed("#zoomedEuropedotmap",vg_5).then(function(result){}).catch(console.error);

vegaEmbed("#choroplethmap",vg_6).then(function(result){}).catch(console.error);