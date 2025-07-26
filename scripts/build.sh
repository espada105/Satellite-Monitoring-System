#!/bin/bash

# 위성 모니터링 시스템 빌드 스크립트

set -e  # 에러 발생 시 스크립트 중단

echo "🚀 위성 모니터링 시스템 빌드 시작..."

# 빌드 디렉토리 생성
mkdir -p build
cd build

# CMake 설정
echo "📋 CMake 설정 중..."
cmake .. -DCMAKE_BUILD_TYPE=Release

# 빌드 실행
echo "🔨 빌드 실행 중..."
make -j$(nproc)

echo "✅ 빌드 완료!"
echo "📁 실행 파일 위치: build/bin/satellite_monitor"

# 실행 권한 부여
chmod +x bin/satellite_monitor

echo "🎯 빌드된 실행 파일을 실행하려면:"
echo "   ./bin/satellite_monitor" 