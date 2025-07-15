let currentRates = {};

let initializedSelect = false; // 🌟 新增旗標

async function fetchRates() {
  const res = await fetch('/api/rate');
  const data = await res.json();
  currentRates = data;

  // 顯示匯率清單
  const infoDiv = document.getElementById('rate-info');
  let html = '即時匯率:<br>';
  for (const [currency, rateInfo] of Object.entries(currentRates)) {
    html += `${currency}: ${rateInfo.spot_buy}<br>`;
  }
  infoDiv.innerHTML = html;

  // 🌟 只在第一次初始化選單
  if (!initializedSelect) {
    const select = document.getElementById('currency-select');
    select.innerHTML = '';
    for (const currency of Object.keys(currentRates)) {
      const option = document.createElement('option');
      option.value = currency;
      option.textContent = currency;
      select.appendChild(option);
    }
    initializedSelect = true; // 標記已初始化
  }
}

// 監聽輸入和選擇
function updateConversion() {
  if (Object.keys(currentRates).length === 0) return;

  const twd = parseFloat(document.getElementById('twd-input').value);
  const currency = document.getElementById('currency-select').value;
  const resultDiv = document.getElementById('conversion-result');

  if (isNaN(twd)) {
    resultDiv.innerText = '-';
  } else {
    const rate = parseFloat(currentRates[currency].spot_buy);
    const converted = (twd / rate).toFixed(2);
    resultDiv.innerText = `約 ${converted} ${currency}`;
  }
}

document.getElementById('twd-input').addEventListener('input', updateConversion);
document.getElementById('currency-select').addEventListener('change', updateConversion);

fetchRates();

setInterval(async function() {
  await fetchRates();
  updateConversion();
}, 10000);