#!/bin/bash

echo "🧹 清除殘留的 Appium 進程..."
pkill -f "appium"
sleep 2  # 確保資源釋放
# ===== 模擬器名稱與 Appium port 對應設定 =====
SIMULATORS=("iPhone 16" "iPhone 16 Pro" "iPhone 15" "iPhone 15 Pro")
WDA_PORTS=(8101 8102 8103 8104)
APPIUM_PORTS=(4723 4724 4725 4726)

# ===== 1. Boot 所有模擬器 =====
echo "🚀 Booting iOS Simulators..."
for sim in "${SIMULATORS[@]}"; do
    xcrun simctl boot "$sim" || echo "⚠️ $sim 可能已開啟"
done

sleep 5  # 等待模擬器穩定啟動

# ===== 2. 啟動多個 Appium instance（背景執行）=====
echo "🚀 Starting Appium Servers..."
for i in "${!SIMULATORS[@]}"; do
    port=${APPIUM_PORTS[$i]}
    wda=${WDA_PORTS[$i]}
    echo "🔧 Appium Port: $port | WDA: $wda"
    appium --port $port --use-drivers=xcuitest --default-capabilities "{\"wdaLocalPort\":$wda}" > "appium_$port.log" 2>&1 &
    sleep 2  # 避免同時啟太快
done

sleep 10  # 等待 Appium Server 都穩定起來

# ===== 3. 執行 Pytest 平行測試 =====
echo "🧪 Running Pytest in parallel with 4 workers..."
pytest -n 4

# ===== 4. 結束提示 =====
echo "✅ 測試完成！可檢查 pytest 結果與 appium_xxxx.log"
