function show_time() {
  const d = new Date();
  let h = addZero(d.getHours());
  let m = addZero(d.getMinutes());
  let s = addZero(d.getSeconds());
  let time = h + ":" + m + ":" + s;
  document.getElementById("live").innerHTML = time;
}

function addZero(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}

function update_time() {
  setInterval(show_time, 1000);
}

