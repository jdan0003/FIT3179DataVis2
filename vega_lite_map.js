var vg_1 = "worldmap2018.vg.json";
var vg_2 = "worldmap2019.vg.json";
var vg_3 = "worldmapmichelin.vg.json";

vegaEmbed("#worldmap2018", vg_1).then(function(result) {}).catch(console.error);

vegaEmbed("#worldmap2019", vg_2).then(function(result){}).catch(console.error);

vegaEmbed("#worldmapmichelin", vg_3).then(function(result){}).catch(console.error);