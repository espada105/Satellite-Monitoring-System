#!/bin/bash

# 위성 모니터링 시스템 실행 스크립트

echo "🛰️ 위성 모니터링 시스템 시작..."

# 가상환경 활성화 (Python 도구 사용 시)
if [ -d "venv" ]; then
    echo "🐍 Python 가상환경 활성화..."
    source venv/Scripts/activate  # Windows
    # source venv/bin/activate    # Linux/Mac
fi

# 빌드 확인
if [ ! -f "build/bin/satellite_monitor" ]; then
    echo "❌ 실행 파일이 없습니다. 먼저 빌드를 실행하세요:"
    echo "   ./scripts/build.sh"
    exit 1
fi

# 데이터 디렉토리 생성
mkdir -p data/logs/system_logs
mkdir -p data/logs/alert_logs
mkdir -p data/logs/status_reports

echo "📊 모니터링 시스템 실행 중..."
echo "🛑 중단하려면 Ctrl+C를 누르세요"

# 모니터링 시스템 실행
cd build
./bin/satellite_monitor 