async function sendData() {
  const res = await fetch("/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      systolic: parseInt(document.getElementById('sys').value),
      diastolic: parseInt(document.getElementById('dia').value),
      pulse: parseInt(document.getElementById('pulse').value)
    })
  });
  const data = await res.json();
  document.getElementById('result').textContent = data.status + " - " + data.advice;
}
