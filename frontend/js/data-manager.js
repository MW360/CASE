let devices = null;

$.get("/interfaces/devices", function (data) {
  devices=json.decode(data);
  console.log(devices);
});

